### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following core components :

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS can handle any type of data, such as structured, semi-structured, or unstructured, without prior organization. HDFS also provides fault tolerance, replication, and high availability features  .
- **MapReduce**: This is the processing layer of Hadoop that allows parallel execution of user-defined functions on the data stored in HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a function to each input key-value pair and generates intermediate key-value pairs. The reduce phase aggregates the intermediate key-value pairs based on the same key and produces the final output  .
- **YARN**: This is the resource management layer of Hadoop that allocates and schedules resources (such as CPU, memory, disk, and network) to different applications running on the cluster. YARN also monitors the health and performance of the nodes and applications. YARN enables Hadoop to support multiple processing frameworks, such as Spark, Hive, Pig, etc., besides MapReduce   .

Some other components of Hadoop that are not core but commonly used are:

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other Hadoop components. It includes configuration files, scripts, Java archives, etc.
- **Hive**: This is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. It converts SQL queries into MapReduce jobs and executes them on the cluster .
- **Pig**: This is a scripting language that allows users to write complex data transformations and analysis using a high-level syntax. It also converts scripts into MapReduce jobs and executes them on the cluster .
- **Spark**: This is a fast and general-purpose processing framework that supports batch, streaming, interactive, and machine learning applications. It can run on Hadoop using YARN or standalone mode. It also provides APIs in Scala, Python, Java, and R .
- **HBase**: This is a distributed and scalable NoSQL database that provides random access and low-latency operations on large data sets. It is based on the Google Bigtable model and stores data in HDFS .
- **Sqoop**: This is a tool that allows users to transfer data between HDFS and relational databases, such as MySQL, Oracle, etc. It can import and export data using parallel MapReduce jobs .
- **Flume**: This is a tool that allows users to collect, aggregate, and transport large amounts of streaming data, such as log files, events, etc., from various sources to HDFS or other destinations .
- **Oozie**: This is a workflow scheduler that allows users to define and execute complex workflows of Hadoop jobs, such as MapReduce, Hive, Pig, etc. It also supports conditional branching, dependencies, and retries .
- **Zookeeper**: This is a coordination service that provides distributed synchronization, configuration management, naming, and group membership for Hadoop components and applications. It maintains a hierarchical namespace of data nodes and ensures their consistency and availability .