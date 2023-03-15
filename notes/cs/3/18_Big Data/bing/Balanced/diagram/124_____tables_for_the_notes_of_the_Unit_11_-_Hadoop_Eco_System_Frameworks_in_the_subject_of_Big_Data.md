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
| YARN | Yet Another Resource Negotiator. It is a framework that manages the resources and scheduling of the tasks on the cluster. It consists of two components: Resource Manager and Node Manager. Resource Manager is the master daemon that allocates the resources to the applications. Node Manager is the slave daemon that runs on each node and monitors the resource usage and task execution. |
| Hadoop Common | It is a set of common utilities and libraries that support the other Hadoop modules. It provides the basic functionality such as configuration, I/O, serialization, and networking. |

- Hadoop Ecosystem also consists of various other components that provide additional functionalities such as data ingestion, data analysis, data processing, data visualization, etc.
- Some of the popular Hadoop Ecosystem components are:

| Component | Description |
|-----------|-------------|
| Hive | It is a data warehouse system that provides a SQL-like interface to query and analyze structured and semi-structured data stored in HDFS. It converts the SQL queries into MapReduce jobs under the hood. |
| Pig | It is a data flow language that provides a high-level abstraction to write complex data transformations and analysis using a series of operators. It also converts the Pig scripts into MapReduce jobs under the hood. |
| Spark | It is a fast and general-purpose cluster computing system that provides an alternative to MapReduce. It supports in-memory processing and can run various types of applications such as batch processing, streaming, machine learning, graph processing, etc. |
| HBase | It is a distributed and scalable NoSQL database that provides random access and strong consistency for large amounts of sparse and structured data. It is built on top of HDFS and supports CRUD operations and MapReduce integration. |
| Sqoop | It is a tool that allows for the transfer of data between Hadoop and relational databases. It can import data from relational databases to HDFS and export data from HDFS to relational databases. |
| Flume | It is a tool that allows for the collection and aggregation of large amounts of streaming data from various sources such as web servers, application servers, social media, etc. It can transport the data to HDFS, HBase, or other destinations. |
| Kafka | It is a distributed and fault-tolerant messaging system that provides high-throughput and low-latency for real-time data feeds. It can handle millions of messages per second from multiple producers and consumers. |
| Oozie | It is a workflow scheduler that allows for the coordination and execution of complex Hadoop jobs. It can trigger the jobs based on time, data availability, or external events. |
| Zookeeper | It is a centralized service that provides configuration management, synchronization, naming, and group services for distributed applications. It helps in maintaining the consistency and availability of the cluster. |
| Mahout | It is a library that provides scalable and distributed machine learning algorithms for data mining and analytics. It supports various types of algorithms