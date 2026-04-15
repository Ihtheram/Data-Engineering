-- Question:
-- Calculate the percentage increase in total sales from the previous year to the current year using the orders_prc table.

-- ColumnName		Datatype

-- order_id 		  INT
-- customer_id    INT
-- order_date 	  DATE
-- amount 		    INT

WITH YearlySales AS (
  SELECT
      YEAR(order_date) Year,
      SUM(amount) `Yearly Sales`,
      COALESCE(
        LAG(SUM(amount)) OVER (ORDER BY YEAR(order_date)), 0
      ) `Past Year's Sales`
  FROM orders_prc o
  GROUP BY
      Year
)
SELECT
    *,
    ROUND(
      COALESCE(
        ((`Yearly Sales` - `Past Year's Sales`)
            / `Past Year's Sales`) * 100, 0
      ), 2
    ) AS `Percentage Increase`
FROM
    YearlySales