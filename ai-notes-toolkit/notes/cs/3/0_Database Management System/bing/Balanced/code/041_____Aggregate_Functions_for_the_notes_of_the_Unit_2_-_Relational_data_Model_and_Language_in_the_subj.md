Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here are some notes on the topic of Aggregate Functions for the Unit 2 - Relational data Model and Language.

### Aggregate Functions
- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the GROUP BY clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:
  - COUNT: returns the number of values in a set or the number of rows that satisfy a condition.
  - SUM: returns the sum of all the values in a set or the sum of the values that satisfy a condition.
  - AVG: returns the average of all the values in a set or the average of the values that satisfy a condition.
  - MIN: returns the minimum value in a set or the minimum value that satisfies a condition.
  - MAX: returns the maximum value in a set or the maximum value that satisfies a condition.
- The syntax of an aggregate function is:

  ```sql
  aggregate_function(expression)
  ```

  where expression is a column name, a constant, or an arithmetic expression.
- For example, the following query returns the total number of employees, the total salary, the average salary, the minimum salary, and the maximum salary in the EMPLOYEE table:

  ```sql
  SELECT COUNT(*), SUM(Salary), AVG(Salary), MIN(Salary), MAX(Salary)
  FROM EMPLOYEE;
  ```
- The following query returns the number of employees and the average salary for each department in the EMPLOYEE table:

  ```sql
  SELECT DeptNo, COUNT(*), AVG(Salary)
  FROM EMPLOYEE
  GROUP BY DeptNo;
  ```
- Aggregate functions can also be used with the HAVING clause to filter the groups based on some condition. For example, the following query returns the number of employees and the average salary for each department that has more than 10 employees:

  ```sql
  SELECT DeptNo, COUNT(*), AVG(Salary)
  FROM EMPLOYEE
  GROUP BY DeptNo
  HAVING COUNT(*) > 10;
  ```
- Aggregate functions can also be used with the DISTINCT keyword to eliminate duplicate values before applying the function. For example, the following query returns the number of distinct departments in the EMPLOYEE table:

  ```sql
  SELECT COUNT(DISTINCT DeptNo)
  FROM EMPLOYEE;
  ```