### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following core components :

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS can handle different types of data, such as structured, semi-structured, or unstructured, without prior organization. HDFS also provides fault tolerance, replication, and high availability features.
- **Hadoop MapReduce**: This is the processing layer of Hadoop that allows parallel execution of user-defined functions on the data stored in HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a function to each input key-value pair and produces intermediate key-value pairs. The reduce phase aggregates the intermediate key-value pairs by the same key and produces the final output.
- **Hadoop YARN**: This is the resource management layer of Hadoop that allocates and schedules resources for different applications running on the cluster. YARN stands for Yet Another Resource Negotiator. YARN consists of two components: a Resource Manager that manages the cluster resources and a Node Manager that runs on each node and monitors the resource usage and health of the node.

Some other components of Hadoop that are not core but provide additional functionality are:

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other Hadoop components. It includes configuration files, scripts, and Java classes.
- **Hadoop ZooKeeper**: This is a service that provides coordination and synchronization for distributed applications. It maintains a hierarchical namespace of configuration data and ensures consistency and reliability among the nodes.
- **Hadoop HBase**: This is a column-oriented database that runs on top of HDFS and provides random access and real-time read/write operations on large data sets.
- **Hadoop Hive**: This is a data warehouse that allows querying and analyzing data stored in HDFS using a SQL-like language called HiveQL.
- **Hadoop Pig**: This is a scripting language that allows writing complex data transformations and analysis on HDFS using a high-level abstraction.
- **Hadoop Spark**: This is a fast and general-purpose engine for large-scale data processing that supports batch, streaming, interactive, and machine learning applications. Spark can run on Hadoop YARN or standalone mode.
- **Hadoop Oozie**: This is a workflow scheduler that allows defining and executing workflows of Hadoop jobs, such as MapReduce, Pig, Hive, or Spark. Oozie can also trigger workflows based on time or data availability.