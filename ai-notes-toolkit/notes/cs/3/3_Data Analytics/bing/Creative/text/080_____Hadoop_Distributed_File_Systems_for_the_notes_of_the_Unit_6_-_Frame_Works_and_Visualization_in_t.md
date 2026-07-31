### Hadoop Distributed File Systems

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters .
- HDFS splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is designed to handle large data sets running on commodity hardware, and to tolerate hardware failures .
- HDFS employs a NameNode and DataNode architecture to implement the distributed file system .
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in the form of blocks.
  - A file in HDFS is split into one or more blocks, and each block is replicated on a fixed number of DataNodes, as specified by the replication factor.
  - NameNode maintains the metadata of the file system, such as the file and block locations, permissions, etc., in memory.
  - DataNode periodically sends a report of the blocks it is hosting to the NameNode, called a block report.
  - NameNode also receives heartbeats from DataNodes to monitor their status and performance.
  - If a DataNode fails or becomes unreachable, the NameNode detects it and replicates the blocks hosted by that DataNode to other DataNodes, to maintain the desired replication factor.
  - If the NameNode fails, the file system becomes inaccessible, unless a secondary NameNode or a standby NameNode is configured to take over the role of the primary NameNode.