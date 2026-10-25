import pandas as pd

RAW = "data/raw/online_retail_II.csv"
df = pd.read_csv(RAW, encoding="latin1", parse_dates=["InvoiceDate"])
df = df.rename(columns={"Customer ID": "CustomerID"})
print("Raw rows:", len(df))

# 1. Remove exact duplicates
df = df.drop_duplicates()

# 2. Flag cancellations (Invoice starts with 'C')
df["Invoice"] = df["Invoice"].astype(str)
df["IsCancelled"] = df["Invoice"].str.startswith("C")

# 3. Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# 4. Valid sales = not cancelled, positive quantity and price
sales = df[(~df.IsCancelled) & (df.Quantity > 0) & (df.Price > 0)].copy()
sales["Month"] = sales["InvoiceDate"].dt.to_period("M").dt.to_timestamp()
sales["Date"] = sales["InvoiceDate"].dt.date
cancels = df[df.IsCancelled].copy()
print("Valid sales rows:", len(sales), "| cancelled rows:", len(cancels))

# 5. Aggregated tables for the dashboard (small files)
daily = (sales.groupby(["Date", "Country"])
         .agg(Revenue=("Revenue", "sum"), Orders=("Invoice", "nunique"),
              Customers=("CustomerID", "nunique"), Units=("Quantity", "sum"))
         .reset_index())

products = (sales.groupby(["StockCode", "Description"])
            .agg(Revenue=("Revenue", "sum"), Units=("Quantity", "sum"))
            .reset_index().sort_values("Revenue", ascending=False))

cancel_prod = (cancels.groupby(["StockCode", "Description"])
               .agg(CancelledUnits=("Quantity", lambda x: -x.sum()))
               .reset_index())

# 6. RFM segmentation (customers with an ID only)
known = sales.dropna(subset=["CustomerID"])
snapshot = known["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm = (known.groupby("CustomerID")
       .agg(Recency=("InvoiceDate", lambda x: (snapshot - x.max()).days),
            Frequency=("Invoice", "nunique"),
            Monetary=("Revenue", "sum")).reset_index())
rfm["R"] = pd.qcut(rfm["Recency"].rank(method="first"), 4, labels=[4, 3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm["Frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
rfm["M"] = pd.qcut(rfm["Monetary"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
rfm["Score"] = rfm["R"] + rfm["F"] + rfm["M"]

def segment(r):
    if r.Score >= 11: return "Champions"
    if r.Score >= 9:  return "Loyal"
    if r.Score >= 6:  return "Potential"
    if r.R <= 2 and r.F >= 3: return "At Risk"
    return "Lost"
rfm["Segment"] = rfm.apply(segment, axis=1)

# 7. Save outputs
out = "data/processed/"
daily.to_csv(out + "daily_sales.csv", index=False)
products.head(500).to_csv(out + "products.csv", index=False)
cancel_prod.to_csv(out + "cancelled_products.csv", index=False)
rfm.to_csv(out + "rfm_segments.csv", index=False)

# 8. Quick KPIs for the README and UAT reconciliation
print("Revenue:", round(sales.Revenue.sum(), 2))
print("Orders:", sales.Invoice.nunique(), "| Customers:", known.CustomerID.nunique())
print("AOV:", round(sales.Revenue.sum() / sales.Invoice.nunique(), 2))
print("Cancel rate (invoices):", round(cancels.Invoice.nunique() / df.Invoice.nunique() * 100, 2), "%")
