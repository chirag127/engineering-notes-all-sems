# Queries and Subqueries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A **query** is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language, such as SQL, which specifies the desired result without describing how to compute it.
- A **subquery** is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar (a single value), a single row, a single column, or a table (one or more rows of one or more columns).
- Subqueries are often used when you need to process data in several steps. For the majority of subqueries you’ll see in actual practice, the inner query will execute first and pass its result to the outer query it's nested in. Subqueries are usually contrasted with Common Table Expressions (CTEs) as they have similar use cases.
- Subqueries can be used in different clauses of a query, such as:
  - **WHERE clause**: A subquery in the WHERE clause can be used to filter the rows returned by the outer query based on the values returned by the subquery. For example, the following query returns the names of the employees who have a salary higher than the average salary of all employees:

  ```sql
  SELECT name
  FROM employees
  WHERE salary > (SELECT AVG(salary) FROM employees);
  ```

  - **FROM clause**: A subquery in the FROM clause can be used to create a temporary table that can be joined with other tables in the outer query. For example, the following query returns the names and departments of the employees who work in the same department as John:

  ```sql
  SELECT e.name, e.department
  FROM employees e
  JOIN (SELECT department FROM employees WHERE name = 'John') d
  ON e.department = d.department;
  ```

  - **SELECT clause**: A subquery in the SELECT clause can be used to return a scalar value for each row returned by the outer query. For example, the following query returns the name, salary, and rank of each employee, where the rank is the number of employees who have a higher salary than the current employee:

  ```sql
  SELECT name, salary, (SELECT COUNT(*) FROM employees e2 WHERE e2.salary > e1.salary) AS rank
  FROM employees e1;
  ```

- Subqueries can also be classified into two types based on their dependency on the outer query:
  - **Correlated subquery**: A subquery that references one or more columns from the outer query in its WHERE clause. A correlated subquery cannot be executed independently, and it is re-evaluated for each row returned by the outer query. For example, the following query returns the names of the employees who have the highest salary in their department:

  ```sql
  SELECT name
  FROM employees e1
  WHERE salary = (SELECT MAX(salary) FROM employees e2 WHERE e2.department = e1.department);
  ```

  - **Non-correlated subquery**: A subquery that does not reference any column from the outer query. A non-correlated subquery can be executed independently, and it is evaluated only once for the entire outer query. For example, the following query returns the names of the employees who have a salary higher than 5000:

  ```sql
  SELECT name
  FROM employees
  WHERE salary > (SELECT 5000);
  ```

- A **relational data model** is a data model that represents data as a collection of tables, where each table consists of rows and columns. Each row represents an entity or a record, and each column represents an attribute or a field of the entity. A relational data model also defines constraints and relationships among the tables, such as primary keys, foreign keys, and referential integrity.
- A **relational query language** is a language that allows users to manipulate and query data stored in a relational database. A relational query language can be either procedural or declarative. A procedural query language requires the user to specify the steps or algorithms to retrieve the desired data, while a declarative query language requires the user to specify the desired result without describing how to compute it.
- The most widely used relational query language is **SQL (Structured Query Language)**, which is a declarative language that consists of several commands