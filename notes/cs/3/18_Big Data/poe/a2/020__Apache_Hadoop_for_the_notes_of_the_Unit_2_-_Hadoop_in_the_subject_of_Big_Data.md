 Here are the notes for Apache Hadoop for Unit 2 - Hadoop in Big Data:

### Apache Hadoop

1. Apache Hadoop is an open-source software framework for distributed storage and processing of very large data sets on computer clusters.
2. It is designed to scale up from single servers to thousands of machines, with very high fault tolerance.
3. Hadoop has two major components:
 - Hadoop Distributed File System (HDFS) - a distributed file system that stores data on commodity machines, providing very high aggregate throughput access to application data.
 - MapReduce - a programming model for large scale data processing. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key.
4. Hadoop's distributed processing model enables data locality for tasks, minimizing network congestion.
5. Hadoop is highly fault-tolerant due to data replication and task retry mechanisms.
6. Hadoop is written in Java and is cross-platform compatible. It has a large ecosystem of tools and libraries.
7. Hadoop is highly scalable - Facebook has a Hadoop cluster with more than 100 PB of data storage.
8. Hadoop's HDFS and MapReduce components are well suited for batch processing workloads. For low-latency requirements, other distributed systems are used.

Does this look okay? Let me know if you would like me to modify or add anything.