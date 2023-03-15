# Queries and Subqueries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregation.
- There are three main types of subqueries: scalar, multirow, and correlated.

## Scalar subqueries
- A scalar subquery is a subquery that returns a single value. It can be used anywhere a literal value can be used, such as in a SELECT list, a WHERE clause, a HAVING clause, or a SET clause.
- A scalar subquery must be enclosed in parentheses, and it must have only one column in the SELECT list.
- Example: The following query uses a scalar subquery to find the average salary of all employees in the company.

```sql
SELECT AVG(salary) AS avg_salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

## Multirow subqueries
- A multirow subquery is a subquery that returns one or more rows. It can be used with operators that compare a value to a set of values, such as IN, NOT IN, ANY, ALL, EXISTS, or NOT EXISTS.
- A multirow subquery must be enclosed in parentheses, and it can have one or more columns in the SELECT list.
- Example: The following query uses a multirow subquery to find the names of the employees who work in the same department as John Smith.

```sql
SELECT name
FROM employees
WHERE department_id IN (SELECT department_id FROM employees WHERE name = 'John Smith');
```

## Correlated subqueries
- A correlated subquery is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query, and it can reference columns from the outer query in its WHERE clause.
- A correlated subquery must be enclosed in parentheses, and it can have one or more columns in the SELECT list.
- Example: The following query uses a correlated subquery to find the names of the employees who earn more than the average salary of their department.

```sql
SELECT name, salary, department_id
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department_id = e2.department_id);
```