### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of rows and return a single value for each group of rows .
- Aggregate functions can be used in select lists, order by clauses, and having clauses.
- Aggregate functions are commonly used with the group by clause, which divides the rows of a table or view into groups based on one or more columns or expressions .
- The group by clause specifies the grouping columns and optionally the grouping sets, which are subsets of the grouping columns that define the level of aggregation.
- The group by clause can also include the rollup or cube operators, which generate subtotals and grand totals for the groups.
- The having clause is used to filter the groups based on a condition that involves an aggregate function .
- Some examples of aggregate functions are sum, count, min, max, avg, listagg, json_arrayagg, and json_objectagg  .
- Aggregate functions can be used as window functions, which perform calculations across a set of rows that are related to the current row.
- The syntax of using aggregate functions with group by clause in Oracle and MySQL is similar, except for some differences in the function names and options .
- Here is a generic example of using aggregate functions with group by clause in Oracle and MySQL:

```sql
-- Oracle
SELECT column1, column2, aggregate_function(column3) AS alias
FROM table
WHERE condition
GROUP BY column1, column2
HAVING aggregate_function(column3) operator value
ORDER BY column1, column2;

-- MySQL
SELECT column1, column2, aggregate_function(column3) AS alias
FROM table
WHERE condition
GROUP BY column1, column2
HAVING aggregate_function(column3) operator value
ORDER BY column1, column2;
```

- Here is a specific example of using aggregate functions with group by clause in Oracle and MySQL:

```sql
-- Oracle
SELECT department_id, COUNT(*) AS num_employees, AVG(salary) AS avg_salary
FROM employees
WHERE job_id LIKE '%MAN%'
GROUP BY department_id
HAVING AVG(salary) > 10000
ORDER BY department_id;

-- MySQL
SELECT department_id, COUNT(*) AS num_employees, AVG(salary) AS avg_salary
FROM employees
WHERE job_id LIKE '%MAN%'
GROUP BY department_id
HAVING AVG(salary) > 10000
ORDER BY department_id;
```