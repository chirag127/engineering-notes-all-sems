# Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

- Hadoop Eco System and YARN
  - Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers.
  - Hadoop consists of three main components: HDFS, MapReduce, and YARN.
  - HDFS is the distributed file system that stores data in blocks across multiple nodes.
  - MapReduce is the programming model that enables parallel processing of data using mapper and reducer functions.
  - YARN is the resource manager that allocates and manages resources for applications running on Hadoop clusters.
  - Hadoop also has a vast ecosystem of tools and libraries that extend its functionality, such as Hive, Pig, HBase, Sqoop, Flume, etc.

- NoSQL databases
  - NoSQL databases are non-relational databases that store data in various formats, such as key-value, document, columnar, graph, etc.
  - NoSQL databases are designed to handle large volumes, high velocity, and high variety of data, often referred to as the 3Vs of big data.
  - NoSQL databases offer advantages such as scalability, flexibility, performance, and availability over traditional relational databases.
  - Some examples of NoSQL databases are MongoDB, Cassandra, HBase, Redis, Neo4j, etc.

- MongoDB
  - MongoDB is a cross-platform, document-oriented, distributed NoSQL database that uses JSON-like documents (BSON) with dynamic schemas.
  - MongoDB supports rich and expressive query language, indexing, aggregation, text search, geospatial queries, etc.
  - MongoDB also provides features such as replication, sharding, transactions, change streams, etc. for high availability, scalability, and consistency.
  - MongoDB can be integrated with Hadoop using MongoDB Connector for Hadoop, which allows reading and writing data between MongoDB and Hadoop.

- Spark
  - Spark is a unified analytics engine for large-scale data processing that supports batch, streaming, SQL, machine learning, and graph processing.
  - Spark runs on top of Hadoop, Mesos, Kubernetes, or standalone clusters, and can access data from various sources, such as HDFS, S3, Cassandra, HBase, MongoDB, etc.
  - Spark consists of four main components: Spark Core, Spark SQL, Spark Streaming, and Spark MLlib.
  - Spark Core is the foundation of Spark that provides distributed task scheduling, memory management, fault tolerance, etc.
  - Spark SQL is the module that enables structured and semi-structured data processing using SQL or DataFrame API.
  - Spark Streaming is the module that enables real-time data processing using DStream or Structured Streaming API.
  - Spark MLlib is the module that provides scalable machine learning algorithms and pipelines.

- Scala
  - Scala is a general-purpose, multi-paradigm programming language that integrates object-oriented and functional programming features.
  - Scala runs on the Java Virtual Machine (JVM) and interoperates with Java libraries and frameworks.
  - Scala is one of the main languages supported by Spark, along with Python, Java, and R.
  - Scala offers advantages such as concise and expressive syntax, high-level abstractions, immutability, pattern matching, etc. for Spark development.