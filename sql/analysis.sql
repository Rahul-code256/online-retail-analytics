
-- 1. Total revenue
SELECT ROUND(SUM(Revenue), 2) AS total_revenue
FROM retail;

-- 2. Revenue by country
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS revenue
FROM retail
GROUP BY Country
ORDER BY revenue DESC;

-- 3. Top 10 products by revenue
SELECT
    Description,
    ROUND(SUM(Revenue), 2) AS revenue
FROM retail
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;

-- 4. Monthly revenue
SELECT
    strftime('%Y-%m', InvoiceDate) AS month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM retail
GROUP BY month
ORDER BY month;

-- 5. Average order value
SELECT ROUND(
    SUM(Revenue) / COUNT(DISTINCT InvoiceNo), 2
) AS average_order_value
FROM retail;

-- 6. Top 10 customers by spending
SELECT
    CustomerID,
    ROUND(SUM(Revenue), 2) AS total_spending
FROM retail
GROUP BY CustomerID
ORDER BY total_spending DESC
LIMIT 10;

-- 7. Best-selling products by units
SELECT
    Description,
    SUM(Quantity) AS units_sold
FROM retail
GROUP BY Description
ORDER BY units_sold DESC
LIMIT 10;

-- 8. Revenue by country and month
SELECT
    Country,
    strftime('%Y-%m', InvoiceDate) AS month,
    ROUND(SUM(Revenue), 2) AS revenue
FROM retail
GROUP BY Country, month
ORDER BY Country, month;
