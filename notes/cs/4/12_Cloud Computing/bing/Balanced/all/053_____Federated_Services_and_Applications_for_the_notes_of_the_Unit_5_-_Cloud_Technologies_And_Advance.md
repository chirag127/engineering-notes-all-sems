# Federated Services and Applications for Hadoop

- Hadoop is an open source framework that enables distributed processing and storage of large-scale data using clusters of commodity hardware.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
- HDFS is a distributed file system that provides high-throughput access to data across multiple nodes in a cluster. HDFS stores data as blocks and replicates them for fault tolerance.
- MapReduce is a programming model that allows parallel processing of data using key-value pairs. MapReduce consists of two phases: map and reduce. The map phase transforms the input data into intermediate key-value pairs, and the reduce phase aggregates the intermediate values for each key.
- Hadoop also supports a variety of other components and applications that run on top of HDFS and MapReduce, such as Hive, Pig, HBase, Spark, etc. These are collectively known as the Hadoop ecosystem.

## HDFS Federation

- HDFS federation is a feature introduced in Hadoop 2.x that allows multiple independent NameNodes to manage different namespaces in a single cluster.
- A NameNode is the master node that maintains the metadata of the file system, such as the file names, locations, permissions, etc. A namespace is a logical grouping of files and directories in HDFS.
- In the original HDFS architecture, there was only one NameNode per cluster, which limited the scalability, performance, and availability of the file system. The NameNode was also a single point of failure, which required a secondary NameNode or a standby NameNode for backup and recovery.
- In HDFS federation, each NameNode manages a separate namespace and does not communicate with other NameNodes. This improves the scalability and performance of the file system by distributing the metadata load and avoiding bottlenecks. It also increases the availability and reliability of the file system by isolating the failures of individual NameNodes.
- The DataNodes, which are the slave nodes that store the actual data blocks, are shared by all the NameNodes. The DataNodes report the block locations to all the NameNodes and serve the read and write requests from the clients.
- The clients, which are the applications that access the data in HDFS, need to know the mapping of the namespaces to the NameNodes. This can be done by using a configuration file, a service discovery mechanism, or a mount table. The clients can then contact the appropriate NameNode to perform the file system operations.