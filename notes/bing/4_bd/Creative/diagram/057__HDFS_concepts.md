HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

HDFS has the following design concepts:

- Blocks: HDFS is a block-structured file system. Each file is broken into blocks of fixed size, usually 128 MB, which are stored across various data nodes on the cluster. Each block is replicated multiple times, by default three times, for fault tolerance.
- NameNode: NameNode is the master node that manages the metadata of the file system, such as the file names, directories, permissions, and locations of the blocks. NameNode also performs operations such as opening, closing, and renaming files and directories. NameNode is a single point of failure in HDFS, so it is usually configured with a secondary or standby NameNode for backup and recovery.
- DataNodes: DataNodes are the worker nodes that store and serve the blocks of data. DataNodes also perform tasks such as block creation, deletion, replication, and verification. DataNodes communicate with the NameNode and report the status of the blocks they are holding.

#### HDFS concepts

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    | Secondary       |    |    Client       |
|                 |    | NameNode        |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Block 1      |    |    Block 1      |    |    Block 1      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Block 2      |    |    Block 2      |    |    Block 3      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Block 3      |    |    Block 4      |    |    Block 4      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```