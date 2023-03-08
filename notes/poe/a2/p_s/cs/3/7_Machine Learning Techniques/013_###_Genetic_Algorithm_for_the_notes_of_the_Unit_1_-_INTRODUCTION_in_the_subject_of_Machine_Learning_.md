 Here is the content in Markdown format for the given topic:

## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

**Hadoop Eco System:**

- Hadoop Distributed File System (HDFS) - Distributed storage system for big data. Stores data across multiple machines in redundant manner.
- MapReduce - Programming model for distributed processing of large data sets. Divides the task into Map and Reduce phases.
- YARN - Resource management platform that allocates resources to the applications running on Hadoop.
- HBase - NoSQL database running on top of HDFS. Stores huge amount of structured data and provides real-time read/write access.
- Hive - Data warehouse infrastructure to process large data sets in a distributed fashion. Uses SQL-like language called HiveQL.
- Pig - Platform for analyzing large data sets using a high-level language called Pig Latin. Converts to MapReduce programs to execute on Hadoop.
- Oozie - Workflow scheduler system to manage Hadoop jobs.
- ZooKeeper - Centralized service for maintaining configuration information, naming, synchronization, and group services for distributed applications.

**NoSQL Databases:**

- Key-value stores: Data stored in an array of key-value pairs. Examples: DynamoDB, Riak.
- Document stores: Data stored in documents (instead of rows/columns in tabular format). Examples: MongoDB, CouchDB.
- Wide-column stores: Stores data in columns instead of rows. Examples: Cassandra, HBase.
- Graph stores: Stores data in graph structures with nodes, properties, and lines. Examples: Neo4J, InfiniteGraph.

**Advantages:** Scalability, Distributed, Open source, Schema-less.
**Disadvantages:** Limited query capabilities, Eventual consistency.

**MongoDB:**

- Document-oriented NoSQL database.
- Data stored in BSON documents.
- Schema-less with dynamic schemas.
- Scalable and distributed.
- Uses shards and replica sets for scaling and high availability.
- Written in C++.
- Uses MapReduce and aggregation pipelines for data processing.

[Further details and examples can be added here]