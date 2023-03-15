### Querying Data and User Defined Functions in Hadoop Eco System

1. **Querying Data:** Hadoop provides several tools for querying data stored in Hadoop Distributed File System (HDFS). These tools include Hive, Pig, and Impala.

2. **Hive:** Hive is a data warehousing and SQL-like query language for Hadoop. It allows users to write queries in a familiar SQL syntax and execute them on data stored in HDFS.

3. **Pig:** Pig is a high-level platform for creating MapReduce programs used with Hadoop. It includes a language called Pig Latin for expressing data analysis tasks.

4. **Impala:** Impala is a massively parallel processing (MPP) SQL query engine for Hadoop. It provides low latency and high concurrency for BI/analytic queries on Hadoop.

5. **User Defined Functions (UDFs):** UDFs allow users to write custom functions in languages such as Java, Python, or Scala and use them in their queries. UDFs can be used in Hive, Pig, and Impala to perform complex data transformations and analysis.

6. **Using UDFs in Hive:** To use a UDF in Hive, the user must first create a temporary or permanent function and register it with Hive. The function can then be used in HiveQL queries.

7. **Using UDFs in Pig:** To use a UDF in Pig, the user must first define the function in a script or register it using the `REGISTER` command. The function can then be used in Pig Latin scripts.

8. **Using UDFs in Impala:** To use a UDF in Impala, the user must first create the function and register it with Impala. The function can then be used in Impala SQL queries.
