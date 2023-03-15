### Hadoop Eco System Frameworks

Hadoop is a framework that enables processing of large data sets which reside in the form of clusters. Being a framework, Hadoop is made up of several modules that are supported by a large ecosystem of technologies.

The Hadoop ecosystem is a collection of tools, libraries, and frameworks that help you build applications on top of Apache Hadoop. Hadoop provides massive parallelism with low latency and high throughput, which makes it well-suited for big data problems.

Some of the major components of the Hadoop ecosystem are:

- **HDFS**: Hadoop Distributed File System is a distributed file system that has the capability to store a large stack of data sets. HDFS provides high availability, fault tolerance, scalability, and reliability.
- **MapReduce**: MapReduce is a programming model that allows for the distributed processing of large data sets across clusters of computers using simple programming models. MapReduce consists of two phases: map and reduce. The map phase takes an input and transforms it into a set of key-value pairs. The reduce phase takes the output of the map phase and aggregates the values based on the keys.
- **YARN**: Yet Another Resource Negotiator is a resource management layer that allocates and manages resources for the applications running on Hadoop. YARN consists of two components: a resource manager that oversees the cluster resources and a node manager that runs on each node and monitors the resource usage and health of the node.
- **Hadoop Common**: Hadoop Common is a set of utilities and libraries that support the other Hadoop modules. It provides common functionalities such as configuration, logging, security, serialization, and I/O operations.

Apart from these core components, there are many other tools and frameworks that are part of the Hadoop ecosystem, such as:

- **Hive**: Hive is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. Hive supports a variety of data formats, such as text, JSON, ORC, Parquet, and Avro. Hive also supports user-defined functions, joins, aggregations, and subqueries.
- **Pig**: Pig is a scripting language that allows for the analysis and transformation of data stored in HDFS. Pig supports a high-level language called Pig Latin, which is similar to SQL, and a low-level language called Pig Engine, which is similar to MapReduce. Pig also supports user-defined functions, complex data types, and nested data structures.
- **Spark**: Spark is a fast and general-purpose cluster computing system that provides an alternative to MapReduce. Spark supports a variety of data sources, such as HDFS, Hive, HBase, Cassandra, and Kafka. Spark also supports a variety of data processing frameworks, such as SQL, Streaming, Machine Learning, and GraphX.
- **HBase**: HBase is a distributed and scalable NoSQL database that provides random access and strong consistency for large amounts of structured and semi-structured data. HBase is built on top of HDFS and supports row-level transactions, versioning, compression, and replication.
- **Sqoop**: Sqoop is a tool that allows for the transfer of data between Hadoop and relational databases. Sqoop supports incremental imports, exports, and joins of data from various sources, such as MySQL, Oracle, PostgreSQL, and SQL Server.
- **Flume**: Flume is a tool that allows for the collection and aggregation of streaming data from various sources, such as web servers, application servers, and social media. Flume supports a variety of sinks, such as HDFS, HBase, Hive, and Kafka.
- **Kafka**: Kafka is a distributed and fault-tolerant messaging system that provides high throughput and low latency for streaming data. Kafka supports a publish-subscribe model, where producers publish messages to topics and consumers subscribe to topics and consume messages.
- **Oozie**: Oozie is a workflow scheduler that allows for the coordination and execution of complex Hadoop jobs. Oozie supports a variety of actions, such as MapReduce, Pig, Hive, Sqoop, and Spark. Oozie also supports conditional branching, looping, and parallel execution of workflows.
- **Zookeeper**: Zookeeper is a distributed and highly available coordination service that provides configuration management, naming service, synchronization, and group membership for distributed applications. Zookeeper supports a hierarchical namespace, where nodes can store data and have children nodes.

These are