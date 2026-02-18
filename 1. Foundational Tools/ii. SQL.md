# SQL (PostgreSQL)
Documentation on SQL

**[⇐ Foundational Tools](./README.md)**

## Case
```SQL
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2 ...        
    ELSE default_result    
END AS alias
```

## Date & Time

* Current Date: `CURRENT_DATE`
* Current Time: `CURRENT_TIME`
* Current Date and Time: `CURRENT_TIMESTAMP`

* Date Difference
    ```SQL
    '2025-08-15'::date - '2025-08-09'::date
    ```

* Add interval to a date
    ```SQL
    '2025-08-09'::date + INTERVAL '10 days'
    ```

* Subtract interval from a date
    ```SQL
    '2025-08-09'::date - INTERVAL '5 days'
    ```

* Format Date
    ```SQL
    TO_CHAR(order_date, 'YYYY/MM/DD');
    TO_CHAR(order_date, 'Month DD, YYYY');
    TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS');
    ```
    - Year options: YYYY, YY
    - Month options: MM, Mon, Month
    - Date: DD
    - Day: Day
    - Hour: HH24
    - Minutes: MI
    - Seconds: SS

* Extract
    ```SQL
        EXTRACT(FIELD FROM source)
    ```
    - FIELDS: YEAR, MONTH, DAY, DAYOFWEEK, HOUR, MINUTE, SECOND
    - source: date, time

## Functions
* `CONCAT(string1, string2, ...)` or   `string1 || string2`
* `CAST(expression AS target_data_type)` or `x::type`
* `LENGTH(string_expression)` for characters `CHAR_LENGTH()`
* `SUBSTRING(string_expression, start_position, length)` or `SUBSTR()`

* `POSITION(substring IN string_expression)`
* `SPLIT_PART(str, delim, field_number)`
* `TRIM()`, `LTRIM()`, `RTRIM()`
* `LEFT()`, `RIGHT()`, `UPPER()`, `LOWER()`

* `COALESCE(expression1, expression2, ...)`: Applies available one among multiple expressions

* WITH Statement - Common Table Expressions (CTE)
    ```SQL
    WITH alias AS (
        SELECT statement
    )
    SELECT statement FROM alias;
    ```

    * WITH RECURSIVE Statement
    ```SQL
    WITH RECURSIVE numbers AS (
        -- Anchor member (starting point)
        SELECT 1 AS n
        UNION ALL
        -- Recursive member (keeps adding rows)
        SELECT n + 1 FROM numbers WHERE n < 10
    )
    SELECT * FROM numbers;
    ```

* * **Window Function** *
    ```SQL
    function_name() OVER (
        PARTITION BY partition_expression
        ORDER BY order_expression
        ROWS/RANGE frame_specification
    )
    ```

    * Row Number
        ```SQL
        ROW_NUMBER() OVER (ORDER BY created_at) AS rn
        ```

    * Aggregate Functions

        * Moving Average
            ```SQL
            AVG(revenue) OVER (
                ORDER BY date ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
            ) AS moving_avg
            ```
    * Ranking Functions
        * Rank
            ```SQL
            RANK() OVER (ORDER BY score DESC) AS rank
            ``` 

    * Analytical Functions
        * Lead: Next value of an ordered column
            ```SQL
            LEAD(sales) OVER (ORDER BY date) AS next_day_sales
            ```

        * Lag: Previous value of an ordered column
            ```SQL
            LAG(sales) OVER (ORDER BY date) AS previous_day_sales
            ```

* * **CTEs** (Common Table Expressions) *

CTEs make code readable and modular.


* * **Query Optimization** *