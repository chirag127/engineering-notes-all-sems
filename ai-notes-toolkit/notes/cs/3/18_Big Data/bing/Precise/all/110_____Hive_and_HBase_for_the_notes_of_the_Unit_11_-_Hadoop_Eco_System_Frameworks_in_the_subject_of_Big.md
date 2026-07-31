# Hive and HBase

Hive and HBase are both Apache Hadoop-based technologies, but they have different use cases and characteristics.

1. **Data Model:** Hive uses a SQL-like language called HiveQL to process structured data stored in Hadoop Distributed File System (HDFS).
2. **Processing:** Hive provides a batch processing framework that enables users to write queries using HiveQL, which are then translated into MapReduce jobs and executed on Hadoop. HBase, on the other hand, is designed for real-time processing of big data and supports random read and write operations.
3. **Hive and Hadoop on AWS:** Amazon Elastic Map Reduce (EMR) is a managed service that lets you use big data processing frameworks such as Spark, Presto, Hbase, and, yes, Hadoop to analyze and process large data sets. Hive, in turn, runs on top of Hadoop clusters, and can be used to query data residing in Amazon EMR clusters, employing an SQL language.
4. **Hadoop:** Hadoop is an open-source framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Hive, a data warehouse software, provides an SQL-like interface to efficiently query and manipulate large data sets residing in various databases and file systems that integrate with Hadoop.
5. **Hive as a relational-database:** Hive is the closest thing to a relational-database in the Hadoop ecosystem. Pig is an application for transforming large data sets. Like Hive, Pig has its own SQL-Like language called Pig Latin. Where Hive is used for structured data, Pig excels in transforming semi-structured and unstructured data.
6. **Hive as a data warehouse system:** Hive is a data warehouse system for Hadoop that facilitates easy data summarization, ad-hoc queries, and the analysis of large datasets stored in Hadoop compatible file systems. It provides a mechanism to project structure onto this data and query the data using a SQL-like language called HiveQL.
