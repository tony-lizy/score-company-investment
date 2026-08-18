---
name: score-company-investment
description: Evaluate a public company as an investment with a reproducible 0–10 score, audited evidence, normalized owner earnings, bear/base/bull valuation, and a disciplined position-size ceiling capped at 20%. Use when analyzing or comparing stocks, assigning an investment-value score, deciding whether a company is buyable at the current price, translating a score into portfolio weight, updating an earlier score, or checking why two analyses of the same company differ.
---

# Score Company Investment

Use a fixed, evidence-first scorecard. Separate company quality from the opportunity created by the current price. Treat the final score as price- and date-specific, not as a permanent company label.

Resolve `SKILL_DIR` to the absolute directory containing this `SKILL.md`. Treat every bundled path below as relative to `SKILL_DIR`, regardless of the current working directory.

## Required files

Before scoring, read:

1. `references/scoring-rubric.md` for all 0–4 anchors.
2. `references/valuation-normalization.md` for the applicable company type and valuation rules.
3. `references/position-sizing.md` for score bands, risk gates, and the 20% hard ceiling.
4. `references/model-config.json` for the exact arithmetic parameters.
5. `references/output-template.md` for the required answer structure.

Do not change weights, thresholds, valuation horizon, or position bands after seeing the company result. A user may override a parameter only prospectively and explicitly; disclose the override prominently.

## Workflow

### 1. Freeze the evaluation contract

State before researching:

- legal company name and security/ticker;
- listing used for price and share count;
- cutoff date, timezone, and last completed market close;
- reporting currency and valuation currency;
- five-year holding horizon;
- whether the task is a fresh score, an update, or a comparison;
- portfolio denominator: total investable equity portfolio net asset value, without leverage.

Do not use information published after the cutoff. When the market is open, use the previous close unless the user explicitly requests an intraday score.

### 2. Establish the evidence ledger

Browse because investment data and prices are time-sensitive. Use sources in this order:

1. regulatory filings and exchange announcements;
2. audited reports, earnings releases, presentations, and transcripts from the company;
3. official regulators and industry bodies;
4. primary competitor filings;
5. reputable reporting for events not yet in filings;
6. analyst estimates only when clearly labeled and never as the sole evidence for a critical input.

Record source URL, publication date, covered period, currency, accounting basis, and whether each number is reported or estimated. If a critical input cannot be verified, issue a score range or “insufficient evidence”; do not manufacture a point estimate.

### 3. Classify the valuation type

Choose exactly one primary type using this order:

1. **Financial**: regulated leverage and capital adequacy define distributable earnings.
2. **Cyclical**: price-taking economics or full-cycle earnings variation dominates value.
3. **Turnaround/pre-profit**: current earnings are not representative and recovery is unproven.
4. **Asset/holding company**: more than roughly 40% of value comes from separable investments or net assets.
5. **Compounder/operating company**: use only if none of the above dominates.

Apply the matching section in `valuation-normalization.md`. Explain borderline classifications. Never choose a type because it produces the highest value.

### 4. Build normalized economics

At minimum calculate or document:

- fully diluted shares and market capitalization;
- debt, lease obligations, restricted cash, customer funds, minority interests, and accessible excess cash;
- revenue, operating profit, attributable earnings, cash from operations, total capex, estimated maintenance capex, stock-based compensation, and net buybacks;
- normalized owner earnings attributable to common shareholders;
- segment economics and any value leakage to minorities or related parties;
- five- to ten-year history where available, with a full cycle for cyclical companies.

Treat stock-based compensation as an economic cost. Count only buybacks exceeding dilution as shareholder return. Do not treat all balance-sheet cash as distributable. Do not use consolidated profit or cash that economically belongs to minority shareholders.

### 5. Value three scenarios

Use a five-year horizon and fixed default probabilities of 25% bear, 50% base, and 25% bull. Estimate for every scenario:

- normalized starting owner earnings;
- five-year operating assumptions;
- cumulative distributions and net share-count change;
- year-five value and terminal multiple or asset value;
- annualized shareholder return from the frozen current price.

Calculate:

- probability-weighted annualized return;
- discount or premium to current base intrinsic value;
- loss from current price to bear intrinsic value.

Label every non-reported assumption. Do not raise a terminal multiple merely to reproduce the current market price.

### 6. Assign the anchored ratings

Score the eleven quality subfactors and `thesis_evidence_confidence` as integers from 0 to 4 using `scoring-rubric.md`. Do not use half-points for manually assigned ratings. Enter the three numeric opportunity metrics; let the script derive continuous 0–4 ratings by linear interpolation between the fixed anchors in `model-config.json`. For each manually assigned rating, provide at least one supporting fact and one counterfact or uncertainty.

Use “2” for genuinely mixed or sector-average evidence. Do not start at 4 and subtract narratively. Missing evidence is not neutral evidence: mark it missing and reduce evidence confidence.

### 7. Calculate deterministically

Create a scorecard JSON matching the schema printed by:

```bash
python3 "$SKILL_DIR/scripts/score_company.py" --template
```

Then run:

```bash
python3 "$SKILL_DIR/scripts/score_company.py" scorecard.json --format markdown
```

Use the script result without manual arithmetic changes. The script returns the quality score, opportunity score, combined score, score-based position ceiling, risk-adjusted ceiling, binding constraint, and an audit hash. Exact same input plus model version must produce the exact same output.

### 8. Run the consistency check

Before finalizing, rescore independently from the evidence ledger without looking at the first total. Compare subratings.

- Reconcile every subrating differing by more than one anchor level.
- Reconcile any total-score difference greater than 0.3.
- If two defensible interpretations remain, report a score range and use the lower end for position sizing.
- When updating a prior analysis, keep unchanged ratings unchanged unless new evidence or price inputs justify a revision.

For a same-company, same-cutoff discrepancy greater than 0.3, show a bridge across: price, diluted shares, accessible net cash, normalized owner earnings, growth, terminal value, scenario downside, and changed subratings. Never silently replace the earlier score.

### 9. Size the position

Treat the script’s percentage as an upper bound, not an instruction to fill immediately. Final position equals the minimum of:

1. score-based ceiling;
2. evidence and structural-risk ceiling;
3. remaining room under the correlated economic-exposure limit;
4. any stricter user-defined portfolio constraint set before the analysis.

Without the user’s current correlated exposures, report only the standalone and risk-adjusted ceilings. Do not call that a final personalized allocation.

Build positions in tranches. Re-underwrite before crossing 10%, 15%, or 18%; price decline alone is not evidence that the thesis improved.

## Reproducibility standard

Target same-company, same-security, same-cutoff variation within ±0.3 when independent analyses use the same evidence set. Exact equality is only guaranteed for identical scorecard JSON and the same `model-config.json`.

Always expose:

- model version;
- cutoff and price;
- all raw 0–4 ratings;
- normalized owner-earnings definition;
- valuation assumptions;
- triggered caps;
- audit hash.

Include the complete scorecard JSON used by the script so another run can reproduce the audit hash. Use single Markdown links for sources; never wrap an existing link inside another link. Do not emit internal citation placeholders or offer reminders unless the user explicitly requested one.

Never hard-code a company, target price, preferred conclusion, or existing holding into the skill.
