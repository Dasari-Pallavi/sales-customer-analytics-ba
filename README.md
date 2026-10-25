# Sales & Customer Analytics (RFM Segmentation)

A data analytics project that processes retail transaction history to evaluate core business health and segment customer behavior patterns using an automated RFM (Recency, Frequency, Monetary) matrix framework.

## Project Performance Snapshot (UAT Verified)
* **Total Cleaned Revenue:** £10,642,124.90
* **Unique Valid Orders:** 19,960 
* **Unique Identified Customers:** 2,997
* **Average Order Value (AOV):** £533.17
* **Invoice Cancellation Rate:** 14.81%

## Repository File Architecture
* `docs/` - Contains business requirement documentation (BRD).
* `src/` - Contains the Python ETL processing data pipeline script.
* `data/raw/` - Local workspace folder for the raw source transaction dataset.
* `data/processed/` - Target outputs generated for dashboard reporting.

## Setup & Local Execution Requirements
1. Clone this repository to your workspace.
2. Download the `online_retail_II.csv` dataset from Kaggle and place it inside the `data/raw/` directory.
3. Install dependencies and run the core script pipeline using your terminal:
   ```bash
   pip install pandas
   python src/clean_and_model.py
   ```
