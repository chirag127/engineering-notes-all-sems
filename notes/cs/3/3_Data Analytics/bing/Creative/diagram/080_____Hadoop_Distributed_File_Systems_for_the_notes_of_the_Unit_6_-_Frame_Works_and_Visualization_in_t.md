### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across highly scalable Hadoop clusters  .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in the form of blocks.
  - HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across the DataNodes in the cluster .
  - HDFS replicates each block across multiple DataNodes to ensure fault tolerance and availability .
- HDFS supports the MapReduce programming model, which is a YARN-based system for parallel processing of large data sets.
  - MapReduce divides the input data into smaller chunks that are processed by the map tasks in parallel on different nodes.
  - The output of the map tasks are then shuffled and sorted by the framework and fed to the reduce tasks, which aggregate the results and produce the final output.
- HDFS is designed to run on commodity hardware, which means low-cost and widely available machines .
  - HDFS assumes that hardware failures are common and handles them automatically by replicating and recovering data .
  - HDFS also provides mechanisms for data integrity checking, data balancing, and data transfer bandwidth throttling.
- HDFS is suitable for applications that have large data sets, sequential access patterns, and high throughput requirements.
  - HDFS is not suitable for applications that need low latency, random access, or multiple writers.