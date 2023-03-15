#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large datasets stored in Hadoop using a SQL-like language called Hive Query Language (HiveQL)  .
- HiveQL is a declarative language that converts queries into MapReduce programs, which are executed on the Hadoop cluster  .
- HiveQL supports many features of SQL, such as select, join, group by, order by, and aggregate functions, as well as some extensions, such as partitioning, bucketing, and windowing functions .
- The basic way to query data in Hive is using the SELECT statement, which has the following syntax:

```sql
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list]
[HAVING having_condition]
[ORDER BY col_list]
[LIMIT number]
```

- The SELECT statement can be used to query data from one or more tables, views, or partitions, and apply various filters, transformations, and aggregations on the data .
- The table_reference can be a table name, a view name, a subquery, or a join expression .
- The where_condition can be any logical expression that evaluates to true or false, and can use operators such as =, <, >, IN, BETWEEN, LIKE, and AND, OR, and NOT .
- The GROUP BY clause can be used to group the rows by one or more columns, and apply aggregate functions such as SUM, COUNT, AVG, MIN, MAX, etc. on the grouped data .
- The HAVING clause can be used to filter the groups based on a condition that involves aggregate functions .
- The ORDER BY clause can be used to sort the rows by one or more columns, in ascending or descending order .
- The LIMIT clause can be used to limit the number of rows returned by the query .

- Here is an example of a simple SELECT query that returns the first 12 rows from a table called who:

```sql
SELECT * FROM who LIMIT 12;
```

- Here is another example of a SELECT query that returns the total population and average life expectancy of each continent from a table called world, grouped by continent and ordered by population in descending order:

```sql
SELECT continent, SUM(population) AS total_population, AVG(life_expectancy) AS avg_life_expectancy
FROM world
GROUP BY continent
ORDER BY total_population DESC;
```

- For more information and examples of querying data in Hive, please refer to the following sources:

: https://mmas.github.io/querying-hive
: https://www.analyticsvidhya.com/blog/2020/12/15-basic-and-highly-used-hive-queries-that-all-data-engineers-must-know/
: https://www.pepperdata.com/blog/hive-queries-writing-effectively
: https://stackoverflow.com/questions/51090906/querying-hive-metadata