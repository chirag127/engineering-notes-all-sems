### Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set.
  - `AVG`: returns the average of all values in a set.
  - `MIN`: returns the minimum value in a set.
  - `MAX`: returns the maximum value in a set.

- Aggregate functions can be used in the `SELECT` clause or the `HAVING` clause of a query.
- Aggregate functions ignore `NULL` values in the set, unless otherwise specified.
- Aggregate functions can be combined with other expressions using arithmetic operators, such as `+`, `-`, `*`, `/`, etc.
- Aggregate functions can also be nested within each other, such as `AVG(SUM(salary))`.
- Some examples of queries using aggregate functions are:

  - To find the total number of employees in each department:

    ```sql
    SELECT dept_id, COUNT(*)
    FROM employee
    GROUP BY dept_id;
    ```

  - To find the average salary of employees in each department:

    ```sql
    SELECT dept_id, AVG(salary)
    FROM employee
    GROUP BY dept_id;
    ```

  - To find the highest salary among all employees:

    ```sql
    SELECT MAX(salary)
    FROM employee;
    ```

  - To find the number of employees who earn more than the average salary:

    ```sql
    SELECT COUNT(*)
    FROM employee
    WHERE salary > (SELECT AVG(salary) FROM employee);
    ```