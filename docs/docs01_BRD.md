\# Business Requirements Document (BRD)

\*\*Project:\*\* Sales \& Customer Analytics Dashboard

\*\*Version:\*\* 1.0 | \*\*Author:\*\* <your name> | \*\*Status:\*\* Approved



\## 1. Executive Summary

The retailer needs a self-service dashboard replacing manual Excel reporting,

giving visibility into revenue, products, geography and customer value.



\## 2. Business Objectives (SMART)

\- BO1: Reduce weekly report preparation time from \~6 hrs to <30 min by Sprint 2.

\- BO2: Identify top 20% customers (RFM) to support retention campaigns.

\- BO3: Provide monthly revenue trend with MoM growth by <date>.



\## 3. Scope

\*\*In scope:\*\* Data cleaning, KPI dashboard, product/country analysis, RFM segmentation, cancellation/returns analysis.

\*\*Out of scope:\*\* Real-time data, forecasting model, inventory system integration.



\## 4. Stakeholders

| Role | Name | Interest |

|---|---|---|

| Sponsor | Head of Sales | Revenue growth |

| Marketing Manager | - | Customer segments |

| Operations Manager | - | Returns, product performance |

| Data Analyst/Developer | - | Build |

| BA (me) | - | Requirements, UAT |



\## 5. Functional Requirements

| ID | Requirement | Priority (MoSCoW) |

|---|---|---|

| FR-01 | Dashboard shall show total revenue, orders, customers, AOV | Must |

| FR-02 | Show monthly revenue trend with date filter | Must |

| FR-03 | Show top 10 products by revenue and quantity | Must |

| FR-04 | Show revenue by country (map/table) | Should |

| FR-05 | Segment customers by RFM and show segment counts/revenue | Must |

| FR-06 | Show cancellation/return rate | Should |

| FR-07 | Allow filter by country, date, segment | Must |



\## 6. Non-Functional Requirements

\- NFR-01: Dashboard loads in < 5 seconds.

\- NFR-02: Data refreshed monthly (manual upload acceptable).

\- NFR-03: Access via shareable link, view-only for business users.

\- NFR-04: Customer IDs are anonymised; no personal data displayed.



\## 7. Assumptions \& Constraints

\- Dataset is a static historical extract (2009–2011).

\- Free tools only (Jira Free, Looker Studio).



\## 8. Risks

| Risk | Impact | Mitigation |

|---|---|---|

| \~20% rows lack Customer ID | Customer metrics incomplete | Exclude from RFM, document |

| Cancellations distort revenue | Wrong KPIs | Separate cancelled invoices |



\## 9. Success Criteria / Sign-off

All Must requirements pass UAT; stakeholder sign-off recorded.

