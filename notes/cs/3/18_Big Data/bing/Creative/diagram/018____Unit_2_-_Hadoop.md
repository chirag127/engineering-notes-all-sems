## Unit 2 - Hadoop

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers.

Some of the key features of Hadoop are:

- It is open-source and written in Java.
- It uses a distributed file system called Hadoop Distributed File System (HDFS) to store and access data.
- It uses a programming model called MapReduce to process data in parallel on multiple nodes.
- It provides a set of common tools and libraries for data analysis, such as Hive, Pig, Spark, HBase, etc.
- It supports fault-tolerance, scalability, reliability, and security.

Some of the key components of Hadoop are:

- HDFS: It is the storage layer of Hadoop that splits and distributes data across multiple nodes in a cluster. It also replicates data for fault-tolerance and provides high-throughput access to data.
- MapReduce: It is the processing layer of Hadoop that divides a large task into smaller subtasks and assigns them to different nodes in a cluster. It consists of two phases: map and reduce. The map phase applies a user-defined function to each input record and produces intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output.
- YARN: It is the resource management layer of Hadoop that allocates and manages resources (such as CPU, memory, disk, network, etc.) for different applications running on a cluster. It consists of two components: a Resource Manager that coordinates the resources among different applications, and a Node Manager that monitors and reports the resources on each node.
- Common: It is the set of utilities and libraries that support the other components of Hadoop. It includes configuration, serialization, IO, compression, authentication, etc.
- Other: There are many other components that extend the functionality of Hadoop, such as Hive, Pig, Spark, HBase, ZooKeeper, Oozie, Sqoop, Flume, etc. They provide different capabilities for data analysis, such as SQL-like querying, scripting, streaming, graph processing, columnar storage, coordination, workflow management, data ingestion, etc.