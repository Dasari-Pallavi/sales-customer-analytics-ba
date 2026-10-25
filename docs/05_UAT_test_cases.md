# UAT Test Cases

**Tester:** <your name>  |  **Date:** <date>  |  **Environment:** Looker Studio (view link)

| TC | Req | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-01 | FR-01 | Open dashboard page 1 | 4 cards show Revenue, Orders, Customers, AOV; values match Python output | | |
| TC-02 | FR-02 | Set date filter Jan-Mar 2011 | Line chart and cards update to the range | | |
| TC-03 | FR-03 | Open page 2, view top 10 products | 10 products, sorted high to low | | |
| TC-04 | FR-04 | View revenue by country | UK is largest; all countries listed | | |
| TC-05 | FR-05 | Open page 3 | Segment customer counts sum to total known customers | | |
| TC-06 | FR-06 | Open page 4 | Cancelled units by product shown; rate displayed | | |
| TC-07 | FR-07 | Apply a country filter | All charts update | | |
| TC-08 | NFR-01 | Open report on a normal connection | Loads in under 5 seconds | | |
| TC-09 | NFR-03 | Open link in a private browser window | Report visible, not editable | | |

## Data reconciliation
| Metric | Python script | Dashboard | Match? |
|---|---|---|---|
| Total revenue | | | |
| Orders | | | |
| Customers | | | |
| AOV | | | |

## Defect log
| ID | Test | Description | Severity | Fix | Retest |
|---|---|---|---|---|---|
| | | | | | |

## Sign-off
- Business sponsor: ______  Date: ______
- Result: All Must requirements passed / Pending fixes
