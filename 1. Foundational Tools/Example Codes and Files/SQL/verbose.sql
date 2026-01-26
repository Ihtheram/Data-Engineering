-- An example SQL query that demonstrates all major SQL keywords at least once

WITH dept_summary AS (
    SELECT department, COUNT(employee_id) AS total_employees, AVG(salary) AS avg_salary
    FROM employees
    WHERE salary IS NOT NULL
    GROUP BY department
    HAVING AVG(salary) > (SELECT AVG(salary) FROM employees)
)
SELECT DISTINCT d.department, d.total_employees, d.avg_salary,
       CASE 
           WHEN d.avg_salary > 70000 THEN 'High'
           ELSE 'Moderate'
       END AS salary_level
FROM dept_summary d
INNER JOIN employees e ON d.department = e.department
LEFT JOIN managers m ON e.manager_id = m.manager_id
RIGHT JOIN locations l ON m.location_id = l.location_id
FULL OUTER JOIN benefits b ON e.employee_id = b.employee_id
UNION
SELECT department, 0 AS total_employees, 0 AS avg_salary, 'None' AS salary_level
FROM departments
EXCEPT
SELECT department, total_employees, avg_salary, salary_level
FROM dept_summary
ORDER BY avg_salary DESC
LIMIT 10 OFFSET 0;
