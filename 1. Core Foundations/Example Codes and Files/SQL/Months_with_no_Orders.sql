-- Question:
-- Identify the months in 2023 with no orders and provide a list of these months.

-- Table: orders_prc

-- ColumnName		Datatype
-- order_id 		INT
-- customer_id      INT
-- order_date 		DATE
-- amount 			INT


WITH RECURSIVE months AS (
    SELECT
        DATE('2023-01-01') AS d
    UNION ALL
        SELECT
            DATE_ADD(d, INTERVAL 1 MONTH)
        FROM
            months
        WHERE
            d < '2023-12-01'
)
SELECT
    DATE_FORMAT(d, '%Y-%m') AS MissingMonth
FROM
    months
LEFT JOIN
    orders_prc o
        ON
            DATE_FORMAT(d, '%Y-%m') = DATE_FORMAT(order_date, '%Y-%m')
WHERE
    o.order_id IS NULL;