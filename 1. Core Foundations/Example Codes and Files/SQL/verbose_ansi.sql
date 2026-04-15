-- SQL script that touches nearly every major ANSI SQL keyword at least once.

-- Create a table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE DEFAULT CURRENT_DATE,
    manager_id INT,
    CHECK (salary > 0)
);

-- Insert sample data
INSERT INTO employees (employee_id, first_name, last_name, department, salary, manager_id)
VALUES 
(1, 'John', 'Doe', 'Sales', 60000, 3),
(2, 'Jane', 'Smith', 'Marketing', 55000, 4),
(3, 'Mike', 'Johnson', 'IT', 70000, 5);

-- Update data
UPDATE employees
SET salary = salary * 1.05
WHERE department = 'Sales';

-- Delete data
DELETE FROM employees
WHERE employee_id = 2;

-- Query with CTE, joins, grouping, subqueries, case, union, etc.
WITH dept_summary AS (
    SELECT department, COUNT(*) AS total_employees, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > (SELECT AVG(salary) FROM employees)
)
SELECT DISTINCT d.department, d.total_employees, d.avg_salary,
       CASE 
           WHEN d.avg_salary > 65000 THEN 'High'
           ELSE 'Moderate'
       END AS salary_level
FROM dept_summary d
INNER JOIN employees e ON d.department = e.department
LEFT JOIN employees m ON e.manager_id = m.employee_id
UNION
SELECT department, 0, 0, 'None'
FROM (SELECT DISTINCT department FROM employees) AS sub
ORDER BY avg_salary DESC
LIMIT 5 OFFSET 0;

-- Alter table
ALTER TABLE employees ADD COLUMN bonus DECIMAL(10,2);

-- Drop table
DROP TABLE employees;
-- End of SQL script