### The Hadoop Distributed File System

- The Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across highly scalable Hadoop clusters   .
- HDFS is designed to run on commodity hardware and handle hardware failures gracefully .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - The DataNodes are the worker nodes that store and serve the data blocks of files.
  - HDFS splits files into large blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes in the cluster  .
  - HDFS maintains multiple replicas of each block for fault tolerance and load balancing   .
- HDFS supports a write-once-read-many model, where files are written once and then read by multiple applications .
- HDFS provides a command-line interface and a Java API for interacting with the file system .
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
  - MapReduce is a programming model for parallel processing of large data sets.
  - YARN is a framework for job scheduling and cluster resource management.