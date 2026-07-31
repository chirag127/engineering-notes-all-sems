### Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

#### Benefits of HDFS:
- HDFS is designed to handle large data sets: HDFS can store and manage petabytes of data efficiently.
- HDFS is highly fault-tolerant: HDFS replicates data blocks across multiple nodes to ensure data availability in case of node failure.
- HDFS is scalable: HDFS can easily scale horizontally by adding more nodes to the cluster.
- HDFS is cost-effective: HDFS is built on top of commodity hardware, which makes it a cost-effective solution for storing large data sets.

#### Challenges of HDFS:
- HDFS is not suitable for low latency data access: HDFS is designed for batch processing and is not suitable for real-time data access.
- HDFS has limited support for random access: HDFS is optimized for sequential data access and has limited support for random access.
- HDFS has a single point of failure: In HDFS, the NameNode is a single point of failure. If the NameNode fails, the entire HDFS cluster becomes unavailable.
- HDFS has limited support for small files: HDFS is not optimized for storing a large number of small files. Storing a large number of small files can lead to inefficient use of disk space and increased load on the NameNode.