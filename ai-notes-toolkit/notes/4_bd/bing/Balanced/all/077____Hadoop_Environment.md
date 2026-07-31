## Hadoop Environment

- Hadoop is an open source software framework that is used for storing and processing large amounts of data in a distributed computing environment   .
- Hadoop is based on the MapReduce programming model, which allows for the parallel processing of large datasets by dividing them into smaller chunks and assigning them to different nodes in the cluster.
- Hadoop has two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce.
  - HDFS is a distributed file system that provides high-throughput access to data across multiple nodes. It stores data in blocks and replicates them across the cluster for fault tolerance.
  - Hadoop MapReduce is a software framework that implements the MapReduce programming model. It consists of two phases: map and reduce. The map phase takes input data and transforms it into key-value pairs. The reduce phase aggregates the values associated with the same key and produces the final output.
- Hadoop also has a rich ecosystem of tools and applications that extend its functionality and provide additional features. Some of the popular ones are:
  - Apache Pig: a high-level scripting language for data analysis and manipulation.
  - Apache Hive: a data warehouse system that provides a SQL-like interface for querying and analyzing data stored in HDFS.
  - Apache HBase: a distributed, column-oriented database that provides random access and strong consistency for large-scale data.
  - Apache Spark: a fast and general engine for large-scale data processing that supports batch, streaming, and interactive applications.
  - Apache Sqoop: a tool that transfers data between HDFS and relational databases.
  - Apache Flume: a service that collects, aggregates, and moves large amounts of log data from various sources to HDFS.
  - Apache Oozie: a workflow scheduler that coordinates and executes Hadoop jobs.
  - Apache ZooKeeper: a centralized service that provides coordination and configuration management for distributed systems.
- Hadoop requires the Java Runtime Environment (JRE) 1.6 or higher. The standard startup and shutdown scripts require that Secure Shell (SSH) be set up between nodes in the cluster.
- Hadoop can run on a single node or a cluster of nodes. The cluster can be composed of commodity computers, which are cheap and widely available.
- Hadoop is one of the technologies that enables big data, which refers to the collection and analysis of large and complex data sets that traditional data processing systems cannot handle.

A possible mnemonic to remember the main components and tools of Hadoop is:

**H**adoop **D**istributed **F**ile **S**ystem, **H**adoop **M**ap**R**educe, **P**ig, **H**ive, **H**Base, **S**park, **S**qoop, **F**lume, **O**ozie, **Z**ooKeeper

Or: HDFSHMRPHHSSFOZ

A possible ascii diagram to illustrate the Hadoop environment is:

```
+-----------------+    +-----------------+    +-----------------+
|     Node 1      |    |     Node 2      |    |     Node 3      |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | HDFS Block | |    | | HDFS Block | |    | | HDFS Block | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | MapReduce  | |    | | MapReduce  | |    | | MapReduce  | |
| | Task       | |    | | Task       | |    | | Task       | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         +---------------------+---------------------+
                           |
                           v
+----------------------------------------------------+
|                  Hadoop Ecosystem                  |
| +------+ +------+ +------+ +------+ +------+ +---+ |
| | Pig  | | Hive  | | HBase | | Spark | | Sqoop | |...|
| +------+ +------+ +------+ +------+ +------+ +---+ |
+----------------------------------------------------+
```