-- Question:
-- Find customers who placed orders in at least two consecutive years and had more than one order in at least one of those years.

-- Tables: customers_prc

-- ColumnName		Datatype
-- customerid 		INT
-- name 			VARCHAR
-- age 			INT
-- city 			VARCHAR

-- Table: orders_prc

-- ColumnName		Datatype
-- order_id 		INT
-- customer_id     INT
-- order_date 		DATE
-- amount 			INT

WITH orders_by_year AS (
  SELECT customer_id, YEAR(order_date) AS order_year, COUNT(*) AS order_count
  FROM orders_prc
  GROUP BY customer_id, YEAR(order_date)
),
has_consecutive_years AS (
  SELECT o1.customer_id
  FROM orders_by_year o1
  JOIN orders_by_year o2
    ON o1.customer_id = o2.customer_id
    AND o1.order_year = o2.order_year - 1
),
has_multi_order_year AS (
  SELECT DISTINCT customer_id
  FROM orders_by_year
  WHERE order_count > 1
)
SELECT name
FROM customers_prc
WHERE customerid IN (
  SELECT customer_id
  FROM has_consecutive_years
  INTERSECT
  SELECT customer_id
  FROM has_multi_order_year
);