# Scoring rubric

## Contents

1. Rating discipline
2. Company quality: 50% of total
3. Current opportunity: 50% of total
4. Evidence confidence
5. Cross-check rules

## 1. Rating discipline

Rate each company-quality subfactor and `thesis_evidence_confidence` with an integer from 0 to 4. The script derives the other three opportunity ratings directly from numeric valuation inputs by linear interpolation between fixed anchors. Derived ratings may contain decimals; never round an input merely to cross an anchor.

| Rating | General meaning |
|---:|---|
| 0 | Structurally destructive, unsupported, or clearly unacceptable |
| 1 | Weak; materially below a rational sector benchmark |
| 2 | Mixed, average, or insufficiently differentiated |
| 3 | Strong and supported by several periods of evidence |
| 4 | Exceptional, durable, and supported across a cycle or long history |

Use sector-appropriate economics, but do not grade on a curve so generous that every sector leader receives 4. A 4 must be rare. When evidence lies on a boundary, use the lower rating unless the stronger rating is supported by both quantitative history and a causal explanation.

Do not use stock-price performance, market popularity, analyst recommendations, or the investor’s existing position as evidence of company quality.

## 2. Company quality: 50% of total

### 2.1 Incremental returns — 10%

Measure returns on new capital, not only historical average ROE inflated by old assets, leverage, or intangible accounting.

| Rating | Anchor |
|---:|---|
| 0 | New investment persistently destroys value or economics cannot be reconstructed |
| 1 | Incremental return is below cost of capital, negative, or highly erratic |
| 2 | Roughly earns cost of capital; evidence is mixed or cycle-dependent |
| 3 | Sustainably exceeds cost of capital, commonly around 12%–20% for non-financial companies |
| 4 | Sustainably above roughly 20%, with meaningful reinvestment capacity and no hidden leverage or underinvestment |

For financial institutions, use incremental ROTCE or equivalent relative to cost of equity and required capital. For asset-light companies, include capitalized customer acquisition, SBC, leases, and acquisitions where economically relevant.

### 2.2 Pricing power and customer value — 8%

| Rating | Anchor |
|---:|---|
| 0 | Customers leave rapidly without discounts; product is structurally obsolete |
| 1 | Price taker with persistent discounting or subsidy dependence |
| 2 | Can broadly hold price but has no demonstrated premium or switching advantage |
| 3 | Repeated price/mix improvement or monetization gains with stable retention and share |
| 4 | Customers accept a persistent premium or the company captures more value while customer economics and retention remain strong across weak demand periods |

Distinguish genuine pricing power from inflation pass-through, mix changes, channel loading, temporary scarcity, or reduced product quality.

### 2.3 Competitive durability — 7%

| Rating | Anchor |
|---:|---|
| 0 | Advantage is disappearing or business is being displaced |
| 1 | Little differentiation; competitors can replicate the offer cheaply |
| 2 | Some scale, brand, data, distribution, cost, or switching advantage, but contestable |
| 3 | Multiple reinforcing advantages with a demonstrated multi-year record |
| 4 | Self-reinforcing network, cost, brand, standard, distribution, regulatory, or ecosystem advantage that has survived major technological and economic changes |

Market share alone is not a moat. High concentration alone does not establish pricing discipline. State protection is not automatically durable value for minority shareholders.

### 2.4 Demand resilience — 8%

Use normalized attributable owner earnings, not revenue alone.

| Rating | Anchor |
|---:|---|
| 0 | Existential demand decline or repeated insolvency risk |
| 1 | Full-cycle earnings drawdowns commonly exceed 50%, or demand is highly discretionary/commodity-driven |
| 2 | Drawdowns around 30%–50%, material cyclicality, or limited history |
| 3 | Drawdowns generally around 15%–30% with fast recovery and limited permanent impairment |
| 4 | Essential or habitual demand, diversified revenue, and normalized earnings drawdowns generally below 15% across stress periods |

Do not give 4 to a young company lacking a real stress period.

### 2.5 Concentration, regulation, and disruption — 7%

This rating is higher when dependency risk is lower.

| Rating | Anchor |
|---:|---|
| 0 | One unresolved event can plausibly destroy most equity value |
| 1 | Severe customer, supplier, founder, jurisdiction, product, funding, or regulatory dependency |
| 2 | One or two material dependencies with partial mitigants |
| 3 | Risks are diversified, funded, and operationally manageable |
| 4 | Broad diversification plus proven adaptation; no single realistic disruption threatens the investment case |

