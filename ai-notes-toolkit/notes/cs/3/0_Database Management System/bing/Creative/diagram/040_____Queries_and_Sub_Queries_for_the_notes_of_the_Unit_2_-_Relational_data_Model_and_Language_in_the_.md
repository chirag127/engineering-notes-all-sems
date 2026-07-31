Hello, I am Sydney, your AI assistant. I can help you with your queries and subqueries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here is some content that you can use for your study material:

### Queries and Sub Queries

- A query is a request for information from a database that follows a specific syntax and format.
- A subquery is a query that is nested inside another query, usually within the WHERE or HAVING clause.
- Subqueries can be used to perform complex operations, such as filtering, aggregation, or computation, on the data returned by the main query.
- Subqueries can be classified into three types: scalar, row, and table subqueries.
- A scalar subquery returns a single value that can be used in a comparison or arithmetic expression.
- A row subquery returns a single row of values that can be compared with another row using the row comparison operators.
- A table subquery returns a table of values that can be used as a source of data for the main query or another subquery.

#### Examples of Queries and Sub Queries

- The following query returns the name and salary of the employee with the highest salary in the company:

```sql
SELECT name, salary
FROM employee
WHERE salary = (SELECT MAX(salary) FROM employee);
```

- The subquery in the WHERE clause is a scalar subquery that returns the maximum salary value from the employee table.
- The main query compares the salary of each employee with the value returned by the subquery and selects the matching rows.

- The following query returns the name and department of the employees who work in the same department as John:

```sql
SELECT name, department
FROM employee
WHERE (department, manager) IN (SELECT department, manager FROM employee WHERE name = 'John');
```

- The subquery in the WHERE clause is a row subquery that returns the department and manager of John from the employee table.
- The main query compares the department and manager of each employee with the row returned by the subquery and selects the matching rows.

- The following query returns the name and salary of the employees who earn more than the average salary of their department:

```sql
SELECT name, salary
FROM employee e
WHERE salary > (SELECT AVG(salary) FROM employee WHERE department = e.department);
```

- The subquery in the WHERE clause is a table subquery that returns the average salary of each department from the employee table.
- The main query joins the employee table with the subquery table on the department column and compares the salary of each employee with the average salary of their department and selects the matching rows.