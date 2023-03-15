## Hadoop Eco System Frameworks , Pig , Hive and HBase

- Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers using simple programming models.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce.
- HDFS is a distributed file system that provides high-throughput access to data stored on multiple nodes in a cluster.
- MapReduce is a programming model and an execution engine for parallel processing of large data sets using key-value pairs.
- Hadoop also includes several additional modules that provide additional functionality, such as Hive, Pig, and HBase  .

### Pig

- Pig is a high-level platform for creating MapReduce programs using a data flow language called Pig Latin .
- Pig Latin is a simple but powerful language that supports common data operations, such as load, filter, join, group, and store.
- Pig Latin scripts are compiled into MapReduce jobs and executed on the Hadoop cluster .
- Pig can handle structured, semi-structured, and unstructured data, and can integrate with other Hadoop components, such as HDFS, HBase, and Hive .
- Pig is suitable for data analysis tasks that require complex transformations, custom functions, and iterative processing .

### Hive

- Hive is a data warehouse infrastructure that provides data summarization and ad-hoc querying using a SQL-like query language called HiveQL  .
- HiveQL queries are translated into MapReduce jobs and executed on the Hadoop cluster  .
- Hive can handle structured and semi-structured data, and can integrate with other Hadoop components, such as HDFS, HBase, and Pig  .
- Hive is suitable for data analysis tasks that require aggregation, filtering, and projection of large data sets using a familiar SQL syntax  .

### HBase

- HBase is a scalable, distributed database that supports structured data storage for large tables  .
- HBase is based on the Google Bigtable model, and provides random, real-time read/write access to data in HDFS  .
- HBase can handle structured and semi-structured data, and can integrate with other Hadoop components, such as HDFS, MapReduce, and Hive  .
- HBase is suitable for data analysis tasks that require low-latency, high-throughput access to large volumes of data with dynamic schema  .