Explicitly consider technology substitution, platform dependence, geopolitical restrictions, licenses, VIE/holding structures, and key-person risk.

### 2.6 Growth runway — 10%

Use conservative five-year per-share owner-earnings growth after dilution, not management TAM claims.

| Rating | Anchor |
|---:|---|
| 0 | Structural decline, expected contraction, or growth has no economic value |
| 1 | Approximately 0%–3% annual per-share growth or highly uncertain recovery |
| 2 | Approximately 3%–8% annual per-share growth |
| 3 | Approximately 8%–15% annual per-share growth with visible drivers |
| 4 | At least roughly 15% annual per-share growth with a long runway, strong unit economics, and limited dilution |

For cyclical companies, score normalized through-cycle growth rather than peak-to-trough rebound. Acquired revenue is not organic growth unless acquisition economics are included.

### 2.7 Reinvestment and optionality — 10%

| Rating | Anchor |
|---:|---|
| 0 | Reinvestment destroys value; “optionality” consists mainly of unsupported narratives |
| 1 | Few attractive uses of capital or repeated speculative spending |
| 2 | Can reinvest part of earnings near cost of capital; optional projects remain unproven |
| 3 | Several scalable reinvestment channels with demonstrated attractive returns |
| 4 | Can reinvest a large share of cash for many years at exceptional incremental returns; new options emerge from existing capabilities and distribution |

Do not count the same growth twice: growth runway measures the likely result; reinvestment measures the economics and repeatability of producing it.

### 2.8 Cash conversion and accounting quality — 10%

Use normalized owner earnings attributable to common shareholders.

| Rating | Anchor |
|---:|---|
| 0 | Cash generation is persistently negative or accounting cannot be trusted |
| 1 | Normalized owner earnings are below roughly 50% of adjusted earnings, or depend on working-capital extraction/SBC |
| 2 | Roughly 50%–75% conversion, capital intensity is material, or adjustments are uncertain |
| 3 | Roughly 75%–100% conversion with understandable working capital, capex, tax, and SBC |
| 4 | Consistently high conversion across a cycle, conservative accounting, low hidden obligations, and minimal gap between economic and reported earnings |

For financial institutions, replace CFO conversion with reserve quality, credit costs, capital generation, and distributable earnings. Never treat deposit inflows as operating cash flow.

### 2.9 Balance sheet and obligations — 10%

| Rating | Anchor |
|---:|---|
| 0 | Distress, covenant/refinancing dependence, or credible equity impairment risk |
| 1 | High leverage, short maturity wall, weak interest coverage, or inaccessible cash |
| 2 | Manageable but meaningful leverage/leases/commitments; limited stress capacity |
| 3 | Conservative leverage, strong liquidity, and obligations covered under bear assumptions |
| 4 | Accessible net cash or exceptional regulatory capital, no material refinancing dependence, and ample capacity after committed capex and contingencies |

Consolidated cash is not automatically accessible to the listed parent. Deduct restricted cash, customer funds, minority claims, committed capex, tax leakage, and minimum operating cash.

### 2.10 Alignment and disclosure — 10%

| Rating | Anchor |
|---:|---|
| 0 | Fraud indicators, abusive related-party transactions, or minority rights are not credible |
| 1 | Material opacity, cash-access uncertainty, controlling-holder leakage, or repeated disclosure failures |
| 2 | Legally adequate disclosure and mixed alignment; important economic data remain unavailable |
| 3 | Clear segment and capital-allocation disclosure, credible ownership alignment, and respectful minority treatment |
| 4 | Exceptional transparency, long record of candid error reporting, clear economic ownership, and incentives tightly linked to durable per-share value |

Founder ownership is neither automatically positive nor negative. Evaluate control, incentives, succession, related parties, voting rights, and actual treatment of outside shareholders.

### 2.11 Capital-allocation record — 10%

Evaluate at least five years and preferably ten.

| Rating | Anchor |
|---:|---|
| 0 | Repeated large value destruction, unjustified dilution, or extraction from minorities |
| 1 | Poor acquisitions, empire building, buybacks offset mainly by dilution, or cash hoarding without credible purpose |
| 2 | Mixed record; some rational distributions but inconsistent reinvestment/M&A discipline |
| 3 | Mostly value-accretive reinvestment, sensible leverage, and distributions responsive to opportunity |
| 4 | Exceptional per-share compounding record: disciplined M&A, buybacks below intrinsic value, rational dividends, and willingness to shrink or exit low-return activities |

