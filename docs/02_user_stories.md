# User Stories & Acceptance Criteria

**Project:** Sales & Customer Analytics Dashboard
**Format:** As a [role], I want [feature], so that [benefit]
**Estimation:** Story points (Fibonacci: 1, 2, 3, 5, 8)

## Epics
| Epic | Description |
|---|---|
| E1 Data Preparation | Clean and model the raw transactional data |
| E2 KPI Dashboard | Headline metrics and revenue trend |
| E3 Product & Geography | Product and country performance |
| E4 Customer Segmentation | RFM-based customer groups |
| E5 Returns | Cancellation analysis |
| E6 UAT & Release | Testing and sign-off |

## Story Summary
| ID | Epic | Story | Priority | Points | Sprint |
|---|---|---|---|---|---|
| US-01 | E1 | Cleaned dataset | Must | 5 | 1 |
| US-02 | E1 | Data dictionary | Should | 2 | 1 |
| US-03 | E2 | KPI scorecards | Must | 3 | 1 |
| US-04 | E2 | Monthly revenue trend + date filter | Must | 3 | 1 |
| US-05 | E3 | Top 10 products | Must | 3 | 2 |
| US-06 | E3 | Revenue by country | Should | 3 | 2 |
| US-07 | E4 | RFM customer segments | Must | 8 | 2 |
| US-08 | E5 | Cancellation rate by product | Should | 3 | 2 |
| US-09 | E6 | UAT execution and sign-off | Must | 3 | 2 |

---

## US-01: Cleaned dataset
**As a** data analyst, **I want** the raw data cleaned (duplicates removed, cancellations flagged, invalid rows excluded) **so that** all KPIs are reliable.

**Acceptance Criteria**
- Given the raw file, when the cleaning script runs, then exact duplicate rows are removed.
- Given invoices starting with "C", when cleaning, then they are flagged as cancellations and excluded from revenue.
- Given rows with Quantity <= 0 or Price <= 0, when cleaning, then they are excluded from sales.
- Given the script finishes, then row counts (raw, valid, cancelled) are printed for audit.

## US-02: Data dictionary
**As a** BA, **I want** a data dictionary **so that** stakeholders understand every field and cleaning rule.

**Acceptance Criteria**
- Every raw and derived field is listed with type, description, and rule.
- The file is stored at `docs/03_data_dictionary.md`.

## US-03: KPI scorecards
**As a** Head of Sales, **I want** Total Revenue, Orders, Customers and Average Order Value on one page **so that** I can see business health at a glance.

**Acceptance Criteria**
- Given the dashboard opens, then four scorecards are visible on page 1.
- Revenue excludes cancelled invoices.
- AOV = Total Revenue / Number of Orders.
- Values match the Python script output.

## US-04: Monthly revenue trend with date filter
**As a** Head of Sales, **I want** a monthly revenue trend with a date filter **so that** I can spot seasonality.

**Acceptance Criteria**
- Given the dashboard opens, then a line chart shows revenue by month.
- Given I select Jan-Mar 2011, then the chart and scorecards update to that range.

## US-05: Top 10 products
**As an** Operations Manager, **I want** the top 10 products by revenue and quantity **so that** I can plan stock.

**Acceptance Criteria**
- A bar chart shows the top 10 products, sorted high to low.
- I can switch between Revenue and Units.
- Product description is shown, not only the code.

## US-06: Revenue by country
**As a** Head of Sales, **I want** revenue by country **so that** I can target markets.

**Acceptance Criteria**
- A map or table shows revenue per country.
- A country filter updates all page 1 and page 2 charts.
- UK is clearly the largest market and is visible in the ranking.

## US-07: RFM customer segments
**As a** Marketing Manager, **I want** customers grouped into RFM segments **so that** I can run targeted campaigns.

**Acceptance Criteria**
- Recency, Frequency and Monetary are calculated per customer.
- Customers are scored 1-4 on each and assigned a segment (Champions, Loyal, Potential, At Risk, Lost).
- Dashboard shows customer count and revenue per segment.
- Rows without a Customer ID are excluded and this is documented.
- Segment counts add up to the total number of known customers.

## US-08: Cancellation rate by product
**As an** Operations Manager, **I want** to see cancelled units by product **so that** I can find problem products.

**Acceptance Criteria**
- A chart shows the top products by cancelled units.
- Overall cancellation rate (cancelled invoices / total invoices) is displayed.

## US-09: UAT execution and sign-off
**As a** BA, **I want** UAT test cases executed against the dashboard **so that** each requirement is validated before release.

**Acceptance Criteria**
- Every Must requirement has at least one test case.
- Results (Pass/Fail) are recorded in `docs/05_UAT_test_cases.md`.
- Any failed test is fixed and retested.
- Sign-off is recorded.

---

## Definition of Done
- Acceptance criteria met
- Data reconciled with the Python output
- Screenshot saved in the repo
- Jira card moved to Done
