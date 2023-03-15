## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

- Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems. It includes Apache projects and various commercial tools and solutions.
- Hadoop Ecosystem consists of four major elements: HDFS, MapReduce, YARN, and Hadoop Common.
- HDFS is the distributed file system that stores the data in a cluster of nodes. It provides high availability, fault tolerance, scalability, and reliability.
- MapReduce is the programming model that processes the data in parallel using key-value pairs. It consists of two phases: map and reduce. Map phase applies a function to each input record and generates intermediate key-value pairs. Reduce phase aggregates the intermediate values associated with the same key and produces the final output.
- YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop. It is responsible for allocating and scheduling the resources (CPU, memory, disk, network) for the applications running on the cluster. It also monitors and manages the workloads.
- Hadoop Common is the set of common utilities and libraries that support the other Hadoop modules. It provides the basic functionality such as configuration, logging, security, and I/O operations.

- NoSQL databases are non-relational databases that store and retrieve data in different ways than the traditional relational databases. They are designed to handle large volumes of unstructured, semi-structured, or structured data with high performance, scalability, and availability.
- NoSQL databases can be classified into four types: key-value, document, column, and graph. Each type has its own advantages and disadvantages depending on the use case and data model.
- MongoDB is a popular document-based NoSQL database that stores data as JSON-like documents. It supports dynamic schema, indexing, aggregation, replication, sharding, and transactions.
- MongoDB provides various operations to create, read, update, and delete (CRUD) documents, as well as query and analyze the data using filters, projections, sorts, limits, skips, and aggregations.
- MongoDB also supports capped collections, which are fixed-size collections that automatically remove the oldest documents when they reach the maximum size. Capped collections are useful for storing log data, time series data, or other data that needs to be accessed in insertion order.

- Spark is a fast and general-purpose framework for large-scale data processing. It provides an in-memory computation engine that can run up to 100 times faster than MapReduce for certain workloads.
- Spark supports various programming languages such as Scala, Python, Java, and R. It also provides a rich set of libraries for SQL, streaming, machine learning, graph processing, and natural language processing.
- Spark consists of four main components: Spark Core, Spark SQL, Spark Streaming, and Spark MLlib. Spark Core is the base layer that provides the basic functionality such as distributed task scheduling, memory management, fault recovery, and data storage. Spark SQL is the module that supports structured and semi-structured data processing using SQL or DataFrames. Spark Streaming is the module that enables real-time data processing using micro-batches or discretized streams. Spark MLlib is the module that offers scalable and easy-to-use machine learning algorithms and utilities.

- Scala is a multi-paradigm programming language that combines the features of object-oriented and functional programming. It runs on the Java Virtual Machine (JVM) and interoperates seamlessly with Java code.
- Scala is designed to be concise, expressive, and scalable. It supports various features such as pattern matching, higher-order functions, lazy evaluation, immutability, traits, case classes, and implicits.
- Scala is also the native language of Spark, which means that it can leverage the full power and performance of the Spark framework. Scala also offers a REPL (Read-Eval-Print Loop) that allows interactive and iterative development and testing of Spark applications.