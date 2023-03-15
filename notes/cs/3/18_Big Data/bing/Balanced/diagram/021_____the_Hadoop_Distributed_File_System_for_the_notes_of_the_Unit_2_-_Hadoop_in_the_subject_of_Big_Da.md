### The Hadoop Distributed File System

- The Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across highly scalable Hadoop clusters  .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
- The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the worker nodes that store and retrieve data blocks from local disks as instructed by the NameNode.
- HDFS splits files into large blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes in the cluster .
- HDFS also replicates each block across multiple DataNodes to ensure fault tolerance and high availability .
- HDFS supports a MapReduce programming model for parallel processing of large data sets .
- HDFS is designed to run on commodity hardware and handle hardware failures gracefully .
- HDFS does not require schemas to be defined up front and can store any type of data, structured or unstructured.