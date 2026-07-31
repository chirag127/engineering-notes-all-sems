Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of aggregate functions for the unit 2 - relational data model and language in the subject of database management system.

### Aggregate Functions
- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:
  - `COUNT`: returns the number of values in a set or the number of rows in a table.
  - `SUM`: returns the sum of all numeric values in a set.
  - `AVG`: returns the average of all numeric values in a set.
  - `MIN`: returns the minimum value in a set.
  - `MAX`: returns the maximum value in a set.
- Aggregate functions can be applied to any column or expression that is compatible with the function, except for `COUNT(*)`, which can be applied to any table or subquery.
- Aggregate functions ignore null values, except for `COUNT(*)`, which counts all rows regardless of null values.
- Aggregate functions can be used in the `SELECT` clause, the `HAVING` clause, and the `ORDER BY` clause of a query.
- Aggregate functions can be combined with other expressions using arithmetic operators, such as `SUM(salary) / COUNT(*)` to calculate the average salary.
- Aggregate functions can be nested within each other, such as `MAX(AVG(salary))` to find the maximum average salary among different groups.
- Aggregate functions can be modified by the keywords `DISTINCT` and `ALL` to specify whether to consider only distinct values or all values in a set, such as `COUNT(DISTINCT name)` to count the number of distinct names. The default is `ALL`.
- Aggregate functions can be used with the `OVER` clause to apply the function to a window of rows defined by a partition and an order, such as `SUM(salary) OVER (PARTITION BY department ORDER BY hire_date)` to calculate the cumulative sum of salaries within each department. This is called a window function.