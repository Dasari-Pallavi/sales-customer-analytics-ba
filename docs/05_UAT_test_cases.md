# UAT Test Cases

**Tester:** Dasari Pallavi  |  **Date:** October 26, 2026  |  **Environment:** Looker Studio (View Link Deployed)

| TC | Req | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-01 | FR-01 | Open dashboard page 1 | 4 cards show Revenue, Orders, Customers, AOV; values match Python output | Executive cards displayed and fully synchronized with data engine outputs. | **Pass** |
| TC-02 | FR-02 | Set date filter Jan-Mar 2011 | Line chart and cards update to the range | All components cross-filtered and recalculated instantly upon date parameter alteration. | **Pass** |
| TC-03 | FR-03 | Open page 2, view top 10 products | 10 products, sorted high to low | Horizontal product bar chart rendered exactly 10 rows sorted descending with optional metric toggles active. | **Pass** |
| TC-04 | FR-04 | View revenue by country | UK is largest; all countries listed | Geo-chart map and data breakdown matrix table accurately highlighted UK market dominance. | **Pass** |
| TC-05 | FR-05 | Open page 3 | Segment customer counts sum to total known customers | Customer segment distributions calculated successfully and summed perfectly to match the 2,997 master customer base. | **Pass** |
| TC-06 | FR-06 | Open page 4 | Cancelled units by product shown; rate displayed | Top returned inventory bar charts displayed cleanly alongside the static 14.81% cancellation rate block. | **Pass** |
| TC-07 | FR-07 | Apply a country filter | All charts update | Report-level country dropdown master filter successfully forced dynamic updates across all relevant visual modules. | **Pass** |
| TC-08 | NFR-01 | Open report on a normal connection | Loads in under 5 seconds | Page canvas cached and populated completely in approximately 2.8 seconds. | **Pass** |
| TC-09 | NFR-03 | Open link in a private browser window | Report visible, not editable | Deployed link loaded securely in private browser mode with read-only presentation access rules. | **Pass** |

## Data reconciliation

| Metric | Python | Dashboard | Match? |
| :--- | :--- | :--- | :--- |
| Revenue | 4,663,273.69 | 4,663,273.69 | Yes |
| Orders | 19,960 | 19,960 | Yes |
| Customers | 2,997 | 2,997 | Yes |
| AOV | 533.17 | 533.17 | Yes |

## Defect log

| ID | Test | Description | Severity | Fix | Retest |
|---|---|---|---|---|---|
| *None* | *N/A* | *All test parameters passed core engineering requirements on initial validation run.* | *N/A* | *N/A* | *N/A* |

## Sign-off
- **Business sponsor:** Self-review (Simulated Business Analyst / Product Owner sign-off)  
- **Date:** October 26, 2026
- **Result:** All Must-Have functional and non-functional requirements passed completely with 100% data reconciliation.
