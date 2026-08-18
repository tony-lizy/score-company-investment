#!/usr/bin/env python3
"""Regression tests for the deterministic company-scoring model."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from decimal import Decimal
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("score_company.py")
SPEC = importlib.util.spec_from_file_location("score_company", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT_PATH}")
score_company = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score_company)


class ScoreCompanyRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = score_company.load_json(score_company.DEFAULT_CONFIG)

    def pdd_scorecard(self) -> dict:
        return {
            "metadata": {
                "company": "PDD Holdings Inc.",
                "security": "NASDAQ:PDD ADS",
                "as_of": "2026-08-18",
                "price": 86.94,
                "price_currency": "USD",
                "valuation_type": "compounder",
            },
            "quality_ratings": {
                "incremental_returns": 4,
                "pricing_power_customer_value": 2,
                "competitive_durability": 3,
                "demand_resilience": 3,
                "concentration_regulation_disruption": 1,
                "growth_runway": 2,
                "reinvestment_optionality": 2,
                "cash_conversion_accounting": 3,
                "balance_sheet_obligations": 3,
                "alignment_disclosure": 2,
                "capital_allocation_record": 2,
            },
            "opportunity_metrics": {
                "five_year_expected_return_pct": 14.96,
                "price_as_pct_of_base_value": 74.28,
                "bear_case_downside_pct": 47.68,
            },
            "opportunity_ratings": {"thesis_evidence_confidence": 2},
            "evidence_confidence": "medium",
            "risk_flags": ["cash_access_or_structure_risk"],
            "risk_flag_rationales": {
                "cash_access_or_structure_risk": {
                    "rating_role": "Reduces expected access to cash and confidence in distributable economics.",
                    "cap_role": "Limits portfolio damage if contractual access to structurally held assets fails.",
                }
            },
            "portfolio": {
                "current_correlated_exposure_excluding_company_pct": None,
                "correlated_exposure_limit_pct": None,
                "user_single_company_limit_pct": None,
            },
        }

    def test_same_input_is_exactly_reproducible(self) -> None:
        scorecard = self.pdd_scorecard()
        first = score_company.calculate(scorecard, self.config)
        second = score_company.calculate(copy.deepcopy(scorecard), self.config)
        self.assertEqual(first, second)

    def test_expected_return_anchor_is_continuous(self) -> None:
        low = self.pdd_scorecard()
        high = copy.deepcopy(low)
        high["opportunity_metrics"]["five_year_expected_return_pct"] = 15.04
        low_result = score_company.calculate(low, self.config)
        high_result = score_company.calculate(high, self.config)
        self.assertLess(
            abs(high_result["combined_score"] - low_result["combined_score"]),
            0.05,
        )

    def test_pdd_regression_sample(self) -> None:
        result = score_company.calculate(self.pdd_scorecard(), self.config)
        self.assertEqual(result["model_version"], "2.0.1")
        self.assertEqual(result["quality_score"], 6.2)
        self.assertEqual(result["opportunity_score"], 7.9)
        self.assertEqual(result["combined_score"], 7.0)
        self.assertEqual(result["score_based_ceiling_pct"], 5.0)
        self.assertEqual(result["risk_adjusted_ceiling_pct"], 5.0)
        self.assertEqual(
            set(result["binding_constraints"]),
            {"score_band", "risk_flag:cash_access_or_structure_risk"},
        )

    def test_risk_flag_requires_separate_rating_and_cap_roles(self) -> None:
        scorecard = self.pdd_scorecard()
        scorecard["risk_flag_rationales"] = {}
        with self.assertRaises(score_company.ScorecardError):
            score_company.calculate(scorecard, self.config)

    def test_position_band_boundaries(self) -> None:
        bands = self.config["position_bands"]
        self.assertEqual(score_company.score_band(Decimal("6.9999"), bands), Decimal("0.0"))
        self.assertEqual(score_company.score_band(Decimal("7.0"), bands), Decimal("5.0"))
        self.assertEqual(score_company.score_band(Decimal("7.5"), bands), Decimal("8.0"))
        self.assertEqual(score_company.score_band(Decimal("8.0"), bands), Decimal("10.0"))
        self.assertEqual(score_company.score_band(Decimal("9.5"), bands), Decimal("20.0"))


if __name__ == "__main__":
    unittest.main()
