## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

- Hadoop Eco System is a collection of open-source software components and tools that enable large-scale data processing and analysis on a distributed computing platform. Some of the components are:

  - Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to data across multiple nodes.
  - MapReduce: A programming model and framework for parallel processing of large data sets using key-value pairs.
  - Hadoop Common: A set of libraries and utilities that support the other Hadoop components.
  - Hadoop YARN: A resource management layer that allocates and schedules computing resources for applications running on Hadoop clusters.
  - Hadoop ZooKeeper: A service that provides coordination and synchronization for distributed applications.
  - Hadoop Oozie: A workflow scheduler that orchestrates and executes Hadoop jobs.
  - Hadoop Hive: A data warehouse system that provides a SQL-like interface for querying and analyzing data stored in HDFS.
  - Hadoop Pig: A scripting language and platform for data transformation and analysis on Hadoop.
  - Hadoop HBase: A column-oriented database that provides random access and consistent updates for large data sets on HDFS.
  - Hadoop Sqoop: A tool that transfers data between Hadoop and relational databases.
  - Hadoop Flume: A service that collects and aggregates data from various sources and delivers it to HDFS or other destinations.
  - Hadoop Spark: A fast and general engine for large-scale data processing that supports batch, streaming, SQL, machine learning, and graph analytics.

- NoSQL databases are non-relational databases that store and retrieve data in different ways than traditional relational databases. Some of the advantages of NoSQL databases are:

  - They can handle unstructured, semi-structured, or schema-less data, such as JSON, XML, documents, graphs, etc.
  - They can scale horizontally by adding more nodes to the cluster, without compromising performance or availability.
  - They can provide flexible and dynamic data models that can evolve with changing business requirements.
  - They can offer high performance, low latency, and high availability for real-time applications.

- MongoDB is a popular NoSQL database that stores data as documents in a binary format called BSON (Binary JSON). Some of the features of MongoDB are:

  - It supports dynamic schemas that allow documents in the same collection to have different fields and structures.
  - It supports various query operators and indexes for efficient data retrieval and manipulation.
  - It supports aggregation framework and map-reduce for complex data analysis and transformation.
  - It supports replication and sharding for high availability and scalability.
  - It supports ACID transactions for multi-document operations within a single replica set.

- Spark is a fast and general engine for large-scale data processing that supports batch, streaming, SQL, machine learning, and graph analytics. Some of the features of Spark are:

  - It uses a distributed memory abstraction called resilient distributed datasets (RDDs) that allow parallel operations on large data sets across multiple nodes.
  - It supports lazy evaluation and caching of RDDs for improved performance and fault tolerance.
  - It supports various APIs and libraries for different languages and domains, such as Spark SQL, Spark Streaming, Spark MLlib, and Spark GraphX.
  - It supports various data sources and formats, such as HDFS, Hive, HBase, Kafka, Parquet, JSON, etc.
  - It supports various cluster managers and deployment modes, such as YARN, Mesos, Kubernetes, standalone, local, etc.

- Scala is a general-purpose programming language that combines object-oriented and functional paradigms. Some of the features of Scala are:

  - It is interoperable with Java and runs on the Java Virtual Machine (JVM).
  - It supports concise and expressive syntax and powerful type system.
  - It supports multiple inheritance and mixin composition through traits.
  - It supports higher-order functions, pattern matching, and immutable data structures.
  - It supports concurrency and parallelism through actors and futures.