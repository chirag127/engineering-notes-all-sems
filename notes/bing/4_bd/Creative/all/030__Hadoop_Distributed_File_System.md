#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a file system that provides scalable, reliable, and fault-tolerant storage for large-scale data processing applications.
- HDFS is designed to run on clusters of commodity hardware, and can store petabytes of data across thousands of nodes.
- HDFS follows a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store the actual data blocks.
- HDFS exposes a POSIX-like interface for clients to interact with the file system, but does not support random writes or modifications of existing files.
- HDFS splits large files into fixed-size blocks (typically 128 MB or 256 MB), and distributes them across the DataNodes in the cluster. Each block is replicated on multiple DataNodes (default replication factor is 3) for fault tolerance and availability.
- HDFS supports rack-awareness, which means that it tries to place replicas of a block on different racks to reduce the impact of rack failures and network congestion.
- HDFS provides a command-line interface (CLI) and a web-based user interface (UI) for users to perform various operations on the file system, such as creating, deleting, copying, moving, and renaming files and directories, changing permissions and ownership, and checking the status and health of the cluster.
- HDFS also provides a Java API and a REST API for programmatic access to the file system.
- HDFS is compatible with various frameworks and tools for data processing, such as MapReduce, Spark, Hive, Pig, HBase, etc.
- HDFS is suitable for storing and processing large, structured, semi-structured, or unstructured data, such as text, images, videos, logs, sensor data, etc.
- HDFS is not suitable for low-latency or interactive applications, or for storing small files that cause metadata overhead and inefficient disk utilization.

A possible mnemonic to remember the key features of HDFS is:

**H**ighly scalable and reliable
**D**istributed and replicated blocks
**F**ault-tolerant and rack-aware
**S**imple and POSIX-like interface

A possible ascii diagram to illustrate the HDFS architecture is:

```
    +-----------------+             +-----------------+
    |    NameNode     |             |  Secondary NN   |
    | (Master Server) |             | (Backup Server) |
    +-----------------+             +-----------------+
    | Namespace &     |             | Checkpoint &    |
    | Metadata        | <---------> | Metadata Backup |
    +-----------------+             +-----------------+
          ^   ^
          |   |
          |   +-----------------+
          |                     |
          |                     v
+---------+---------+     +---------+---------+
|    DataNode 1    |     |    DataNode 2    |
| (Slave Server 1) |     | (Slave Server 2) |
+-------------------+     +-------------------+
| Block 1 (Replica)|     | Block 2 (Replica)|
| Block 3 (Replica)|     | Block 4 (Replica)|
| Block 5          |     | Block 6          |
+-------------------+     +-------------------+
          ^                     ^
          |                     |
          +---------------------+
          |
          v
+---------+---------+
|    DataNode 3    |
| (Slave Server 3) |
+-------------------+
| Block 1 (Replica)|
| Block 2 (Replica)|
| Block 3 (Replica)|
| Block 4 (Replica)|
+-------------------+
```