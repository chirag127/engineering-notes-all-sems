# Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to data across highly scalable Hadoop clusters  .
- HDFS splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel using MapReduce programming model.
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in the local file system and performs read and write operations on the data as instructed by the NameNode.
- HDFS is designed to handle large data sets running on commodity hardware, and to tolerate hardware failures .
  - HDFS can scale to hundreds or thousands of nodes in a cluster.
  - HDFS can automatically replicate data blocks across multiple nodes for fault tolerance.
  - HDFS can detect and recover from node failures by re-replicating the data blocks to other nodes.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
  - MapReduce is a framework for parallel processing of large data sets using a key-value pair approach.
  - YARN is a framework for job scheduling and cluster resource management.