## Hadoop Eco System Frameworks , Pig , Hive and HBase

- Hadoop is an open-source framework that allows distributed processing of large-scale data sets across clusters of computers using simple programming models.
- Hadoop consists of four main components: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce, and Hadoop YARN.
- Hadoop Common provides the common utilities and libraries that support other Hadoop modules.
- HDFS is a distributed file system that stores data across multiple nodes in a cluster, providing high availability, fault tolerance, and scalability.
- MapReduce is a programming model and an execution engine for processing large-scale data sets in parallel using key-value pairs.
- YARN is a resource management layer that allocates and schedules resources for applications running on top of Hadoop.
- Hadoop also has a rich ecosystem of frameworks and tools that extend its functionality and provide higher-level abstractions for data analysis, such as Pig, Hive, and HBase.

- Pig is a high-level scripting language that allows users to write complex data transformations and analysis using a set of operators and functions.
- Pig scripts are compiled into MapReduce jobs and executed on Hadoop clusters.
- Pig provides a data model that consists of atomic values, tuples, bags, and maps, and supports both structured and unstructured data.
- Pig also has a user-defined function (UDF) mechanism that allows users to write custom functions in Java, Python, or other languages and invoke them from Pig scripts.
- Pig is suitable for data pipelines, data cleansing, data integration, and ad-hoc queries.

- Hive is a data warehouse system that provides a SQL-like query language called HiveQL for querying and analyzing structured and semi-structured data stored in HDFS or other data sources.
- HiveQL queries are translated into MapReduce jobs and executed on Hadoop clusters.
- Hive provides a data model that consists of tables, partitions, and buckets, and supports various data formats, such as text, JSON, ORC, Parquet, and Avro.
- Hive also has a user-defined function (UDF) mechanism that allows users to write custom functions in Java, Python, or other languages and invoke them from HiveQL queries.
- Hive is suitable for data warehousing, data mining, business intelligence, and reporting.

- HBase is a distributed, column-oriented, NoSQL database that provides random, real-time read/write access to large-scale data sets.
- HBase runs on top of HDFS and uses Hadoop's MapReduce and ZooKeeper for distributed processing and coordination.
- HBase provides a data model that consists of tables, rows, columns, and cells, and supports both single-row and batch operations.
- HBase also has a coprocessor framework that allows users to write custom logic that runs on the server side, such as filters, aggregations, and transactions.
- HBase is suitable for low-latency applications, such as web analytics, online recommendation systems, and time series data.