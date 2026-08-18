# Required output template

Use this structure for every full analysis. A short user request may receive a concise answer, but never omit the audit table, score decomposition, or binding position cap.

## 1. Evaluation contract

| Item | Value |
|---|---|
| Company/security | |
| Cutoff and price | |
| Reporting/valuation currency | |
| Primary valuation type | |
| Holding horizon | Five years |
| Model version | |

## 2. Conclusion first

State:

- combined investment score out of 10;
- company-quality score;
- current-opportunity score;
- score-based standalone ceiling;
- risk-adjusted ceiling and binding constraint;
- one-sentence investment classification.

Do not call a score-based ceiling a personalized final weight unless current correlated portfolio exposures were provided. If a disclosed existing position exceeds the standalone or risk-adjusted ceiling, state the mismatch and required re-underwriting; do not convert the model ceiling into an unconditional market-order instruction.

## 3. Fact and normalization ledger

Show current market capitalization, fully diluted shares, accessible net cash/debt, normalized owner earnings, owner-earnings definition, and major segment/ownership adjustments. Cite every critical fact next to the claim.

Separate:

- reported facts;
- mechanical calculations;
- analyst estimates;
- assumptions.

## 4. Scenario valuation

| Scenario | Probability | Core assumptions | Intrinsic value/share | Five-year annualized return |
|---|---:|---|---:|---:|
| Bear | 25% | | | |
| Base | 50% | | | |
| Bull | 25% | | | |

Then show probability-weighted annualized return, price/base value, and downside to bear value.

## 5. Raw scorecard

| Quality subfactor | Weight | Rating 0–4 | Supporting fact | Counterfact/uncertainty |
|---|---:|---:|---|---|

Include all eleven quality subfactors.

| Opportunity subfactor | Weight | Derived rating 0–4 | Numeric input and interpolation anchors |
|---|---:|---:|---|

Include all four opportunity subfactors.

Display the three mechanically derived ratings to two decimals and `thesis_evidence_confidence` as an integer. Do not replace continuous derived ratings with lower integer bands.

Show the unrounded combined score for band selection and the displayed score rounded to one decimal.

## 6. Position calculation

| Constraint | Ceiling |
|---|---:|
| Score band | |
| Evidence confidence | |
| Rating gates | |
| Structural flags | |
| Correlated-exposure room | Not calculated if portfolio data absent |
| Final permitted ceiling | |

Explain why the lowest constraint binds. State what evidence or price change would move the company into the next higher or lower band.

## 7. Falsification and monitoring

List:

- the three facts most likely to disprove the thesis;
- quantitative thresholds that would change at least one raw rating;
- the next filing/event that can test each threshold.

## 8. Reproducibility block

Provide:

```text
model_version:
as_of:
security:
price:
evidence_confidence:
risk_flags:
audit_hash:
```

If updating a previous score, add a score bridge showing every changed input and rating.

## 9. Machine-readable scorecard

Include the complete JSON passed to `score_company.py`. This is required to reproduce the audit hash. Do not include private portfolio data unless the user supplied it for this analysis.

## Formatting constraints

- Use one Markdown link per source; never nest a linked citation inside another link.
- Do not emit `chatgpt-content-reference`, tool reference IDs, or any other internal placeholder.
- Do not suggest or create a reminder unless the user explicitly requests one.
