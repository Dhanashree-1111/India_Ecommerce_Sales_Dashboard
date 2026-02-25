-- 1. Total Revenue and Profit by Category
-- This query verifies the main bar chart in our dashboard
SELECT 
    Category, 
    SUM(Amount) AS Total_Revenue, 
    SUM(Profit) AS Total_Profit
FROM Cleaned_Ecommerce_Data
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 2. Performance by State
-- This query identifies which regions are most profitable
SELECT 
    State, 
    SUM(Amount) AS Total_Sales,
    AVG(Profit_Margin) AS Average_Margin
FROM Cleaned_Ecommerce_Data
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 10;