-- MySQL Version
-- SELECT
--     CONCAT(YEAR(order_date), 'Q', QUARTER(order_date)) AS Quarter,
--     SUM(amount) AS TotalRevenue
-- FROM orders_prc
-- WHERE YEAR(order_date) IN (2022, 2023)
-- GROUP BY Quarter;

-- PostgreSQL Version
SELECT
    EXTRACT(YEAR FROM order_date)::text
        || 'Q' ||
    EXTRACT(QUARTER FROM order_date)::text AS quarter,
    SUM(amount) AS total_revenue
FROM
    orders_prc
WHERE
    EXTRACT(YEAR FROM order_date) IN (2022, 2023)
GROUP BY
    quarter
ORDER BY
    quarter;
