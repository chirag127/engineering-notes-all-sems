Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. It consists of several components, such as HDFS (Hadoop Distributed File System), MapReduce (a programming model for parallel processing), and YARN (a resource management platform).

Hadoop also includes several additional modules that provide additional functionality, such as:

- Pig: a high-level platform for creating MapReduce programs using a scripting language called Pig Latin.
- Hive: a data warehouse infrastructure that provides data summarization and ad-hoc querying using a SQL-like query language called HiveQL.
- HBase: a non-relational, distributed database that supports structured data storage for large tables.
- Zookeeper: a service for coordinating and managing distributed systems.

The following diagram illustrates the basic architecture of a Hadoop ecosystem, including Pig, Hive, and HBase:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     Client      |      |     Client      |      |     Client      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     HDFS        |      |     HBase       |      |     Zookeeper   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     YARN        |      |     Hive        |      |     Pig         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     MapReduce   |      |     MapReduce   |      |     MapReduce   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```