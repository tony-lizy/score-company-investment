# Position-sizing discipline

## Contents

1. Governing principle
2. Score-based standalone ceiling
3. Why the curve is nonlinear
4. Hard gates and structural caps
5. Portfolio correlation
6. Building and changing a position
7. Requirements for a 20% position

## 1. Governing principle

The score determines a maximum permitted weight, not a mandatory target. Position size must reflect both expected return and the consequence of being wrong.

Calculate:

`final permitted weight = min(score ceiling, evidence cap, structural-risk caps, rating gates, remaining correlated-exposure room, user pre-committed limit)`

Express weight as a percentage of total investable equity portfolio net asset value, including portfolio cash and excluding borrowed capital. Never increase the denominator by using leverage.

The model’s hard ceiling for one company is 20%. It represents an exceptional company purchased at an exceptional opportunity, not merely a company that the investor understands well.

## 2. Score-based standalone ceiling

| Combined score | Standalone ceiling |
|---:|---:|
| Below 7.00 | 0% |
| 7.00–7.49 | 5% |
| 7.50–7.99 | 8% |
| 8.00–8.49 | 10% |
| 8.50–8.99 | 12% |
| 9.00–9.24 | 15% |
| 9.25–9.49 | 18% |
| 9.50–10.00 | 20% |

Use the unrounded combined score for band selection and display the score rounded to one decimal. This prevents a displayed 7.0 created by rounding from incorrectly crossing the 7.00 threshold.

## 3. Why the curve is nonlinear

- Below 7.0, the combination of expected return, business quality, and downside is not strong enough to justify company-specific risk. A watchlist has zero capital cost.
- At 7.0, 5% is a meaningful initial allocation while limiting the cost of a major analytical error. A known but bounded weakness may be acceptable when the price compensates for it; structural caps still apply.
- At 7.5, the ceiling rises to 8%, but the company or opportunity can still contain material uncertainty.
- At 8.0, a company earns a 10% ceiling only when business quality and current opportunity jointly support a full-sized position.
- From 8.5 to 9.0, weights rise gradually because better evidence and asymmetric valuation reduce, but do not eliminate, uncertainty.
- Above 9.0, each additional point requires both high quality and high opportunity; position growth slows as concentration risk becomes dominant.
- At 20%, a 50% permanent loss costs 10% of the entire portfolio. No score can eliminate fraud, regulation, technological discontinuity, key-person events, war, or analytical error. This irreducible risk is why the model stops at 20%.

The curve is deliberately not linear. A move from 7 to 8 is mainly the transition from a starter position to a normal full position; a move from 9 to 10 does not justify doubling an already concentrated position.

## 4. Hard gates and structural caps

Apply every relevant cap; the lowest one binds.

### Evidence caps

| Evidence confidence | Maximum |
|---|---:|
| Insufficient | 0% |
| Medium | 10% |
| High | 20% |

### Fixed risk flags

| Trigger | Maximum |
|---|---:|
| Binary permanent-loss risk | 5% |
| Cash-access, VIE, holding-structure, or minority-leakage risk | 5% |
| High financial leverage/refinancing dependence | 5% |
| Unproven turnaround | 8% |
| Uncertain cyclical normalization | 10% |

Trigger a flag only with evidence and explain it. Do not omit a flag merely because applying it would reduce an existing position.

Do not use a risk flag as a second narrative score deduction. The related raw rating estimates the probability and economic impact of the weakness; the flag limits portfolio damage if the tail event occurs. Apply both only when those two roles are stated separately.

### Rating gates

- `alignment_disclosure` at 0 or 1: maximum 5%.
- `balance_sheet_obligations` at 0 or 1: maximum 5%.
- `capital_allocation_record` at 0 or 1: maximum 8%.

These gates prevent an attractive price from numerically compensating for a potentially fatal governance or solvency weakness.

## 5. Portfolio correlation

The default limit for one correlated economic-exposure group is 30%. Examples include companies dependent on the same commodity price, Chinese premium-liquor demand, one property cycle, one funding market, or the same regulatory platform.

Correlation is economic, not based only on exchange sector labels. If current correlated exposure is 24%, a new position in the same group has at most 6% room even if its standalone ceiling is 15%.

The 30% group limit is a disclosed default model parameter. A user may set a different limit before scoring, but the analyst must not loosen it after seeing an attractive result.

If portfolio exposures are unavailable, report the standalone and risk-adjusted ceilings and state that the correlation constraint has not been calculated.

## 6. Building and changing a position

- Enter in at least two tranches when the permitted ceiling exceeds 5%.
- Re-underwrite the full evidence ledger before crossing 10%, 15%, or 18%.
- Add because expected return or evidence improved, not because the share price fell in isolation.
- Reduce when score or risk ceiling falls below current weight; do not wait for the market price to recover as a separate thesis.
- Treat this as a portfolio-discipline breach requiring re-underwriting and an explicit reduction plan, not as an instruction to submit an immediate market order without considering taxes, liquidity, trading constraints, and the user's current portfolio data.
- Do not raise a score because the investor already owns the stock or lower it merely because the share price has fallen.
- Recalculate after a material filing, capital-allocation decision, governance event, balance-sheet change, or price movement large enough to cross an opportunity anchor.

## 7. Requirements for a 20% position

All conditions must hold:

1. Combined score is at least 9.50 before rounding.
2. Company-quality score is at least 9.0.
3. Current-opportunity score is at least 9.0.
4. `alignment_disclosure` is at least 3.
5. `balance_sheet_obligations` is at least 3.
6. Evidence confidence is high.
7. No structural risk flag is active.
8. The resulting position stays within the correlated-exposure limit.
9. No portfolio leverage is used.

If the combined score maps to 20% but any condition fails, cap the position at 18% before applying stricter gates. In practice, a 20% result should be rare because it requires a strong company and a deeply favorable price simultaneously.
