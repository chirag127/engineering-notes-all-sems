### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across scalable Hadoop clusters  .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in the form of blocks.
  - HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across multiple DataNodes .
- HDFS supports the MapReduce programming model, which is a framework for parallel processing of large data sets .
  - MapReduce transfers packaged code into DataNodes to process the data in parallel.
  - MapReduce consists of two phases: map and reduce.
    - Map phase applies a user-defined function to each block of data and produces intermediate key-value pairs.
    - Reduce phase aggregates the intermediate key-value pairs by keys and produces the final output.
- HDFS is designed to handle hardware failures, data replication, load balancing, and data locality .
  - HDFS can detect and recover from hardware failures by replicating each block of data to multiple DataNodes .
  - HDFS can balance the load of data and computation across the cluster by moving blocks from one DataNode to another.
  - HDFS can optimize the performance of MapReduce by placing the computation near the data, i.e., running the map tasks on the same DataNodes where the data blocks are stored.