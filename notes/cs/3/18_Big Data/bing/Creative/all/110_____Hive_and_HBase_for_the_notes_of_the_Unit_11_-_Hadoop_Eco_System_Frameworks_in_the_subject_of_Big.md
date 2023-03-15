# Hive and HBase

Hive and HBase are two Hadoop-based technologies that serve different purposes. Here are some points to compare and contrast them:

- **Data Model**: Hive uses a SQL-like language called HiveQL to process structured data stored in Hadoop Distributed File System (HDFS). HBase, on the other hand, is a NoSQL database that stores unstructured or semi-structured data in a column-family data model.
- **Processing**: Hive provides a batch processing framework that enables users to write queries using HiveQL and execute them as MapReduce jobs on HDFS. HBase provides a real-time processing framework that enables users to perform CRUD (create, read, update, delete) operations on large datasets using Java API, REST API, or Thrift API.
- **Schema**: Hive has a schema-on-read approach, which means that the schema of the data is inferred at the time of query execution. HBase has a schema-on-write approach, which means that the schema of the data is defined at the time of data insertion.
- **Querying**: Hive supports complex queries and ad hoc analysis using HiveQL, which is similar to SQL. HBase supports simple queries and real-time analysis using filters, scanners, and coprocessors.
- **Data Size**: Hive is suitable for processing large volumes of data (terabytes or petabytes) that are not frequently updated. HBase is suitable for processing large volumes of data (gigabytes or terabytes) that are frequently updated.

: https://www.geeksforgeeks.org/difference-between-hive-and-hbase/
: https://intellipaat.com/blog/hive-vs-hbase/