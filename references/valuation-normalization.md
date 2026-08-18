# Valuation and normalization rules

## Contents

1. Rules applying to every company
2. Compounder or operating company
3. Cyclical company
4. Financial institution
5. Asset or holding company
6. Turnaround or pre-profit company
7. Scenario construction
8. Prohibited shortcuts

## 1. Rules applying to every company

Use a five-year holding horizon. Value the common equity actually owned through the selected security.

Start from reported figures and build a bridge to normalized owner earnings:

`attributable operating earnings after tax`

`+ non-cash charges that are not economic costs`

`- maintenance capital expenditure`

`- recurring lease principal and similar financing-like operating obligations`

`- stock-based compensation or the economic cost of offsetting dilution`

`- recurring cash needed for working-capital growth`

`- minority-shareholder and structural leakage`

`= normalized owner earnings attributable to common shareholders`

Do not automatically add depreciation. Do not automatically equate total capex with maintenance capex. Show both and explain the estimate. If maintenance capex cannot be bounded, use a range.

Accessible excess cash equals cash and liquid investments minus debt, restricted/customer cash, minority claims, committed capex, likely tax leakage, legal contingencies, and minimum operating liquidity. Apply a haircut when transferability is uncertain. Record interest income consistently: if excess cash is added separately, remove its after-tax income from operating earnings.

Use fully diluted shares. Treat SBC as a cost even if a non-GAAP metric excludes it. Count buybacks only net of issued shares and SBC dilution.

## 2. Compounder or operating company

Use normalized current owner earnings only when recent margins and working capital are representative. Otherwise use a three- to five-year normalized margin applied to current sustainable revenue.

Base growth must be consistent with market size, reinvestment, unit economics, and per-share dilution. It cannot exceed the lower of a defensible industry/company runway and demonstrated economics without explicit evidence.

Set the base terminal multiple no higher than the lowest defensible value among:

- the company’s ten-year median through comparable regimes;
- a quality-adjusted peer median;
- the multiple justified by terminal growth, returns, and risk.

When less than ten years of comparable history exists, use a wider value range and lower evidence confidence. The bull multiple should normally be no more than 1.2 times base and not above a relevant historical 75th percentile. The bear multiple should normally be no more than 0.7 times base and should consider the historical 25th percentile.

## 3. Cyclical company

Do not extrapolate current spot prices, freight rates, commodity prices, utilization, or peak margins.

Use at least one full cycle and preferably seven to ten years. Reconstruct normalized volume, unit revenue, unit cost, maintenance capex, and required working capital. Separate structural change from cycle position.

Base value uses mid-cycle owner earnings. Bear value must include a trough period long enough to test liquidity and committed capex. Bull value may include temporary excess profits, but capitalize them for only the period economically justified; do not apply a high terminal multiple to peak earnings.

When cycle history is incomplete or structural capacity additions make the old cycle non-comparable, trigger `cyclical_normalization_uncertain`.

## 4. Financial institution

Do not use conventional CFO minus capex. Use distributable earnings after credit costs, insurance reserving, required regulatory capital, and realistic through-cycle losses.

Value with a combination of normalized ROTCE/ROE, tangible book or embedded value where appropriate, and distributable capital. Deduct capital that cannot be distributed without weakening required solvency. Stress funding, asset quality, duration, and regulatory intervention.

Do not compare a bank’s deposits or an insurer’s float with industrial-company debt. Do not count required capital as excess cash.

## 5. Asset or holding company

Use a sum-of-the-parts model. Value each asset once, deduct parent debt, tax leakage, corporate costs, minority interests, and structural discounts supported by actual control and distribution limits.

Use market value for listed holdings with an explicit liquidity/tax/control haircut. Use conservative peer or transaction values for private assets. Do not add associate earnings to value when the underlying associate is already valued separately.

The base case cannot assume the holding-company discount closes without a credible mechanism. If cash or investments cannot be distributed to the listed security, trigger `cash_access_or_structure_risk`.

## 6. Turnaround or pre-profit company

Do not treat management targets as normalized earnings. Base value may include recovery only to levels supported by achieved unit economics, funded capacity, signed demand, or comparable historical operations.

Separate survival value, current operating value, and optional recovery value. Bear value must model the financing required before breakeven, including dilution. If the turnaround is not yet demonstrated in reported cash flow or unit economics, trigger `unproven_turnaround`.

Use revenue multiples only as a cross-check. Convert them into implied margins, capital needs, dilution, and owner earnings before scoring expected return.

## 7. Scenario construction

Keep probabilities fixed at 25% bear, 50% base, and 25% bull unless the user changes the model before company selection.

For each scenario show:

1. starting normalized owner earnings or asset value;
2. five-year revenue/volume and margin path;
3. maintenance and growth investment;
4. distributions, SBC, and net share change;
5. accessible excess cash at year five;
6. terminal multiple or asset valuation;
7. total terminal shareholder wealth and annualized return.

Calculate probability-weighted terminal wealth first, then calculate its five-year CAGR from current equity value. Also show the three scenario CAGRs separately.

Base intrinsic value is today’s value of the base scenario using a discount rate consistent with the required return. Do not use a lower discount rate simply because the business has recently performed well.

## 8. Prohibited shortcuts

- Do not use headline P/E without reconciling one-offs, associates, minorities, SBC, and excess cash.
- Do not call cash “net cash” without deducting debt, leases, restrictions, commitments, and operating needs.
- Do not use EBITDA as owner earnings.
- Do not normalize a cyclical company from only the last three years.
- Do not value a turnaround on fully recovered margins without funding and execution evidence.
- Do not add buyback yield when buybacks merely offset dilution.
- Do not treat high reported ROE caused by leverage or negative equity as business quality.
- Do not use target prices or consensus recommendations as intrinsic value.
