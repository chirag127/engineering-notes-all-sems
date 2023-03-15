### Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - `AVG`: returns the average of all values in a set or the average of values that satisfy a condition.
  - `MIN`: returns the minimum value in a set or the minimum value that satisfies a condition.
  - `MAX`: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the `SELECT` clause, the `HAVING` clause, or the `ORDER BY` clause of a query.
- Aggregate functions ignore `NULL` values in the set of values they operate on, unless otherwise specified by the `ALL` or `DISTINCT` modifiers.
- Examples of aggregate functions:

  - `SELECT COUNT(*) FROM student;` returns the number of rows in the `student` table.
  - `SELECT AVG(marks) FROM student WHERE grade = 'A';` returns the average marks of students who have grade A.
  - `SELECT MIN(salary), MAX(salary) FROM employee GROUP BY department;` returns the minimum and maximum salary for each department.
  - `SELECT department, SUM(salary) AS total_salary FROM employee GROUP BY department HAVING SUM(salary) > 100000;` returns the department and the total salary for each department that has a total salary greater than 100000.
  - `SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 1;` returns the name and salary of the employee with the highest salary.