#!/usr/bin/env python3
"""Deterministically calculate an investment score and position-size ceiling."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = SKILL_DIR / "references" / "model-config.json"


TEMPLATE: dict[str, Any] = {
    "metadata": {
        "company": "Example Company",
        "security": "EXAMPLE",
        "as_of": "YYYY-MM-DD",
        "price": 0.0,
        "price_currency": "USD",
        "valuation_type": "compounder"
    },
    "quality_ratings": {
        "incremental_returns": 2,
        "pricing_power_customer_value": 2,
        "competitive_durability": 2,
        "demand_resilience": 2,
        "concentration_regulation_disruption": 2,
        "growth_runway": 2,
        "reinvestment_optionality": 2,
        "cash_conversion_accounting": 2,
        "balance_sheet_obligations": 2,
        "alignment_disclosure": 2,
        "capital_allocation_record": 2
    },
    "opportunity_metrics": {
        "five_year_expected_return_pct": 9.0,
        "price_as_pct_of_base_value": 90.0,
        "bear_case_downside_pct": 30.0
    },
    "opportunity_ratings": {
        "thesis_evidence_confidence": 2
    },
    "evidence_confidence": "high",
    "risk_flags": [],
    "portfolio": {
        "current_correlated_exposure_excluding_company_pct": None,
        "correlated_exposure_limit_pct": None,
        "user_single_company_limit_pct": None
    }
}


class ScorecardError(ValueError):
    pass


def decimal(value: Any) -> Decimal:
    return Decimal(str(value))


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ScorecardError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ScorecardError(f"Invalid JSON in {path}: {exc}") from exc


def require_exact_keys(actual: dict[str, Any], expected: dict[str, Any], label: str) -> None:
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing or extra:
        parts = []
        if missing:
            parts.append(f"missing={missing}")
        if extra:
            parts.append(f"unexpected={extra}")
        raise ScorecardError(f"{label} keys do not match config: " + ", ".join(parts))


def validate_weights(weights: dict[str, Any], label: str) -> None:
    total = sum((decimal(value) for value in weights.values()), Decimal("0"))
    if total != Decimal("1"):
        raise ScorecardError(f"{label} must sum to 1.0; got {total}")


def validate_ratings(
    ratings: dict[str, Any], weights: dict[str, Any], config: dict[str, Any], label: str
) -> None:
    require_exact_keys(ratings, weights, label)
    minimum = int(config["rating_min"])
    maximum = int(config["rating_max"])
    for key, value in ratings.items():
        if isinstance(value, bool) or not isinstance(value, int):
            raise ScorecardError(f"{label}.{key} must be an integer from {minimum} to {maximum}")
        if value < minimum or value > maximum:
            raise ScorecardError(f"{label}.{key}={value} is outside {minimum}..{maximum}")


def weighted_score(ratings: dict[str, int], weights: dict[str, Any], rating_max: int) -> Decimal:
    weighted_rating = sum(
        (decimal(ratings[key]) * decimal(weight) for key, weight in weights.items()),
        Decimal("0"),
    )
    return weighted_rating / decimal(rating_max) * Decimal("10")


def derive_metric_rating(value: Decimal, rule: dict[str, Any]) -> Decimal:
    if rule.get("method") != "linear_anchors":
        raise ScorecardError(f"Unknown opportunity metric method: {rule.get('method')!r}")

    raw_anchors = rule.get("anchors")
    if not isinstance(raw_anchors, list) or len(raw_anchors) < 2:
        raise ScorecardError("Opportunity metric rule requires at least two anchors")

    anchors = [(decimal(item["value"]), decimal(item["rating"])) for item in raw_anchors]
    if any(right[0] <= left[0] for left, right in zip(anchors, anchors[1:])):
        raise ScorecardError("Opportunity metric anchor values must be strictly increasing")

    if value <= anchors[0][0]:
        return anchors[0][1]
    if value >= anchors[-1][0]:
        return anchors[-1][1]

    for left, right in zip(anchors, anchors[1:]):
        left_value, left_rating = left
        right_value, right_rating = right
        if left_value <= value <= right_value:
            fraction = (value - left_value) / (right_value - left_value)
            return left_rating + fraction * (right_rating - left_rating)

    raise ScorecardError(f"Opportunity metric value {value} could not be interpolated")


def derive_opportunity_ratings(scorecard: dict[str, Any], config: dict[str, Any]) -> dict[str, Decimal]:
    metrics = scorecard.get("opportunity_metrics")
    manual = scorecard.get("opportunity_ratings")
    if not isinstance(metrics, dict) or not isinstance(manual, dict):
        raise ScorecardError("opportunity_metrics and opportunity_ratings must be objects")

    rules = config["opportunity_metric_rules"]
    expected_metric_keys = {rule["input_key"] for rule in rules.values()}
    missing = sorted(expected_metric_keys - set(metrics))
    extra = sorted(set(metrics) - expected_metric_keys)
    if missing or extra:
        raise ScorecardError(f"opportunity_metrics keys mismatch: missing={missing}, unexpected={extra}")
    require_exact_keys(manual, {"thesis_evidence_confidence": None}, "opportunity_ratings")

    thesis = manual["thesis_evidence_confidence"]
    if isinstance(thesis, bool) or not isinstance(thesis, int):
        raise ScorecardError("opportunity_ratings.thesis_evidence_confidence must be an integer")
    if thesis < int(config["rating_min"]) or thesis > int(config["rating_max"]):
        raise ScorecardError("opportunity_ratings.thesis_evidence_confidence is outside the rating range")

    derived: dict[str, Decimal] = {}
    for output_key, rule in rules.items():
        raw_value = metrics[rule["input_key"]]
        if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
            raise ScorecardError(f"opportunity_metrics.{rule['input_key']} must be numeric")
        derived[output_key] = derive_metric_rating(decimal(raw_value), rule)
    derived["thesis_evidence_confidence"] = decimal(thesis)
    return derived


def validate_derived_ratings(
    ratings: dict[str, Decimal], weights: dict[str, Any], config: dict[str, Any]
) -> None:
    require_exact_keys(ratings, weights, "derived_opportunity_ratings")
    minimum = decimal(config["rating_min"])
    maximum = decimal(config["rating_max"])
    for key, value in ratings.items():
        if value < minimum or value > maximum:
            raise ScorecardError(
                f"derived_opportunity_ratings.{key}={value} is outside {minimum}..{maximum}"
            )


def score_band(score: Decimal, bands: list[dict[str, Any]]) -> Decimal:
    for band in bands:
        if decimal(band["min_score"]) <= score < decimal(band["max_score_exclusive"]):
            return decimal(band["ceiling_pct"])
    raise ScorecardError(f"No position band covers score {score}")


def normalized_hash(scorecard: dict[str, Any], config: dict[str, Any]) -> str:
    payload = {"scorecard": scorecard, "config": config}
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def calculate(scorecard: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    quality_weights = config["quality_weights"]
    opportunity_weights = config["opportunity_weights"]
    validate_weights(quality_weights, "quality_weights")
    validate_weights(opportunity_weights, "opportunity_weights")

    quality = scorecard.get("quality_ratings")
    if not isinstance(quality, dict):
        raise ScorecardError("quality_ratings must be an object")
    validate_ratings(quality, quality_weights, config, "quality_ratings")
    opportunity = derive_opportunity_ratings(scorecard, config)
    validate_derived_ratings(opportunity, opportunity_weights, config)

    q_weight = decimal(config["quality_weight_in_total"])
    o_weight = decimal(config["opportunity_weight_in_total"])
    if q_weight + o_weight != Decimal("1"):
        raise ScorecardError("quality_weight_in_total plus opportunity_weight_in_total must equal 1.0")

    rating_max = int(config["rating_max"])
    quality_score = weighted_score(quality, quality_weights, rating_max)
    opportunity_score = weighted_score(opportunity, opportunity_weights, rating_max)
    combined_score = quality_score * q_weight + opportunity_score * o_weight
    score_ceiling = score_band(combined_score, config["position_bands"])

    evidence = scorecard.get("evidence_confidence")
    evidence_caps = config["evidence_confidence_caps_pct"]
    if evidence not in evidence_caps:
        raise ScorecardError(f"Unknown evidence_confidence={evidence!r}; expected one of {sorted(evidence_caps)}")

    risk_flags = scorecard.get("risk_flags", [])
    if not isinstance(risk_flags, list) or any(not isinstance(flag, str) for flag in risk_flags):
        raise ScorecardError("risk_flags must be a list of strings")
    if len(risk_flags) != len(set(risk_flags)):
        raise ScorecardError("risk_flags contains duplicates")
    known_flags = config["risk_flag_caps_pct"]
    unknown_flags = sorted(set(risk_flags) - set(known_flags))
    if unknown_flags:
        raise ScorecardError(f"Unknown risk_flags: {unknown_flags}")

    constraints: list[tuple[str, Decimal]] = [
        ("score_band", score_ceiling),
        (f"evidence:{evidence}", decimal(evidence_caps[evidence])),
        ("single_company_hard_max", decimal(config["maximum_single_company_pct"])),
    ]

    for flag in sorted(risk_flags):
        constraints.append((f"risk_flag:{flag}", decimal(known_flags[flag])))

    for gate in config["rating_gate_caps"]:
        key = gate["rating_key"]
        if quality[key] <= int(gate["at_or_below"]):
            constraints.append((f"rating_gate:{key}<={gate['at_or_below']}", decimal(gate["ceiling_pct"])))

    max_requirements = config["maximum_score_for_20pct_requires"]
    if score_ceiling == decimal(config["maximum_single_company_pct"]):
        failures: list[str] = []
        if combined_score < decimal(max_requirements["combined_score_at_least"]):
            failures.append("combined_score")
        if quality_score < decimal(max_requirements["quality_score_at_least"]):
            failures.append("quality_score")
        if opportunity_score < decimal(max_requirements["opportunity_score_at_least"]):
            failures.append("opportunity_score")
        if quality["alignment_disclosure"] < int(max_requirements["minimum_alignment_disclosure_rating"]):
            failures.append("alignment_disclosure")
        if quality["balance_sheet_obligations"] < int(max_requirements["minimum_balance_sheet_rating"]):
            failures.append("balance_sheet_obligations")
        if evidence != max_requirements["evidence_confidence"]:
            failures.append("evidence_confidence")
        if bool(max_requirements["no_risk_flags"]) and risk_flags:
            failures.append("risk_flags")
        if failures:
            constraints.append(("20pct_eligibility:" + ",".join(failures), Decimal("18")))

    portfolio = scorecard.get("portfolio") or {}
    if not isinstance(portfolio, dict):
        raise ScorecardError("portfolio must be an object")

    user_limit = portfolio.get("user_single_company_limit_pct")
    if user_limit is not None:
        user_limit_value = decimal(user_limit)
        if user_limit_value < 0:
            raise ScorecardError("user_single_company_limit_pct cannot be negative")
        constraints.append(("user_single_company_limit", user_limit_value))

    correlated_exposure = portfolio.get("current_correlated_exposure_excluding_company_pct")
    if correlated_exposure is not None:
        exposure_value = decimal(correlated_exposure)
        if exposure_value < 0:
            raise ScorecardError("current_correlated_exposure_excluding_company_pct cannot be negative")
        configured_limit = portfolio.get("correlated_exposure_limit_pct")
        limit_value = (
            decimal(configured_limit)
            if configured_limit is not None
            else decimal(config["default_correlated_exposure_limit_pct"])
        )
        room = max(Decimal("0"), limit_value - exposure_value)
        constraints.append((f"correlated_exposure_room(limit={limit_value})", room))

    final_ceiling = min(value for _, value in constraints)
    binding = [name for name, value in constraints if value == final_ceiling]

    decimals = int(config["round_score_decimals"])
    quantum = Decimal("1").scaleb(-decimals)

    def rounded(value: Decimal) -> float:
        return float(value.quantize(quantum, rounding=ROUND_HALF_UP))

    rating_quantum = Decimal("0.01")

    result = {
        "model_version": config["model_version"],
        "metadata": scorecard.get("metadata", {}),
        "quality_score": rounded(quality_score),
        "opportunity_score": rounded(opportunity_score),
        "combined_score": rounded(combined_score),
        "combined_score_unrounded": str(combined_score.normalize()),
        "quality_ratings": quality,
        "derived_opportunity_ratings": {
            key: float(value.quantize(rating_quantum, rounding=ROUND_HALF_UP))
            for key, value in opportunity.items()
        },
        "score_based_ceiling_pct": float(score_ceiling),
        "risk_adjusted_ceiling_pct": float(final_ceiling),
        "binding_constraints": binding,
        "all_constraints": [
            {"name": name, "ceiling_pct": float(value)} for name, value in constraints
        ],
        "audit_hash": normalized_hash(scorecard, config),
    }
    return result


def markdown(result: dict[str, Any]) -> str:
    metadata = result.get("metadata", {})
    bindings = ", ".join(result["binding_constraints"])
    lines = [
        f"# {metadata.get('company', 'Company')} investment score",
        "",
        f"- Security: {metadata.get('security', '')}",
        f"- As of: {metadata.get('as_of', '')}",
        f"- Price: {metadata.get('price', '')} {metadata.get('price_currency', '')}",
        f"- Model version: {result['model_version']}",
        f"- Company quality: {result['quality_score']}/10",
        f"- Current opportunity: {result['opportunity_score']}/10",
        f"- Combined score: {result['combined_score']}/10",
        f"- Score-based ceiling: {result['score_based_ceiling_pct']}%",
        f"- Risk-adjusted ceiling: {result['risk_adjusted_ceiling_pct']}%",
        f"- Binding constraint: {bindings}",
        f"- Audit hash: {result['audit_hash']}",
        "",
        "| Constraint | Ceiling |",
        "|---|---:|",
    ]
    lines.extend(
        f"| {item['name']} | {item['ceiling_pct']}% |" for item in result["all_constraints"]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scorecard", nargs="?", type=Path)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--template", action="store_true", help="Print a blank scorecard template")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.template:
        print(json.dumps(TEMPLATE, ensure_ascii=False, indent=2))
        return 0
    if args.scorecard is None:
        print("scorecard is required unless --template is used", file=sys.stderr)
        return 2
    try:
        scorecard = load_json(args.scorecard)
        config = load_json(args.config)
        result = calculate(scorecard, config)
    except ScorecardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.format == "markdown":
        print(markdown(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
