### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following core components :

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS can handle different types of data, such as structured, semi-structured, or unstructured, without prior organization. HDFS also provides fault tolerance, replication, and high availability features  .
- **MapReduce**: This is the processing layer of Hadoop that allows parallel execution of user-defined functions on the data stored in HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a function to each input key-value pair and generates intermediate key-value pairs. The reduce phase aggregates the intermediate key-value pairs by the same key and produces the final output  .
- **Yet Another Resource Negotiator (YARN)**: This is the resource management layer of Hadoop that allocates and schedules resources (such as CPU, memory, disk, and network) to different applications running on the cluster. YARN consists of two components: a resource manager that manages the cluster resources and a node manager that runs on each node and monitors the resource usage and health of the node  .

Some other components of Hadoop that are not core but provide additional functionality are:

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other Hadoop components. It includes configuration files, scripts, and Java classes .
- **Hive**: This is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. It converts SQL queries into MapReduce jobs and executes them on the cluster.
- **Pig**: This is a scripting language that allows users to write complex data transformations and analysis using a high-level syntax. It also converts the scripts into MapReduce jobs and executes them on the cluster.
- **HBase**: This is a NoSQL database that provides random access and real-time updates to large-scale data stored in HDFS. It is based on the Google Bigtable model and supports row-level transactions and versioning.
- **Spark**: This is a fast and general-purpose processing engine that can run on top of Hadoop. It supports batch, streaming, interactive, and machine learning applications. It uses an in-memory data structure called resilient distributed dataset (RDD) to store and process data .
- **Sqoop**: This is a tool that allows users to transfer data between Hadoop and relational databases. It can import data from relational databases to HDFS and export data from HDFS to relational databases.
- **Flume**: This is a tool that allows users to collect and ingest streaming data from various sources (such as web servers, social media, sensors, etc.) to HDFS. It uses agents that run on the source nodes and forward the data to the destination nodes.
- **Oozie**: This is a workflow scheduler that allows users to define and execute complex workflows of Hadoop jobs. It supports dependency management, error handling, and notification features.