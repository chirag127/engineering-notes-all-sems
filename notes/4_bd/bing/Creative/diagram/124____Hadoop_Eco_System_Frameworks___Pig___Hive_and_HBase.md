## Hadoop Eco System Frameworks , Pig , Hive and HBase

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. It consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce. HDFS is a distributed file system that provides high-throughput access to data stored on multiple nodes. MapReduce is a programming model and an execution engine for parallel processing of data on HDFS.

Hadoop also includes several additional modules that provide additional functionality, such as :

- **Pig**: A high-level platform for creating MapReduce programs using a scripting language called Pig Latin. Pig allows users to write complex data transformations without having to write low-level Java code. Pig also provides a number of built-in functions and operators for common tasks such as filtering, joining, grouping, sorting, and aggregating data.
- **Hive**: A data warehouse infrastructure that provides data summarization and ad-hoc querying using a SQL-like query language called HiveQL. Hive enables users to perform analytical queries on structured and semi-structured data stored on HDFS. Hive also supports user-defined functions and custom data types.
- **HBase**: A scalable, distributed database that supports structured data storage for large tables. HBase is a column-oriented database that provides random read and write access to data on HDFS. HBase is suitable for applications that require low-latency and real-time access to large volumes of data. HBase also supports transactions, secondary indexes, and coprocessors for custom logic execution.

The following diagram shows the relationship between Hadoop and its ecosystem components :

![Hadoop Ecosystem](https://media.geeksforgeeks.org/wp-content/uploads/20191009174932/Hadoop-Ecosystem.png)

: https://www.geeksforgeeks.org/hadoop-an-introduction/
: https://stackoverflow.com/questions/13911501/when-to-use-hadoop-hbase-hive-and-pig
: https://www.geeksforgeeks.org/hadoop-ecosystem/
: https://webpages.charlotte.edu/aatzache/ITCS6190/PowerPoints/Hadoop/S_Pig_Hive_HBase_Zookeeper.pptx