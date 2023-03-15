#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large datasets stored in Hadoop using a SQL-like language called HiveQL  .
- HiveQL is a declarative language that is converted into MapReduce programs by Hive. It can also leverage other execution engines such as Tez, Tez LLAP, and Spark.
- HiveQL supports various types of queries, such as simple selects, joins, aggregations, subqueries, window functions, and user-defined functions.
- The basic syntax of a HiveQL query is:

```sql
SELECT column_names
FROM table_name
[WHERE condition]
[GROUP BY column_names]
[HAVING condition]
[ORDER BY column_names]
[LIMIT number];
```

- Some examples of HiveQL queries are:

```sql
-- Select all columns from the who table and limit the output to 12 rows
SELECT * FROM who LIMIT 12;

-- Select the name and age columns from the employee table and order them by age in descending order
SELECT name, age FROM employee ORDER BY age DESC;

-- Select the average salary of employees grouped by department and filter out the departments with less than 10 employees
SELECT dept, AVG(salary) AS avg_salary
FROM employee
GROUP BY dept
HAVING COUNT(*) >= 10;
```

- Hive also provides a way to query the metadata of tables and views using the DESCRIBE and SHOW commands. For example:

```sql
-- Describe the schema of the employee table
DESCRIBE employee;

-- Show all the tables in the default database
SHOW TABLES;

-- Show the views that reference the employee table
SHOW VIEWS 'employee';
```

- Querying and data analysis using Hive is easier and faster than doing the same using the MapReduce framework, even when dealing with large datasets. Hive also supports various file formats, compression methods, and storage handlers.