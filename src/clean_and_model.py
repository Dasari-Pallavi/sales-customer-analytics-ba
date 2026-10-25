import os
import pandas as pd
import numpy as np

def run_pipeline():
    print("Initializing Data Engineering Pipeline...")
    
    # ----------------------------------------------------
    # STEP 1: STABLE CSV INGESTION ENGINE
    # ----------------------------------------------------
    RAW = "data/raw/online_retail_II.csv"
    
    if not os.path.exists(RAW):
        if os.path.exists("data/raw/Online Retail II UCI.csv"):
            RAW = "data/raw/Online Retail II UCI.csv"
        elif os.path.exists("data/raw/online_retail_II.CSV"):
            RAW = "data/raw/online_retail_II.CSV"
        else:
            raise FileNotFoundError(f"Source file not found. Please check that your dataset is placed in data/raw/ and named online_retail_II.csv")
        
    print(f"Reading transaction database from: {RAW}")
    df = pd.read_csv(RAW, encoding="latin1")
    
    raw_count = len(df)
    print(f"Raw rows loaded: {raw_count}")
    
    # ----------------------------------------------------
    # STEP 2: DATA CLEANING & RECONCILIATION PREPARATION
    # ----------------------------------------------------
    if "UnitPrice" in df.columns and "Price" not in df.columns:
        df = df.rename(columns={"UnitPrice": "Price"})
    if "CustomerID" in df.columns and "Customer ID" not in df.columns:
        df = df.rename(columns={"CustomerID": "Customer ID"})
        
    # FIXED: Added format='mixed' to handle changing day/month text sequences
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='mixed')
    df['Invoice'] = df['Invoice'].astype(str)
    df['Customer ID'] = pd.to_numeric(df['Customer ID'], errors='coerce')
    
    # Isolate valid sales entries separate from cancellations
    cancelled_mask = df['Invoice'].str.startswith('C', na=False) | (df['Quantity'] < 0)
    df_cancelled = df[cancelled_mask].copy()
    df_sales = df[~cancelled_mask].copy()
    
    # Drop rows missing critical numeric or category elements
    df_sales = df_sales.dropna(subset=['Customer ID', 'Price'])
    df_sales = df_sales[df_sales['Price'] > 0]
    df_sales = df_sales[df_sales['Quantity'] > 0]
    
    # Calculate transaction metrics
    df_sales['Revenue'] = df_sales['Quantity'] * df_sales['Price']
    
    # ----------------------------------------------------
    # STEP 3: EXPORT AGGREGATED REPORTING FILE EXTRACTS
    # ----------------------------------------------------
    os.makedirs("data/processed", exist_ok=True)
    
    # 1. daily_sales.csv
    daily_sales = df_sales.groupby(['InvoiceDate', 'Country']).agg(
        Revenue=('Revenue', 'sum'),
        Orders=('Invoice', 'nunique'),
        Customers=('Customer ID', 'nunique'),
        Units=('Quantity', 'sum')
    ).reset_index()
    daily_sales.to_csv("data/processed/daily_sales.csv", index=False)
    
    # 2. products.csv
    products = df_sales.groupby(['StockCode', 'Description']).agg(
        Revenue=('Revenue', 'sum'),
        Units_Sold=('Quantity', 'sum')
    ).reset_index().sort_values(by='Revenue', ascending=False)
    products.to_csv("data/processed/products.csv", index=False)
    
    # 3. cancelled_products.csv
    df_cancelled['Return_Value'] = df_cancelled['Quantity'].abs() * df_cancelled['Price']
    cancelled_products = df_cancelled.groupby(['StockCode', 'Description']).agg(
        Returned_Units=('Quantity', lambda x: x.abs().sum()),
        Lost_Revenue=('Return_Value', 'sum')
    ).reset_index().sort_values(by='Lost_Revenue', ascending=False)
    cancelled_products.to_csv("data/processed/cancelled_products.csv", index=False)
    
    # ----------------------------------------------------
    # STEP 4: AUTOMATED RFM LOYALTY COHORT SCORING ENGINE
    # ----------------------------------------------------
    snapshot_date = df_sales['InvoiceDate'].max() + pd.Timedelta(days=1)
    
    rfm = df_sales.groupby('Customer ID').agg(
        Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
        Frequency=('Invoice', 'nunique'),
        Monetary=('Revenue', 'sum')
    ).reset_index()
    
    # Generate distribution quartile ranking scores
    r_labels = [4, 3, 2, 1]
    f_labels = [1, 2, 3, 4]
    m_labels = [1, 2, 3, 4]
    
    rfm['R'] = pd.qcut(rfm['Recency'], q=4, labels=r_labels, duplicates='drop')
    rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=f_labels)
    rfm['M'] = pd.qcut(rfm['Monetary'], q=4, labels=m_labels)
    
    # Calculate unified segment indicators
    rfm['RFM_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)
    
    # Segment structural classification lookup map
    def assign_segment(row):
        score = row['RFM_Score']
        if score in ['444', '443', '434', '344']: return 'Champions'
        elif score.startswith('4') or '4' in score: return 'Loyal Customers'
        elif score.startswith('2') or '2' in score: return 'At Risk'
        elif score.startswith('1'): return 'Lost'
        else: return 'Potential Loyalists'
        
    rfm['Segment'] = rfm.apply(assign_segment, axis=1)
    
    # Clean column naming convention to map seamlessly with Looker Studio
    rfm = rfm.rename(columns={'Customer ID': 'CustomerID'})
    rfm.to_csv("data/processed/rfm_segments.csv", index=False)
    
    # ----------------------------------------------------
    # STEP 5: OUTPUT UAT CONSOLE METRICS LOG
    # ----------------------------------------------------
    total_revenue = df_sales['Revenue'].sum()
    total_orders = df_sales['Invoice'].nunique()
    total_customers = df_sales['Customer ID'].nunique()
    aov = total_revenue / total_orders
    
    total_invoices_raw = df['Invoice'].nunique()
    cancelled_invoices_raw = df_cancelled['Invoice'].nunique()
    cancel_rate = (cancelled_invoices_raw / total_invoices_raw) * 100
    
    print("\n==============================================")
    print("     DATA ENGINE PIPELINE RUN SUCCESSFUL      ")
    print("==============================================")
    print(f"Raw rows processed: {raw_count}")
    print(f"Valid sales rows: {len(df_sales)} | Cancelled rows: {len(df_cancelled)}")
    print(f"Revenue: {total_revenue:.1f}")
    print(f"Orders: {total_orders} | Customers: {total_customers}")
    print(f"AOV: {aov:.2f}")
    print(f"Cancel rate (invoices): {cancel_rate:.2f} %")
    print("==============================================\n")

if __name__ == "__main__":
    run_pipeline()
