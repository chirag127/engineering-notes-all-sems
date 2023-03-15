## Unit 3 - Hadoop Eco System and YARN, NoSQL Databases, MongoDB, Spark, Scala

### Hadoop Eco System and YARN
- Hadoop is an open-source framework that allows distributed processing of large datasets across clusters of computers.
- Hadoop ecosystem includes various tools that are built on top of Hadoop to provide additional functionality.
- YARN (Yet Another Resource Negotiator) is a key component of the Hadoop ecosystem that manages resources and schedules tasks across the cluster.
- YARN separates the resource management and job scheduling functions of the earlier MapReduce engine, providing greater flexibility and scalability.
- Some popular tools in the Hadoop ecosystem are:
  - HDFS (Hadoop Distributed File System) - a distributed file system that provides high throughput access to data.
  - MapReduce - a programming model for processing large datasets in parallel across a cluster.
  - Hive - a data warehousing tool that provides SQL-like query language for data analysis.
  - Pig - a platform for analyzing large datasets using a high-level scripting language.
  - Spark - a fast and general-purpose cluster computing system that supports in-memory data processing.

### NoSQL Databases
- NoSQL databases are non-relational databases that provide a flexible, scalable, and high-performance alternative to traditional relational databases.
- NoSQL databases can handle large amounts of unstructured data, such as social media data, sensor data, and machine logs.
- Some popular types of NoSQL databases are:
  - Document-oriented databases - MongoDB, Couchbase, etc.
  - Key-value stores - Redis, Riak, etc.
  - Column-family stores - Cassandra, HBase, etc.
  - Graph databases - Neo4j, OrientDB, etc.
- NoSQL databases provide several advantages over traditional relational databases, such as:
  - Scalability - NoSQL databases can handle large amounts of data and can scale horizontally by adding more nodes to the cluster.
  - Flexibility - NoSQL databases can handle unstructured data and can adapt to changing data models easily.
  - Performance - NoSQL databases can provide high performance by using distributed architectures and optimized data storage formats.

### MongoDB
- MongoDB is a document-oriented NoSQL database that provides a flexible and scalable data storage solution.
- MongoDB stores data in JSON-like documents, which can have nested structures and dynamic schemas.
- MongoDB provides several features, such as:
  - Indexing - MongoDB supports various indexing techniques to improve query performance.
  - Sharding - MongoDB can scale horizontally by partitioning data across multiple servers.
  - Replication - MongoDB can provide high availability and data redundancy by replicating data across multiple servers.
  - Aggregation - MongoDB provides a comprehensive aggregation framework for data analysis and reporting.

### Spark
- Spark is a fast and general-purpose cluster computing system that supports in-memory data processing.
- Spark provides several APIs for data processing, such as:
  - RDD (Resilient Distributed Datasets) - a fault-tolerant collection of data that can be processed in parallel across a cluster.
  - DataFrame - a distributed collection of data organized into named columns that can be manipulated using SQL-like operations.
  - Dataset - a type-safe, object-oriented programming interface that combines the features of RDDs and DataFrames.
- Spark provides several advantages over traditional Hadoop MapReduce, such as:
  - Speed - Spark can process data much faster than traditional MapReduce by keeping data in memory.
  - Ease of use - Spark provides a simple and easy-to-use API for data processing.
  - Compatibility - Spark can run on various cluster managers, such as YARN, Mesos, and standalone mode.

### Scala
- Scala is a programming language that runs on the Java Virtual Machine (JVM) and provides a concise and expressive syntax.
- Scala provides several features, such as:
  - Object-oriented programming - Scala supports object-oriented programming concepts, such as classes, objects, and inheritance.
  - Functional programming - Scala supports functional programming concepts, such as higher-order functions, immutability, and pattern matching.
  - Type inference - Scala can infer types automatically, reducing the need for explicit type declarations.
- Scala is widely used in the big data ecosystem, particularly with Spark, due to its expressiveness and conciseness. 

## Learning Tricks and Mnemonics
- Hadoop Eco System:
  - Mnemonic: "Have a Hadoop Elephant Eating Mangoes" - HDFS, MapReduce, Hive, HBase, ElephantDB, Mahout.
- YARN:
  - Mnemonic: "You Are Really Needed" - YARN separates resource management and job scheduling, making it a critical component of the Hadoop ecosystem.
- MongoDB:
  - Mnemonic: "More Data, More Benefits" - MongoDB can handle large amounts of unstructured data and provides several features, such as indexing, sharding, and replication.
- Spark:
  - Mnemonic: "Spark the Fire" - Spark is fast and supports in-memory data processing, making it a popular choice