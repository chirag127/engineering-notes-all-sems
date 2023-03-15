### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative or imperative language, depending on the data model and query language used.
- A subquery is a query that is nested inside another query, usually in the WHERE, FROM/JOIN, or SELECT clause. A subquery can return a single value, a row, a column, or a table, depending on how it is used.
- Subqueries are often used when you need to process data in several steps, or when you need to compare values from different tables or sources.
- Subqueries can be classified into three types: scalar, multirow, and correlated.
  - A scalar subquery is a subquery that returns a single value. It can be used anywhere a literal value can be used, such as in a comparison, arithmetic expression, or function argument.
  - A multirow subquery is a subquery that returns one or more rows. It can be used with operators such as IN, ANY, ALL, or EXISTS, to test for membership, comparison, or existence of values.
  - A correlated subquery is a subquery that references one or more columns from the outer query. It is executed once for each row of the outer query, and the result depends on the values of the outer query row.
- Subqueries can be alternatively formulated as joins in some cases, but not in others. Joins are used to combine data from two or more tables based on a common attribute or condition. Joins can be inner, outer, cross, or self, depending on how the tables are matched.
- Some examples of queries and subqueries in SQL are:

```sql
-- A query that returns the name and salary of employees who work in the Sales department
SELECT name, salary
FROM employee
WHERE department = 'Sales';

-- A subquery that returns the average salary of employees who work in the Sales department
SELECT AVG(salary)
FROM employee
WHERE department = 'Sales';

-- A query that uses a scalar subquery to return the name and salary of employees who earn more than the average salary of the Sales department
SELECT name, salary
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee WHERE department = 'Sales');

-- A query that uses a multirow subquery to return the name and salary of employees who work in the same department as John Smith
SELECT name, salary
FROM employee
WHERE department IN (SELECT department FROM employee WHERE name = 'John Smith');

-- A query that uses a correlated subquery to return the name and salary of employees who earn more than the average salary of their department
SELECT name, salary
FROM employee e1
WHERE salary > (SELECT AVG(salary) FROM employee e2 WHERE e1.department = e2.department);

-- A query that uses a join to return the name and salary of employees and the name and location of their department
SELECT e.name, e.salary, d.name, d.location
FROM employee e
JOIN department d
ON e.department = d.name;
```