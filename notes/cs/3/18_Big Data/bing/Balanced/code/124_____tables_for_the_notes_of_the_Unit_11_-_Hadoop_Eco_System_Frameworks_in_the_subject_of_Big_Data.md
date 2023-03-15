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
| YARN | Yet Another Resource Negotiator. It is a resource management layer that allocates the resources (CPU, memory, disk, network) to the applications running on the Hadoop cluster. It consists of two components: Resource Manager and Node Manager. Resource Manager is the master daemon that manages the resources across the cluster. Node Manager is the slave daemon that runs on each node and monitors the resource usage and health of the node. |
| Hadoop Common | It is a set of common utilities and libraries that support the other Hadoop modules. It provides the basic functionality such as configuration, I/O, serialization, logging, etc. |

- Apart from the four major elements, there are many other components and tools in the Hadoop Ecosystem that provide additional functionalities and features for big data problems.
- Some of the common components and tools in the Hadoop Ecosystem are:

| Component | Description |
|-----------|-------------|
| Hive | It is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. It converts the SQL queries into MapReduce jobs and executes them on the Hadoop cluster. |
| Pig | It is a scripting language that provides a high-level abstraction to write data analysis programs on Hadoop. It converts the Pig scripts into MapReduce jobs and executes them on the Hadoop cluster. |
| HBase | It is a column-oriented NoSQL database that provides random access and real-time read/write operations on large data sets stored in HDFS. It is based on the Google Bigtable model. |
| Spark | It is a fast and general-purpose cluster computing system that provides an alternative to MapReduce. It supports in-memory processing and can run applications up to 100 times faster than MapReduce. It also provides a rich set of libraries for machine learning, graph processing, streaming, and SQL. |
| Sqoop | It is a tool that allows for the transfer of data between HDFS and relational databases. It can import data from relational databases to HDFS and export data from HDFS to relational databases. |
| Flume | It is a tool that allows for the collection and aggregation of large amounts of streaming data from various sources such as web servers, social media, sensors, etc. It can transport the data to HDFS, HBase, or other destinations. |
| Kafka | It is a distributed messaging system that provides high-throughput, low-latency, and scalable data streaming. It can handle millions of messages per second from multiple producers and consumers. It can be integrated with Hadoop, Spark, Storm, and other big data frameworks. |
| Oozie | It is a workflow scheduler that allows for the coordination and execution of complex Hadoop jobs. It can trigger the jobs based on time, data availability, or external events. It can also manage the dependencies and retries of the jobs. |
| Zookeeper | It is a distributed coordination service that provides reliable and consistent configuration