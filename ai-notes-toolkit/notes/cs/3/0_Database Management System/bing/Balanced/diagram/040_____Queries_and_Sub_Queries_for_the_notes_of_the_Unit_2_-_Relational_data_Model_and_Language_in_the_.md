### Queries and Subqueries for the notes of the Unit 2 - Relational Data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data to retrieve, but not how to retrieve it.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to compare values from different tables or sources. Subqueries can also be used to create temporary tables or views that can be joined with other tables .
- There are three main types of subqueries: scalar, multirow, and correlated. Each type has different rules and restrictions on how it can be used in the outer query.
  - A scalar subquery returns a single value that can be used in the SELECT, WHERE, or HAVING clause of the outer query. For example, the following query uses a scalar subquery to find the average salary of all employees:

  ```sql
  SELECT AVG(salary) AS avg_salary
  FROM employees;
  ```

  - A multirow subquery returns one or more rows that can be used in the WHERE or HAVING clause of the outer query with comparison operators such as IN, ANY, or ALL. For example, the following query uses a multirow subquery to find the employees who work in the same department as John Smith:

  ```sql
  SELECT name, department
  FROM employees
  WHERE department IN (SELECT department
                       FROM employees
                       WHERE name = 'John Smith');
  ```

  - A correlated subquery is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query. A correlated subquery can be used in the SELECT, WHERE, or HAVING clause of the outer query with comparison operators such as =, <, >, etc. For example, the following query uses a correlated subquery to find the employees who earn more than the average salary of their department:

  ```sql
  SELECT name, salary, department
  FROM employees e1
  WHERE salary > (SELECT AVG(salary)
                  FROM employees e2
                  WHERE e1.department = e2.department);
  ```

- The relational data model is a way of representing data as a collection of tables, where each table consists of rows and columns. Each row represents an entity or an instance of a relation, and each column represents an attribute or a property of the entity. The relational data model is based on the principles of mathematical logic and set theory.
- The relational data model has several advantages, such as:
  - Easy to use: The tables consisting of rows and columns are quite natural and simple to understand.
  - Query capability: It makes possible for a high-level query language like SQL to avoid complex database navigation.
  - Data independence: The structure of the relational database can be changed without having to change the application programs that access the data.
  - Data integrity: The data can be enforced by using constraints such as primary keys, foreign keys, and check constraints.
  - Data security: The data can be protected by using access control mechanisms such as user authentication and authorization.