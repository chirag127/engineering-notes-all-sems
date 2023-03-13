## Hadoop Eco System Frameworks , Pig , Hive and HBase

- Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers using simple programming models.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
- HDFS is a distributed file system that provides high-throughput access to data stored in Hadoop clusters.
- MapReduce is a programming model and an execution engine for parallel processing of large data sets using key-value pairs.
- Hadoop also includes several additional modules that provide additional functionality, such as Hive, Pig, and HBase.

### Pig

- Pig is a high-level platform for creating MapReduce programs using a scripting language called Pig Latin.
- Pig Latin is a data-flow language that allows users to express complex transformations and analysis of data in a simple and declarative way.
- Pig can handle both structured and unstructured data, and supports various data formats, such as text, binary, or JSON.
- Pig can also interact with other Hadoop components, such as HDFS, HBase, or Hive, to read and write data.
- Pig helps to achieve ease of programming and optimization, and hence is a major segment of the Hadoop ecosystem.

### Hive

- Hive is a data warehouse infrastructure that provides data summarization and ad-hoc querying using a SQL-like query language called HiveQL.
- HiveQL is a declarative language that allows users to perform various operations on data stored in Hadoop, such as filtering, grouping, joining, aggregating, and sorting.
- Hive can also support custom functions and scripts written in other languages, such as Python, Java, or Ruby, to extend its functionality.
- Hive can handle both structured and semi-structured data, and supports various data formats, such as text, ORC, Parquet, or Avro.
- Hive can also interact with other Hadoop components, such as HDFS, HBase, or Pig, to read and write data.
- Hive performs reading and writing of large data sets using SQL methodology and interface, and hence is a major segment of the Hadoop ecosystem.

### HBase

- HBase is a distributed column-oriented database that supports structured data storage for large tables.
- HBase is an open-source project and horizontally scalable, meaning that it can handle increasing amounts of data and requests by adding more nodes to the cluster.
- HBase is a data model that is similar to Google's BigTable, and designed to provide quick random access to huge amounts of structured data.
- HBase can also support atomic operations, such as increment, decrement, or append, on individual cells or rows.
- HBase can also interact with other Hadoop components, such as HDFS, MapReduce, or Hive, to read and write data.
- HBase is a major segment of the Hadoop ecosystem for applications that require low-latency and high-throughput access to data.

### Mnemonics and learning tricks

- A possible mnemonic to remember the names and functions of the Hadoop ecosystem frameworks is:

  - **H**ave **P**izza **H**ere **B**efore **M**idnight
  - **H**adoop: distributed processing of large data sets
  - **P**ig: high-level platform for creating MapReduce programs
  - **H**ive: data warehouse infrastructure for data summarization and ad-hoc querying
  - **B**ase: distributed column-oriented database for structured data storage
  - **M**apReduce: programming model and execution engine for parallel processing of large data sets

- A possible learning trick to understand the differences and similarities between Pig and Hive is:

  - Pig and Hive are both high-level platforms for creating MapReduce programs, but they use different languages and data models.
  - Pig uses a scripting language called Pig Latin, which is a data-flow language that allows users to express complex transformations and analysis of data in a simple and declarative way.
  - Hive uses a query language called HiveQL, which is a SQL-like language that allows users to perform various operations on data stored in Hadoop, such as filtering, grouping, joining, aggregating, and sorting.
  - Pig can handle both structured and unstructured data, and supports various data formats, such as text, binary, or JSON.
  - Hive can handle both structured and semi-structured data, and supports various data formats, such as text, ORC, Parquet, or Avro.
  - Pig and Hive can both interact with other Hadoop components, such as HDFS, HBase, or MapReduce, to