# Hadoop Ecosystem for the notes of the Unit 2 - Hadoop in the subject of Big Data

The Hadoop ecosystem is a collection of software components and tools that enable the processing and analysis of large-scale data sets on a distributed computing platform. The Hadoop ecosystem consists of four main layers: data storage, data processing, data access, and data management.

## Data Storage

The data storage layer is responsible for storing the raw data in a distributed and fault-tolerant manner. The core component of this layer is the **Hadoop Distributed File System (HDFS)**, which is a file system that splits the data into blocks and distributes them across multiple nodes in the cluster. HDFS provides high availability, scalability, and reliability for the data .

Other components of the data storage layer include:

- **HBase**: A column-oriented database that runs on top of HDFS and provides random access and real-time updates for large-scale data .
- **Kudu**: A storage system that supports both analytical and transactional workloads on the same platform. It combines the benefits of columnar storage with fast inserts and updates.
- **Alluxio**: A virtual distributed storage system that provides a unified namespace and a caching layer for data from different sources, such as HDFS, S3, or local disks.

## Data Processing

The data processing layer is responsible for executing various types of computations on the data stored in the data storage layer. The core component of this layer is the **MapReduce** framework, which is a programming model that allows parallel processing of large data sets using a map and reduce function. MapReduce divides the data into key-value pairs and distributes them to the map tasks, which perform some transformation on the data. The output of the map tasks is then shuffled and sorted and sent to the reduce tasks, which perform some aggregation or summarization on the data .

Other components of the data processing layer include:

- **YARN**: A resource management system that allocates and schedules the resources (CPU, memory, disk, network) for the applications running on the cluster. YARN is also known as the operating system of the Hadoop ecosystem .
- **Spark**: A fast and general-purpose engine for large-scale data processing. Spark supports batch, streaming, interactive, and machine learning workloads. Spark can run on top of HDFS, HBase, Kudu, or Alluxio, and can use YARN or its own standalone scheduler for resource management .
- **Flink**: A stream processing framework that provides high throughput, low latency, and stateful computations on unbounded and bounded data streams. Flink can run on top of HDFS, HBase, Kudu, or Alluxio, and can use YARN or its own standalone scheduler for resource management.
- **Tez**: A framework that optimizes the execution of complex directed acyclic graphs (DAGs) of tasks. Tez is used by Hive and Pig to improve the performance of their queries .

## Data Access

The data access layer is responsible for providing various interfaces and tools for accessing and querying the data stored in the data storage layer. The core component of this layer is the **Hive** project, which is a data warehouse system that allows SQL-like queries on large-scale data. Hive translates the queries into MapReduce, Spark, or Tez jobs and executes them on the cluster .

Other components of the data access layer include:

- **Pig**: A scripting language that allows complex data transformations and analysis using a high-level syntax. Pig translates the scripts into MapReduce, Spark, or Tez jobs and executes them on the cluster .
- **Impala**: A distributed query engine that provides low-latency and interactive SQL queries on large-scale data. Impala can query data stored in HDFS, HBase, or Kudu, and can use YARN or its own admission control mechanism for resource management.
- **Drill**: A distributed query engine that provides schema-free and self-service SQL queries on various types of data sources, such as HDFS, HBase, Kudu, JSON, CSV, Parquet, etc.
- **Presto**: A distributed query engine that provides fast and interactive SQL queries on large-scale data. Presto can query data