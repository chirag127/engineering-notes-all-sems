# The Hadoop Distributed File System

The Hadoop Distributed File System (HDFS) is a distributed file system that provides high-throughput access to application data across highly scalable Hadoop clusters   . HDFS is one of the core components of Apache Hadoop, along with MapReduce and YARN .

Some of the main features and benefits of HDFS are:

- It can store large files (up to terabytes or petabytes) by splitting them into smaller blocks (typically 64 MB or 128 MB) and distributing them across multiple nodes in a cluster   .
- It can handle hardware failures by replicating each block to multiple nodes (usually three) and automatically recovering from node failures    .
- It can support concurrent access by multiple clients by providing a single namespace for the entire cluster and allowing clients to read and write data from any node   .
- It can optimize data processing by moving computation to the data (instead of the other way around) and using a MapReduce programming model to parallelize and distribute the processing tasks   .
- It can scale up to thousands of nodes and petabytes of data by adding more nodes to the cluster without changing the application code or configuration    .

The main components of HDFS are:

- NameNode: The master node that manages the namespace, the metadata, and the access control of the file system. It also coordinates the placement and replication of blocks across the cluster   .
- DataNode: The worker node that stores and serves the data blocks to the clients. It also performs periodic block reports and heartbeat messages to the NameNode   .
- Client: The application or user that interacts with the file system by using the HDFS API or command-line interface. It can perform operations such as creating, reading, writing, deleting, or copying files or directories   .
- Secondary NameNode: An optional node that performs periodic checkpoints of the NameNode's metadata and helps in recovery in case of NameNode failure  .

The following diagram illustrates the architecture of HDFS:

![HDFS Architecture](https://hadoop.apache.org/docs/r1.2.1/images/hdfsarchitecture.gif)

Source: https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html