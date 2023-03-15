# Querying Data and User Defined Functions in Hadoop

- Querying data in Hadoop is the process of retrieving and analyzing data stored in HDFS using various tools and frameworks.
- One of the most popular tools for querying data in Hadoop is **Hive**, which is a data warehouse framework that provides a SQL-like dialect called **HiveQL** for summarizing and querying large data sets on Hadoop .
- HiveQL supports many features of SQL, such as joins, group by, order by, subqueries, etc. It also allows users to create, alter, and drop tables, databases, views, or user-defined functions.
- User-defined functions (UDFs) are custom functions that can be written in any programming language and plugged into Hive queries using the **TRANSFORM** clause.
- UDFs can be used to perform complex calculations, transformations, or validations on column values during a Hive query.
- UDFs can be written using two different interfaces: **Simple API** and **Complex API**.
- The Simple API (org.apache.hadoop.hive.ql.exec.UDF) can be used when the UDF reads and returns primitive types, such as basic Hadoop and Hive writable types.
- The Complex API (org.apache.hadoop.hive.ql.udf.generic.GenericUDF) can be used when the UDF reads and returns complex types, such as arrays, maps, structs, etc.
- To use a UDF in a Hive query, the user needs to export the UDF code to a JAR file, copy the JAR file to HDFS, and register the UDF with Hive using the **CREATE FUNCTION** statement.
- The registered UDF can then be invoked in a Hive query using the function name and the required arguments.