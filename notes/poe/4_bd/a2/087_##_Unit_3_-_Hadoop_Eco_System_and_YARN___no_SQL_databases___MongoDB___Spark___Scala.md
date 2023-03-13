 Here is the content in markdown format for ## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala:

## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

### Hadoop Eco System and YARN

- Hadoop Eco System refers to the suite of big data tools and frameworks developed around Hadoop. Some of the major components are:
- HDFS - Distributed File System to store large data
- MapReduce - Framework for running distributed computations on large clusters
- YARN - Resource management platform to allocate resources to applications running on Hadoop
- Pig - Platform to analyze large data sets using Pig Latin scripting language
- Hive - Data warehouse infrastructure to query and manage large datasets using SQL-like language
- Sqoop - Tool to transfer data between Hadoop and relational databases
- Flume - Tool to aggregate and move large amounts of log data into HDFS
- Oozie - Workflow scheduler system to manage Hadoop jobs

Advantages: Scalable, Fault tolerant, Cost effective, Open source
Disadvantages: Steep learning curve, Complex architecture

YARN stands for Yet Another Resource Negotiator. It is a cluster management technology for Hadoop. It has a central ResourceManager and per-application ApplicationMaster. It separates resource management and job scheduling/monitoring functions. It allows running both batch and interactive applications on Hadoop.

### NoSQL Databases

NoSQL databases are non tabular databases that do not require a fixed schema. They have a dynamic schema. Some popular NoSQL databases are:
- MongoDB - Document oriented database, stores data in JSON like documents
- Cassandra - Column oriented database, stores data in tables with columns
- HBase - Wide column store database, built on top of Hadoop
- Redis - Key-value store database, stores data in key-value pairs

Advantages: Scalable, Schema free, Distributed
Disadvantages: Limited query capabilities, Eventual consistency

### MongoDB

MongoDB is a document oriented NoSQL database. Data is stored in JSON like documents. A database contains collections which contains documents.
Some key points:
- Dynamic schema: Documents in a collection can have different fields
- Indexes: Can create indexes on fields to speed up queries
- Replication: Supports replication for fault tolerance and scalability
- Sharding: Can be sharded to store very large amounts of data
- Uses BSON to store data
- Has drivers for many languages like Python, Java, etc.

Use cases: Content management systems, Real time analytics, Mobile applications

### Spark and Scala

Spark is a fast and general cluster computing system. It has APIs in Scala, Java, Python, and R. Some key points:
- Resilient Distributed Datasets (RDDs): Core data abstraction in Spark, represents immutable partitioned collection of elements
- Runs on Hadoop, Mesos, standalone, or in the cloud
- Supports multiple languages
- Has libraries for SQL, machine learning, graph processing, and streaming

Scala is a programming language that runs on JVM. It combines Object Oriented and Functional programming concepts. Some key points:
- Statically typed
- Supports both Object Oriented and Functional styles
- Has lesser boilerplate code than Java
- seamlessly integrates with Java
- Used to develop Spark applications

Use cases: Machine learning, Real time processing, Graph processing