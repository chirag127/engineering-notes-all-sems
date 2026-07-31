### Writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- A SQL SELECT statement is used to retrieve data from one or more tables or views in a database.
- The basic syntax of a SQL SELECT statement is:

```sql
SELECT column_list
FROM table_list
WHERE condition_list
ORDER BY column_list
GROUP BY column_list
HAVING condition_list
LIMIT number;
```

- The SELECT clause specifies the columns or expressions to be displayed in the result set. It can also use aliases, functions, and aggregate functions.
- The FROM clause specifies the tables or views to be queried. It can also use joins, subqueries, and aliases.
- The WHERE clause specifies the conditions to filter the rows from the tables or views. It can use logical operators, comparison operators, and wildcards.
- The ORDER BY clause specifies the order of the rows in the result set. It can use ASC or DESC keywords to indicate ascending or descending order. It can also use column numbers or expressions.
- The GROUP BY clause specifies the grouping of the rows based on one or more columns or expressions. It is often used with aggregate functions to calculate summary statistics for each group.
- The HAVING clause specifies the conditions to filter the groups from the GROUP BY clause. It can use logical operators, comparison operators, and aggregate functions.
- The LIMIT clause specifies the maximum number of rows to be returned in the result set. It is often used for pagination or performance optimization.

- Some examples of SQL SELECT statements are:

```sql
-- Select all columns from the employees table
SELECT *
FROM employees;

-- Select the first name, last name, and salary of the employees who earn more than 5000
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 5000;

-- Select the department name and the average salary of the employees in each department, ordered by the average salary in descending order
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- Select the first name, last name, and job title of the employees who work as a clerk or a manager, and limit the result to 10 rows
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
JOIN jobs j
ON e.job_id = j.job_id
WHERE j.job_title IN ('Clerk', 'Manager')
LIMIT 10;
```