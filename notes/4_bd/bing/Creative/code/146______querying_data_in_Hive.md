#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large-scale data using a SQL-like language called HiveQL.
- HiveQL is a declarative language that abstracts the complexity of MapReduce, the underlying framework for distributed data processing in Hadoop.
- Hive supports various data formats, such as text, JSON, ORC, Parquet, Avro, etc., and can access data stored in HDFS, HBase, or other external sources.
- Hive provides a schema-on-read approach, which means that the data schema is inferred at the time of query execution, rather than at the time of data ingestion.
- Hive allows users to create tables, partitions, buckets, views, indexes, and functions to organize and manipulate data.
- Hive also supports user-defined functions (UDFs), user-defined aggregate functions (UDAFs), and user-defined table functions (UDTFs) to extend the functionality of HiveQL.
- To query data in Hive, users need to use the Hive shell, the Hive web interface (HWI), or the HiveServer2 (HS2) service, which provides a JDBC/ODBC interface for external applications.
- A typical Hive query consists of the following components:
  - A SELECT clause that specifies the columns or expressions to be returned.
  - A FROM clause that specifies the table or view to be queried, optionally with aliases, joins, or subqueries.
  - A WHERE clause that specifies the filtering conditions for the rows to be returned.
  - A GROUP BY clause that specifies the grouping criteria for the rows to be aggregated.
  - A HAVING clause that specifies the filtering conditions for the groups to be returned.
  - An ORDER BY clause that specifies the sorting order for the rows to be returned.
  - A LIMIT clause that specifies the maximum number of rows to be returned.
- Hive also supports various clauses and keywords to modify the query behavior, such as DISTINCT, OVER, LATERAL VIEW, WINDOW, CLUSTER BY, DISTRIBUTE BY, SORT BY, etc.
- Hive also supports various built-in functions and operators to perform calculations, transformations, and comparisons on the data, such as arithmetic, string, date, conditional, collection, etc.
- Hive also supports various commands and statements to perform administrative and metadata operations, such as CREATE, ALTER, DROP, SHOW, DESCRIBE, etc.