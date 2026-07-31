Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of aggregate functions for the unit 2 - relational data model and language in the subject of database management system.

# Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the GROUP BY clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - COUNT: returns the number of values in a set or the number of rows that satisfy a condition.
  - SUM: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - AVG: returns the average of all values in a set or the average of values that satisfy a condition.
  - MIN: returns the minimum value in a set or the minimum value that satisfies a condition.
  - MAX: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the SELECT clause, the HAVING clause, or the ORDER BY clause of a query.
- Aggregate functions ignore NULL values in the set of values they operate on, unless otherwise specified by the function.
- Aggregate functions can be nested, meaning that one aggregate function can be used as an argument for another aggregate function.
- Examples of aggregate functions in SQL:

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

  - To find the highest salary among the employees who have a bonus:

    ```sql
    SELECT MAX(salary)
    FROM employee
    WHERE bonus IS NOT NULL;
    ```

  - To find the number of distinct job titles in the employee table:

    ```sql
    SELECT COUNT(DISTINCT job_title)
    FROM employee;
    ```