-- with clause syntax in SQL
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)


-- Window functions syntax in SQL

SELECT column1, column2, 
       ROW_NUMBER() OVER (ORDER BY column1) AS row_num,
       RANK() OVER (ORDER BY column1) AS rank_num
FROM table_name;

