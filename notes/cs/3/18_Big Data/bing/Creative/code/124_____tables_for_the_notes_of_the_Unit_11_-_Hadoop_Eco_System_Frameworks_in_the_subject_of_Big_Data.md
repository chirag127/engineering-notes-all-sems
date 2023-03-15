### Tables for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data

- Hadoop is a framework that enables processing of large data sets which reside in the form of clusters.
- Hadoop is made up of several modules that are supported by a large ecosystem of technologies.
- Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems.
- Hadoop Ecosystem includes Apache projects and various commercial tools and solutions.
- There are four major elements of Hadoop i.e. HDFS, MapReduce, YARN, and Hadoop Common.

| Element | Description |
|---------|-------------|
| HDFS | Hadoop Distributed File System. It is a distributed file system that has the capability to store a large stack of data sets. It provides high availability, fault tolerance, scalability, and reliability. |
| MapReduce | It is a programming model that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It consists of two phases: Map and Reduce. Map phase takes input data and converts it into key-value pairs. Reduce phase aggregates the key-value pairs based on the keys. |
| YARN | Yet Another Resource Negotiator. It is a framework that manages the resources and scheduling of the tasks on the cluster. It consists of two components: Resource Manager and Node Manager. Resource Manager is the master daemon that allocates the resources to the applications. Node Manager is the slave daemon that runs on each node and executes the tasks assigned by the Resource Manager. |
| Hadoop Common | It is a set of common utilities and libraries that support the other Hadoop modules. It provides the basic functionality such as configuration, I/O, serialization, etc. |

- Apart from the four major elements, there are many other components and tools in the Hadoop Ecosystem that provide various functionalities and services for big data problems.
- Some of the common components and tools in the Hadoop Ecosystem are:

| Component | Description |
|-----------|-------------|
| Hive | It is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. It converts the SQL queries into MapReduce jobs and executes them on the cluster. |
| Pig | It is a scripting language that provides a high-level abstraction to write complex data transformations and analysis on Hadoop. It converts the Pig scripts into MapReduce jobs and executes them on the cluster. |
| HBase | It is a column-oriented NoSQL database that provides random access and real-time updates to large data sets stored in HDFS. It is based on the Google Bigtable model and supports horizontal scalability and high availability. |
| Spark | It is a fast and general-purpose cluster computing system that provides an alternative to MapReduce. It supports in-memory processing and can run various types of applications such as batch, streaming, interactive, and machine learning. |
| Sqoop | It is a tool that allows for the transfer of data between Hadoop and relational databases. It can import data from relational databases to HDFS and export data from HDFS to relational databases. |
| Flume | It is a tool that allows for the collection and aggregation of large amounts of streaming data from various sources to HDFS. It can handle high-volume and high-velocity data such as log files, social media feeds, etc. |
| Kafka | It is a distributed messaging system that provides a high-throughput and low-latency platform for handling real-time data feeds. It can integrate with various data sources and sinks such as Hadoop, Spark, Storm, etc. |
| Oozie | It is a workflow scheduler that allows for the coordination and execution of complex Hadoop jobs. It can trigger and manage the dependencies of various Hadoop tasks such as MapReduce, Pig, Hive, Sqoop, etc. |
| Zookeeper | It is a distributed coordination service that provides a consistent and reliable way of managing the configuration, synchronization, and naming of the cluster nodes. It can handle the failures and changes of the cluster nodes and ensure the availability and consistency of the services. |
| Mahout | It is a