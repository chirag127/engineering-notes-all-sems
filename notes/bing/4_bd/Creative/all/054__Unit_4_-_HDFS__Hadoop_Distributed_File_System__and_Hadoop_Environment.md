## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system that is designed to store and process large amounts of data across a cluster of machines.
- HDFS is one of the core components of the Hadoop ecosystem, which also includes MapReduce, YARN, Hive, Pig, Spark, etc.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the metadata of the file system, such as the file names, directories, permissions, locations of blocks, etc.
- The DataNodes are responsible for storing the actual data blocks of the files, and for serving read and write requests from the clients.
- HDFS splits the files into fixed-size blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes, with replication for fault tolerance.
- HDFS provides a high-level abstraction of the file system to the clients, who can access the files using a standard interface (such as Java API, command-line, web browser, etc.).
- HDFS is optimized for batch processing of large and sequential data, rather than random and interactive access.
- HDFS supports the write-once-read-many (WORM) model, where the files are appended to but not modified after creation.
- HDFS is designed to run on commodity hardware, which means that it can handle hardware failures and network partitions gracefully.

Some of the advantages of HDFS are:

- Scalability: HDFS can scale to thousands of nodes and petabytes of data, by adding more machines to the cluster.
- Reliability: HDFS can tolerate the loss of some DataNodes or blocks, by replicating the data across multiple nodes and by performing checksums to detect corruption.
- Availability: HDFS can provide high availability of the NameNode, by using a secondary or standby NameNode that can take over in case of failure.
- Cost-effectiveness: HDFS can run on low-cost hardware, which reduces the total cost of ownership and maintenance.
- Compatibility: HDFS can integrate with various tools and frameworks in the Hadoop ecosystem, such as MapReduce, Hive, Pig, Spark, etc.

Some of the disadvantages of HDFS are:

- Latency: HDFS has a high latency for read and write operations, due to the network overhead and the replication factor.
- Overhead: HDFS consumes a lot of disk space and memory for storing the metadata and the blocks, which reduces the effective storage capacity and performance of the cluster.
- Limitations: HDFS has some limitations in terms of the file size, the number of files, the number of concurrent clients, the append operations, etc.

Some of the applications of HDFS are:

- Data warehousing: HDFS can store and process large volumes of structured and unstructured data, such as logs, transactions, social media, etc.
- Data analytics: HDFS can support various types of analytics, such as batch, real-time, streaming, machine learning, etc., by using different tools and frameworks in the Hadoop ecosystem.
- Data backup: HDFS can provide a reliable and cost-effective backup solution for the data, by replicating and archiving the data across multiple nodes and locations.
- Data archive: HDFS can store and preserve the data for a long time, by using compression and encryption techniques, and by applying retention and deletion policies.

Some of the mnemonics and learning tricks for HDFS and Hadoop Environment are:

- HDFS: Hadoop Distributed File System
  - H: Huge files
  - D: Distributed blocks
  - F: Fault tolerant replication
  - S: Scalable cluster
- NameNode: Master node that manages the metadata
  - N: Name of the files and directories
  - A: Access permissions and ownership
  - M: Map of the blocks and their locations
  - E: Edit log and fsimage of the file system
- DataNode: Slave node that stores the data blocks
  - D: Data blocks of the files
  - A: Acknowledgement of the write requests
  - T: Transfer of the blocks to other nodes
  - A: Availability report to the NameNode
- Block: Fixed-size unit of data storage
  - B: Big size (128 MB or 256 MB)
  - L: Location on the DataNodes
  - O: Offset within the file
  - C: Checksum for error detection
  - K: Key for identification
- Replication: Process of copying the blocks across multiple DataNodes
  - R: Redundancy for fault tolerance
  -