Do not reward dividends or buybacks in isolation. Measure whether each action increased per-share intrinsic value after dilution, taxes, and opportunity cost.

## 3. Current opportunity: 50% of total

### 3.1 Five-year probability-weighted annualized return — 40%

Include cumulative dividends, net buybacks/dilution, and year-five value. Use the fixed 25% bear / 50% base / 25% bull probabilities unless the user changed the model before the company was selected.

Enter the calculated percentage as `five_year_expected_return_pct`; do not assign this rating manually. The listed return levels are continuous anchors: interpolate linearly between them and cap the result to 0–4. The 0 anchor is -1% and the 4 anchor is 15%, so a value immediately below 15% remains immediately below 4 rather than falling to 3.

| Rating | Annualized return anchor |
|---:|---|
| 0 | -1% or lower |
| 1 | 3% |
| 2 | 7% |
| 3 | 11% |
| 4 | 15% or higher |

Use nominal returns in the valuation currency. Explain material currency exposure separately. Do not count excess cash twice in both earnings and terminal value.

### 3.2 Margin of safety to base intrinsic value — 25%

Define price/value as current fully diluted equity value divided by base intrinsic equity value.

Enter the percentage as `price_as_pct_of_base_value`; do not assign this rating manually. Interpolate linearly between the listed anchors. Use 140% as the 0 anchor and cap values below 70% at 4.

| Rating | Price as percentage of base value |
|---:|---|
| 0 | 140% or higher |
| 1 | 120% |
| 2 | 100% |
| 3 | 85% |
| 4 | 70% or lower |

If base value requires an unproven turnaround, lower `thesis_evidence_confidence`; do not inflate the margin-of-safety rating by treating an aspirational case as base.

### 3.3 Bear-case downside — 20%

Measure permanent-value downside from current price to bear intrinsic value, not temporary share-price volatility. Higher ratings mean less downside.

Enter the percentage as `bear_case_downside_pct`; use a negative number when bear value exceeds current price. Do not assign this rating manually. Interpolate linearly between the listed anchors. Use 80% downside as the 0 anchor and cap downside of 10% or less at 4.

| Rating | Downside to bear value |
|---:|---|
| 0 | 80% or more |
| 1 | 60% |
| 2 | 40% |
| 3 | 25% |
| 4 | 10% or less, including bear value above price |

Bear assumptions must be economically coherent and severe enough to matter: recession, margin compression, lower terminal value, execution failure, and balance-sheet stress where relevant.

### 3.4 Thesis evidence confidence — 15%

| Rating | Anchor |
|---:|---|
| 0 | Critical evidence is unavailable; valuation rests mainly on narrative |
| 1 | Four or more major uncertain assumptions must all work, or economic ownership is unclear |
| 2 | Two or three major uncertainties; evidence supports more than one materially different value |
| 3 | One major uncertainty, with most value supported by reported economics and conservative assumptions |
| 4 | Value is supported by observable assets/cash flows across scenarios and does not require a catalyst, multiple expansion, or heroic forecast |

This subfactor measures valuation confidence, while the separate evidence-confidence field controls the maximum permissible position when source coverage is incomplete.

## 4. Evidence confidence

Assign one of three values:

- `high`: latest primary filings are available; ownership, share count, debt/cash, cash flow, and major segments are reconcilable.
- `medium`: analysis is possible, but one important item relies on estimation, incomplete interim data, or secondary sourcing.
- `insufficient`: a critical ownership, solvency, cash-flow, or valuation input cannot be reasonably bounded.

Evidence confidence cannot be raised merely because several secondary sources repeat the same number.

## 5. Cross-check rules

Before calculation:

1. Reconcile diluted shares with buybacks and SBC.
2. Reconcile enterprise value with accessible rather than consolidated cash.
3. Reconcile owner earnings with both income statement and cash flow.
4. Check whether growth is per share and after acquisition spending.
5. Check whether bear/base/bull terminal assumptions follow the selected valuation type.
6. Check that every 4 rating contains multi-period or through-cycle evidence.
7. Check that no fact is counted in more than one rating without explaining the different causal role.
8. Distinguish score effects from position caps: a raw rating measures expected economics; a structural cap limits portfolio damage from a tail event. Do not repeat the same narrative penalty without this distinction.
