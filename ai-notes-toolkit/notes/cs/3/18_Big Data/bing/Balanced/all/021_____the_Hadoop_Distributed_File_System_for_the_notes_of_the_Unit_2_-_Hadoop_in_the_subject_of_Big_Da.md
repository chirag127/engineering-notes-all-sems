# The Hadoop Distributed File System

- The Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to data across highly scalable Hadoop clusters  .
- HDFS is designed to handle large data sets running on commodity hardware, and to scale to hundreds or thousands of nodes.
- HDFS employs a NameNode and DataNode architecture to implement the distributed file system .
  - The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - The DataNodes are the worker nodes that store the data in blocks and perform read and write operations on the blocks as instructed by the NameNode.
- HDFS splits files into large blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes in the cluster .
- HDFS also maintains multiple copies of each block (usually three) for fault tolerance and to improve data availability .
- HDFS supports a MapReduce programming model for parallel processing of large data sets .
  - MapReduce is a framework that divides a computation task into two phases: map and reduce.
  - The map phase applies a user-defined function to each block of data and produces a set of intermediate key-value pairs.
  - The reduce phase aggregates the intermediate values associated with the same key and produces the final output.
  - HDFS transfers the packaged code into the DataNodes to process the data in parallel.
- HDFS provides a command-line interface and a Java API for interacting with the file system.
- HDFS also supports a web-based user interface for browsing the file system and monitoring the cluster status.