### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A **query** is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A **subquery** is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregations.
- There are three types of subqueries: scalar, multirow, and correlated.
  - A **scalar subquery** returns a single value that can be used in an expression or a comparison. For example, the following query uses a scalar subquery to find the average salary of all employees:

  ```sql
  SELECT AVG(salary) FROM employees;
  ```

  - A **multirow subquery** returns one or more rows that can be used with operators such as IN, ANY, ALL, or EXISTS. For example, the following query uses a multirow subquery to find the employees who work in the same department as John Smith:

  ```sql
  SELECT name, department FROM employees
  WHERE department IN
  (SELECT department FROM employees
  WHERE name = 'John Smith');
  ```

  - A **correlated subquery** is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query. For example, the following query uses a correlated subquery to find the employees who earn more than the average salary of their department:

  ```sql
  SELECT name, salary, department FROM employees e1
  WHERE salary >
  (SELECT AVG(salary) FROM employees e2
  WHERE e1.department = e2.department);
  ```

- Subqueries can be used in different clauses of a query, such as the WHERE, FROM/JOIN, or SELECT clause. For example, the following query uses a subquery in the FROM clause to join two tables:

  ```sql
  SELECT e.name, e.salary, d.name AS department
  FROM employees e
  JOIN
  (SELECT department_id, name FROM departments) d
  ON e.department = d.department_id;
  ```

- Subqueries can also be nested inside other subqueries, as long as the nesting level does not exceed the limit imposed by the database system. For example, the following query uses a nested subquery to find the employees who work in the same department as the highest-paid employee:

  ```sql
  SELECT name, salary, department FROM employees
  WHERE department =
  (SELECT department FROM employees
  WHERE salary =
  (SELECT MAX(salary) FROM employees));
  ```

- Subqueries are usually contrasted with Common Table Expressions (CTEs) as they have similar use cases. CTEs are temporary named result sets that can be referenced within a query. CTEs can improve the readability and maintainability of complex queries, and can also enable recursive queries. For example, the following query uses a CTE to find the employees who work in the same department as John Smith:

  ```sql
  WITH dept AS
  (SELECT department FROM employees
  WHERE name = 'John Smith')
  SELECT name, department FROM employees
  WHERE department IN dept;
  ```