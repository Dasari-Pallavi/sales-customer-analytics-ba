# Data Dictionary

**Source:** Online Retail II (UCI / Kaggle)
**Period:** 01 Dec 2009 - 09 Dec 2011
**Grain:** One row = one product line on one invoice

## Raw fields
| Field | Type | Description | Cleaning rule |
|---|---|---|---|
| Invoice | Text | Invoice number, 6 digits. Starts with "C" if cancelled | Starting with "C" flags a cancellation |
| StockCode | Text | Product code | Keep as text |
| Description | Text | Product name | Missing values left as is; trimmed for display |
| Quantity | Integer | Units per line. Negative for cancellations | Sales require Quantity > 0 |
| InvoiceDate | Datetime | Date and time of the invoice | Parsed as datetime |
| Price | Decimal | Unit price in GBP | Sales require Price > 0 |
| Customer ID | Number | 5-digit customer identifier | About 20% are blank; excluded from customer metrics only |
| Country | Text | Customer's country | No change |

## Derived fields (created in `src/clean_and_model.py`)
| Field | Type | Formula | Purpose |
|---|---|---|---|
| CustomerID | Number | Renamed from "Customer ID" | Avoids a space in the column name |
| IsCancelled | Boolean | Invoice starts with "C" | Separates returns from sales |
| Revenue | Decimal | Quantity x Price | Core sales metric |
| Month | Date | First day of invoice month | Monthly trend |
| Date | Date | Date part of InvoiceDate | Daily aggregation |
| Recency | Integer | Days from last purchase to snapshot date | RFM |
| Frequency | Integer | Distinct invoices per customer | RFM |
| Monetary | Decimal | Total revenue per customer | RFM |
| R, F, M | Integer 1-4 | Quartile score of each measure (4 = best) | RFM scoring |
| Score | Integer 3-12 | R + F + M | Segment rule |
| Segment | Text | Champions / Loyal / Potential / At Risk / Lost | Marketing action |

## KPI definitions
| KPI | Definition |
|---|---|
| Total Revenue | Sum of Revenue for valid sales (not cancelled, Qty > 0, Price > 0) |
| Orders | Count of distinct valid Invoice numbers |
| Customers | Count of distinct CustomerID in valid sales |
| AOV | Total Revenue / Orders |
| Cancellation rate | Distinct cancelled invoices / all distinct invoices |

## Segment rules
| Segment | Rule |
|---|---|
| Champions | Score 11-12 |
| Loyal | Score 9-10 |
| Potential | Score 6-8 |
| At Risk | Score below 6, R <= 2 and F >= 3 |
| Lost | Everything else |

## Known data quality issues
1. About 20% of rows have no Customer ID (guest checkouts).
2. Duplicate rows exist and are removed.
3. Some rows have non-product stock codes (postage, adjustments).
4. Data is historical, not real-time.
