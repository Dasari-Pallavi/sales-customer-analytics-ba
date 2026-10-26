-- ====================================================================
-- BUSINESS INTELLIGENCE COMPLIANCE & RECONCILIATION QUERY LIBRARY
-- ====================================================================

-- 1. Monthly Revenue Seasonality & Velocity Log
-- Purpose: Aggregates historical transaction revenues into chronological monthly clusters
SELECT 
    DATE_TRUNC('month', InvoiceDate) AS purchase_month, 
    SUM(Quantity * Price) AS monthly_revenue,
    COUNT(DISTINCT Invoice) AS transaction_volume
FROM sales 
WHERE Quantity > 0 AND Price > 0
GROUP BY 1 
ORDER BY 1 ASC;

-- 2. Top 10 Product Inventory Revenue Matrices
-- Purpose: Isolates top-performing products by cumulative gross spend value parameters
SELECT 
    Description AS product_name, 
    StockCode AS stock_identifier,
    SUM(Quantity * Price) AS aggregate_revenue,
    SUM(Quantity) AS total_units_dispatched
FROM sales 
WHERE Quantity > 0 AND Price > 0
GROUP BY 1, 2 
ORDER BY aggregate_revenue DESC 
LIMIT 10;

-- 3. Global Regional Sales Concentration Breakdown
-- Purpose: Tracks total net value generation mapped across international market borders
SELECT 
    Country AS market_region, 
    SUM(Quantity * Price) AS total_market_revenue,
    COUNT(DISTINCT "Customer ID") AS identified_buyer_base
FROM sales 
WHERE Quantity > 0 AND Price > 0
GROUP BY 1 
ORDER BY total_market_revenue DESC;
