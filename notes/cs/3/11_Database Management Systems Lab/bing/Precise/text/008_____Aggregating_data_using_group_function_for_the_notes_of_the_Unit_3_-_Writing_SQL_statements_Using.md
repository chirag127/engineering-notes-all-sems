### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregating data refers to the process of summarizing and grouping data to extract useful information.
- The GROUP BY clause is used in a SELECT statement to group rows into a set of summary rows by values of columns or expressions.
- The GROUP BY clause returns one row for each group.
- The SELECT statement can include aggregate functions such as COUNT, SUM, AVG, MIN, and MAX to perform calculations on each group of rows.
- The HAVING clause is used to filter groups based on a specified condition.
- The GROUP BY clause can be used with the JOIN, WHERE, and HAVING clauses to further filter and manipulate the data.
- The GROUP BY clause can be used with the ROLLUP, CUBE, and GROUPING SETS operators to produce subtotal and grand total values.
- The GROUP BY clause can be used with the ORDER BY clause to sort the grouped rows.

Example:
```sql
SELECT department_id, COUNT(*) 
FROM employees 
GROUP BY department_id 
HAVING COUNT(*) > 5 
ORDER BY department_id;
```
This query returns the department_id and the number of employees in each department where the number of employees is greater than 5, grouped by department_id and ordered by department_id.