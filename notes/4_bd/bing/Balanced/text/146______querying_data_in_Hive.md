#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large datasets stored in Hadoop using a SQL-like language called Hive Query Language (HiveQL)  .
- HiveQL is a declarative language that converts queries into MapReduce programs, which are executed on the Hadoop cluster  .
- HiveQL supports various types of queries, such as:
  - Simple selects: to retrieve data from one or more tables or views, optionally with filters, aggregations, joins, and order by clauses .
  - Subqueries: to use the result of one query as the input of another query, either in the FROM, WHERE, or HAVING clauses .
  - Common table expressions (CTEs): to define temporary tables that can be referenced in the main query or other CTEs .
  - Window functions: to perform calculations over a set of rows that are related to the current row, such as rank, sum, or average .
  - Analytical functions: to perform complex statistical or mathematical operations on a group of rows, such as correlation, covariance, or linear regression .
- The basic syntax of a HiveQL query is:

```sql
SELECT [DISTINCT] column_list
FROM table_or_view [alias]
[WHERE condition]
[GROUP BY column_list [HAVING condition]]
[ORDER BY|SORT BY|CLUSTER BY|DISTRIBUTE BY column_list]
[LIMIT number];
```

- Some examples of HiveQL queries are:

```sql
-- Select all columns from the who table
SELECT * FROM who;

-- Select the name and age columns from the who table, where age is greater than 30
SELECT name, age FROM who WHERE age > 30;

-- Select the name and age columns from the who table, and sort them by age in descending order
SELECT name, age FROM who ORDER BY age DESC;

-- Select the name and average age of each country from the who table, and filter only the countries with average age above 40
SELECT country, AVG(age) AS avg_age
FROM who
GROUP BY country
HAVING avg_age > 40;

-- Select the name and rank of each person in the who table, based on their age within each country
SELECT name, RANK() OVER (PARTITION BY country ORDER BY age DESC) AS rank
FROM who;
```

: Querying in Hive - GitHub Pages
: Hive Query | Make the Most of Big Data Analytics with Apache Hive
: Intro to Hive Queries and How to Write Them Effectively - Pepperdata