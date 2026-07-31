#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large datasets stored in Hadoop using a SQL-like language called HiveQL  .
- HiveQL is a declarative language that converts queries into MapReduce programs, which are executed on the Hadoop cluster.
- HiveQL supports most of the standard SQL features, such as select, join, group by, order by, etc., as well as some extensions, such as partitioning, bucketing, windowing, etc.
- To query data in Hive, users need to create tables or views that map to the underlying data files in HDFS or other storage systems  .
- The basic syntax of a HiveQL query is:

```sql
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list]
[HAVING having_condition]
[CLUSTER BY col_list | [DISTRIBUTE BY col_list] [SORT BY col_list]]
[LIMIT number]
```

- Some examples of HiveQL queries are:

```sql
-- Select all columns from a table
SELECT * FROM employees;

-- Select specific columns from a table
SELECT name, salary, department FROM employees;

-- Select distinct values from a column
SELECT DISTINCT department FROM employees;

-- Filter rows based on a condition
SELECT * FROM employees WHERE salary > 50000;

-- Join two tables on a common column
SELECT e.name, e.salary, d.location
FROM employees e
JOIN departments d
ON e.department = d.name;

-- Aggregate data using group by and having clauses
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING avg_salary > 60000;

-- Partition data by a column and sort within each partition
SELECT * FROM employees
CLUSTER BY department;

-- Limit the number of rows returned
SELECT * FROM employees
LIMIT 10;
```

- To query the metadata of Hive tables and views, such as column names, data types, comments, etc., users can use the DESCRIBE or SHOW commands. For example:

```sql
-- Describe the schema of a table or view
DESCRIBE employees;

-- Show the partitions of a table
SHOW PARTITIONS employees;

-- Show the tables or views in a database
SHOW TABLES;

-- Show the databases in Hive
SHOW DATABASES;
```

- To learn more about HiveQL, users can refer to the official documentation or some online tutorials .