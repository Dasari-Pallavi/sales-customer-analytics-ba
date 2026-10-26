# Scrum Lifecycle Sprint Notes & Retrospective Logs

## Sprint 1: Foundation (Planned Story Points: 13)
* **Status:** Deployed and Closed successfully.
* **Velocity Metrics:** **13 Story Points Completed** (100% target alignment).
* **Sprint Review:** Successfully demoed an automated Python data preprocessing ETL pipeline that reads raw transactions, resolves day/month mixed-date anomalies, and outputs clean analytics files. Deployed the initial core financial summary KPIs page in Google Looker Studio.
* **Retrospective Summary:**
  * *What went well:* Establishing explicit validation rules and schema thresholds upfront prevented logic exceptions during initial dataset ingestion loops.
  * *What did not go well:* The initial front-end Looker Studio Customer scorecard double-counted consumers due to daily transactional grain duplication constraints.
  * *Process Improvements:* Swapped the scorecard data source layout directly over to the customer-unique RFM file matrix block to enforce a clean `Count Distinct` parameter check.

## Sprint 2: Insights & Release (Planned Story Points: 20)
* **Status:** Deployed and Closed successfully.
* **Velocity Metrics:** **20 Story Points Completed** (100% target alignment).
* **Sprint Review:** Demoed advanced analytical dashboard modules including dynamic top product performance tables with optional unit sales metrics toggles, global choropleth transaction maps, and an automated RFM behavioral segmentation distribution graph suite. Filed full offline PDF records and public viewing share filters.
* **Retrospective Summary:**
  * *What went well:* Creating clear task flows within our project tracking framework speeded up layout construction on pages 2, 3, and 4.
  * *What did not go well:* Running an isolated developer sprint model forced a cliff-drop graphic trend rather than standard daily scrum diagonal charts due to bulk end-of-cycle tracking task movement.
  * *Process Improvements:* Added dedicated solo project documentation notes into our workspace log to clarify tracking strategies to stakeholders.
