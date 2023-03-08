 Here is the content in markdown format for the topic #### sorting and aggregating in Hive:

#### Sorting and Aggregating in Hive

- Hive queries can be ordered using `ORDER BY` clause. This clause is used to sort the data in ascending or descending order.
- `ORDER BY` clause can be used with `SELECT` and `CREATE TABLE AS SELECT` queries.
- The column specified in the `ORDER BY` clause must be present in the select list.
- Sorting is done on the data once the query is executed i.e. after the map-reduce job is completed.
- Aggregation is performed using aggregate functions like `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` etc.
- These functions operate on a set of values and return a single value.
- `GROUP BY` clause is used along with aggregate functions to group the rows by one or more columns.
- `GROUP BY` clause must contain at least one column that is not an aggregate function.
- The columns in the `SELECT` list must be either aggregate function or must be present in the `GROUP BY` list.
- Example:
```
SELECT
    department,
    SUM(salary)
FROM
    employees
GROUP BY
    department;
```
This query will sum up the salaries for each department.
- Advantages: Sorting and aggregation reduces the number of rows which decreases the size of data to be processed and analyzed. This improves the performance of queries.
- Disadvantages: If the table is very large and sorting or aggregation is being done on multiple columns then it can negatively impact the performance due to excessive Map-Reduce jobs.
- Applications: Sorting and aggregating is used in data analysis for trend analysis, finding averages, identifying maximum and minimum values etc. It is a very commonly used operation in data processing.