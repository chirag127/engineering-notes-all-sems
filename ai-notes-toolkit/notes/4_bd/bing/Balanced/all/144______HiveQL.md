# HiveQL

HiveQL is a query language for Apache Hive, a data warehouse system for Apache Hadoop. HiveQL allows users to process and analyze structured data in a Metastore, which is a central repository of metadata. HiveQL separates users from the complexity of Map Reduce programming and reuses common concepts from relational databases, such as tables, rows, columns, and schema .

Some of the features of HiveQL are:

- It provides the basic SQL-like operations, such as SELECT, WHERE, GROUP BY, HAVING, ORDER BY, JOIN, etc.
- It supports built-in operators and functions for data operations, such as arithmetic, logical, comparison, string, date, etc.
- It allows users to define custom functions (UDFs), aggregations (UDAFs), and table-generating functions (UDTFs) in Java, Python, or other languages.
- It supports subqueries, views, partitions, buckets, indexes, and other advanced features for optimizing query performance.
- It supports storage on various file systems, such as HDFS, S3, ADLS, GS, etc.
- It supports different file formats, such as text, JSON, ORC, Parquet, Avro, etc.
- It supports different data types, such as primitive, complex, and user-defined.

HiveQL is similar to SQL, but it has some differences and limitations. For example, HiveQL does not support transactions, updates, deletes, or inserts on existing rows. HiveQL also does not support some SQL features, such as correlated subqueries, triggers, stored procedures, etc. HiveQL is designed for batch processing and analytics, not for real-time or interactive queries.