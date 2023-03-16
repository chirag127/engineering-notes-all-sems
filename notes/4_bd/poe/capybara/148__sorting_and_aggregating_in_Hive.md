#### Sorting and Aggregating in Hive

Hive is a data warehousing tool that enables the processing of large data sets using SQL-like queries. Sorting and aggregating are essential functions when working with big datasets in Hive. Here are some key points to keep in mind when performing sorting and aggregating in Hive:

##### Sorting in Hive
- Sorting can be done in ascending or descending order.
- The `ORDER BY` clause is used to sort data in Hive.
- The `SORT BY` clause is used to sort the data within a specific partition.
- Sorting can be done on multiple columns using a comma-separated list.
- Hive uses a distributed sorting technique to sort large datasets. 

##### Aggregating in Hive
- Aggregating is the process of summarizing large datasets into a smaller form.
- Hive provides various built-in aggregate functions such as `SUM`, `AVG`, `MIN`, `MAX`, and `COUNT`.
- The `GROUP BY` clause is used to group the data based on one or more columns.
- The `HAVING` clause is used to filter the groups based on aggregate functions.
- Hive supports rollup, cube, and grouping sets which are extensions to the `GROUP BY` clause.

##### Examples
Sorting example:
```sql
SELECT name, age FROM employees ORDER BY age DESC;
```

Aggregating example:
```sql
SELECT department, COUNT(*) as count FROM employees GROUP BY department HAVING count > 10;
```

Rollup example:
```sql
SELECT department, gender, SUM(salary) as total_salary FROM employees GROUP BY department, gender WITH ROLLUP;
```

By keeping these points in mind, you can efficiently sort and aggregate large datasets in Hive.