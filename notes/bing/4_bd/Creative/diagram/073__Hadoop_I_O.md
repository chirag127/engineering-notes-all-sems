Hadoop I/O is the process of reading and writing data from and to the Hadoop Distributed File System (HDFS), which is the storage layer of the Hadoop framework. HDFS is designed to store large amounts of data in a distributed and fault-tolerant manner across multiple nodes in a cluster. HDFS consists of two types of nodes: NameNode and DataNode. NameNode is the master node that manages the metadata of the file system, such as the file names, locations, permissions, etc. DataNode is the worker node that stores the actual data blocks of the files. Each file in HDFS is divided into fixed-size blocks (typically 64 MB or 128 MB) and replicated across multiple DataNodes for reliability. The default replication factor is 3, which means each block has three copies on different DataNodes.

The following diagram illustrates the basic architecture of HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Metadata       |    |  Data Blocks    |    |  Data Blocks    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  RPC Server     |    |  RPC Server     |    |  RPC Server     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  HTTP Server    |    |  HTTP Server    |    |  HTTP Server    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         |                    |                     |
         +--------------------+---------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |