Hadoop Distributed File System (HDFS) is a distributed file system that runs on commodity hardware and provides high-throughput access to large data sets. HDFS consists of two types of nodes: NameNode and DataNode. NameNode is the master node that manages the file system namespace and the metadata of the files and directories. DataNode is the slave node that stores the actual data blocks of the files. HDFS splits files into fixed-size blocks (typically 64 MB or 128 MB) and distributes them across the DataNodes in the cluster. HDFS also replicates each block on multiple DataNodes (default replication factor is 3) to ensure fault tolerance and availability.

The following diagram illustrates the basic architecture of HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Metadata       |    |  Block 1        |    |  Block 1        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |  Block 2        |    |  Block 2        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |  Block 3        |    |  Block 3        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |  Block 4        |    |  Block 4        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```