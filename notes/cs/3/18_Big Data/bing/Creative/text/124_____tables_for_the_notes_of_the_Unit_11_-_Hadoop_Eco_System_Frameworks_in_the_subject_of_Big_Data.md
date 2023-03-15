### Tables for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data

- Table 1: Definition and description of Hadoop and its ecosystem

| Term | Definition | Description |
|------|------------|-------------|
| Hadoop | An open-source software framework for distributed processing of large data sets across clusters of computers | Hadoop provides massive parallelism with low latency and high throughput, which makes it well-suited for big data problems  |
| Hadoop Ecosystem | A platform or a suite that provides various services and tools to solve the big data problems using Hadoop | Hadoop ecosystem includes Apache projects and various commercial tools and solutions. There are four major elements of Hadoop: HDFS, MapReduce, YARN, and Hadoop Common   |

- Table 2: Components and functions of Hadoop ecosystem

| Component | Function |
|-----------|----------|
| HDFS | Hadoop Distributed File System: A distributed file system that stores data across multiple nodes in a cluster. It provides high availability, fault tolerance, scalability, and reliability   |
| MapReduce | A programming model and an execution engine for processing large data sets in parallel. It consists of two phases: map and reduce. Map applies a user-defined function to each input record and produces intermediate key-value pairs. Reduce aggregates the intermediate values associated with the same key and produces the final output   |
| YARN | Yet Another Resource Negotiator: A resource management layer that allocates and schedules resources (CPU, memory, disk, network) for the applications running on Hadoop. It consists of two components: ResourceManager and NodeManager. ResourceManager is the master that arbitrates resources among all the applications. NodeManager is the agent that runs on each node and manages the containers (units of resources) assigned to it   |
| Hadoop Common | A set of common utilities and libraries that support the other Hadoop modules. It includes configuration, I/O, serialization, compression, authentication, and IPC (inter-process communication) components  |

- Table 3: Examples of Hadoop ecosystem tools and their use cases

| Tool | Use Case |
|------|----------|
| Hive | A data warehouse system that provides a SQL-like interface (HiveQL) to query and analyze structured and semi-structured data stored in HDFS. It supports various data formats, such as text, JSON, ORC, Parquet, and Avro  |
| Pig | A high-level scripting language (Pig Latin) that allows users to write complex data transformations and analysis using a series of operators. It compiles the scripts into MapReduce jobs and runs them on Hadoop  |
| Spark | A fast and general-purpose cluster computing system that supports in-memory processing and interactive analysis. It provides APIs in Scala, Python, Java, and R, and supports various libraries, such as Spark SQL, Spark Streaming, MLlib, and GraphX  |
| HBase | A distributed and scalable NoSQL database that provides random read/write access to large data sets. It is based on the Google Bigtable model and stores data in column-oriented tables. It is suitable for applications that require low latency and high throughput  |
| Sqoop | A tool that transfers data between Hadoop and relational databases. It supports incremental imports and exports, and can handle large data sets efficiently. It can also generate Hive and HBase schemas from the database metadata  |
| Flume | A distributed and reliable service that collects, aggregates, and moves large amounts of streaming data from various sources (such as web servers, application logs, social media, etc.) to HDFS, HBase, or other destinations. It supports various sources, sinks, and channels, and can handle complex data flows  |
| Kafka | A distributed and fault-tolerant messaging system that provides high-throughput and low-latency data ingestion and delivery. It is based on the publish-subscribe model and can handle multiple producers and consumers. It can also integrate with Hadoop, Spark, Storm, and other frameworks