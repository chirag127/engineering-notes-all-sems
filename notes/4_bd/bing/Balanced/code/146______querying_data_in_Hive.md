#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large datasets stored in Hadoop using a SQL-like language called Hive Query Language (HiveQL)   .
- HiveQL is a declarative language that converts queries into MapReduce, Tez, or Spark programs that run on the Hadoop cluster .
- HiveQL supports most of the standard SQL features, such as select, join, group by, order by, subqueries, functions, and operators .
- HiveQL also provides some extensions, such as partitioning, bucketing, windowing, and user-defined functions .
- To query data in Hive, users need to create tables or views that map to the underlying data files in Hadoop  .
- Hive supports two types of tables: external and managed (or internal)  .
- External tables are used to reference data that is already present in Hadoop and is not managed by Hive  .
- Managed tables are used to store data that is loaded or inserted by Hive and is managed by Hive  .
- Hive also supports two types of views: regular and materialized .
- Regular views are logical views that do not store any data, but only the query definition .
- Materialized views are physical views that store the query results in a table and can be refreshed periodically .
- To query data in Hive, users need to use the SELECT statement, which has the following syntax :

```sql
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list [HAVING having_condition]]
[ORDER BY col_list [ASC | DESC]]
[LIMIT number]
```

- The SELECT statement can be used to query data from one or more tables or views, apply filters, aggregations, sorting, and limiting .
- The SELECT statement can also be used to create new tables or views from existing ones using the CREATE TABLE AS SELECT (CTAS) or CREATE VIEW AS SELECT (CVAS) syntax .
- Hive also provides some built-in functions and operators that can be used in the SELECT statement to perform various operations on the data, such as arithmetic, string, date, conditional, and analytical functions .
- Hive also allows users to create and use their own custom functions, called user-defined functions (UDFs), user-defined aggregate functions (UDAFs), and user-defined table-generating functions (UDTFs) .
- To query the metadata of Hive tables and views, such as the schema, partitions, properties, and statistics, users can use the DESCRIBE, SHOW, and ANALYZE commands .