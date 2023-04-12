### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following core components :

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS can handle different types of data, such as structured, semi-structured, or unstructured, without prior organization. HDFS also provides fault tolerance, replication, and high availability features  .
- **MapReduce**: This is the processing layer of Hadoop that allows parallel execution of user-defined functions on the data stored in HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a function to each input key-value pair and produces intermediate key-value pairs. The reduce phase aggregates the intermediate key-value pairs by the same key and produces the final output  .
- **YARN**: This is the resource management layer of Hadoop that allocates and manages resources (such as CPU, memory, disk, and network) for the applications running on the cluster. YARN also provides scheduling, monitoring, and security features for the applications  .

Some other components of Hadoop that are not core but are commonly used are:

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other components of Hadoop. It includes configuration, logging, serialization, and I/O modules .
- **Hive**: This is a data warehouse system that provides a SQL-like interface for querying and analyzing data stored in HDFS. It also supports data partitioning, compression, and indexing features .
- **Pig**: This is a scripting language that allows users to write complex data transformations and analysis using a high-level syntax. It also supports user-defined functions and operators .
- **HBase**: This is a column-oriented database that provides low-latency random access to large-scale data stored in HDFS. It also supports transactions, replication, and consistency features .
- **Spark**: This is a fast and general-purpose processing engine that can run on top of Hadoop. It supports batch, streaming, interactive, and machine learning applications. It also provides a rich set of APIs in Scala, Java, Python, and R languages .
- **Sqoop**: This is a tool that allows users to transfer data between Hadoop and relational databases. It supports incremental and parallel data transfer features .
- **Flume**: This is a tool that allows users to collect, aggregate, and move large amounts of streaming data from various sources to HDFS. It supports multiple sources, sinks, and channels .
- **Oozie**: This is a workflow scheduler that allows users to define and execute complex workflows of Hadoop jobs. It supports dependency, concurrency, and retry features .
- **ZooKeeper**: This is a coordination service that provides distributed synchronization, configuration, and naming for the applications running on the cluster. It also provides high availability and fault tolerance features .

The following diagram shows the architecture of Hadoop and its components:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Hadoop       |     |    Hadoop       |     |    Hadoop       |
|    Common       |     |    Common       |     |    Common       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    MapReduce    |     |    MapReduce    |     |    MapReduce    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    YARN         |     |    YARN         |     |    YARN         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|

```
