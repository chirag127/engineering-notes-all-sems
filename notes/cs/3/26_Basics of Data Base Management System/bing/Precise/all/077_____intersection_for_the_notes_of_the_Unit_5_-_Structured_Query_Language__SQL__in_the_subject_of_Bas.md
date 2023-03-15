# Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

### Intersection

- The `INTERSECT` operator in SQL is used to combine two `SELECT` statements, but returns rows only from the first `SELECT` statement that are identical to a row in the second `SELECT` statement.
- The `INTERSECT` operator returns only distinct rows that are common to both queries.
- The number and the order of the columns must be the same in both `SELECT` statements, and the data types must be compatible.
- The basic syntax of the `INTERSECT` operator is as follows:
```
SELECT column1, column2, ...
FROM table1
INTERSECT
SELECT column1, column2, ...
FROM table2;
```
- Here is an example that uses the `INTERSECT` operator to return the common rows between two tables:
```
SELECT employee_id, employee_name
FROM employees
INTERSECT
SELECT employee_id, employee_name
FROM managers;
```
- This statement returns the `employee_id` and `employee_name` of all employees who are also managers.
- The `INTERSECT` operator can be combined with other operators such as `ORDER BY` to sort the result set.
- The `INTERSECT` operator is not supported by all database systems. In some systems, the same result can be achieved using an `INNER JOIN` or a subquery with the `IN` operator.