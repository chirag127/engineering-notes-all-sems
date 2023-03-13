HDFS stands for Hadoop Distributed File System. It is a distributed file system designed to run on commodity hardware. It has a master/slave architecture, where a single NameNode manages the file system namespace and regulates access to files by clients, and a number of DataNodes store the data blocks on the nodes that they run on. HDFS is highly fault-tolerant and scalable, and supports replication of data blocks across multiple DataNodes.

### HDFS

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Client       |      |    Client       |      |    Client       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+------------------+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       +----------------------+----------------------+------------------+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       v                      v                      v                  v
+-----------------+      +-----------------+      +-----------------+  +-----------------+
|                 |      |                 |      |                 |  |                 |
|    NameNode     |      |    DataNode     |      |    DataNode     |  |    DataNode     |
|                 |      |                 |      |                 |  |                 |
+-----------------+      +-----------------+      +-----------------+  +-----------------+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       +----------------------+----------------------+------------------+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       v                      v                      v                  v
+-----------------+      +-----------------+      +-----------------+  +-----------------+
|                 |      |                 |      |                 |  |                 |
|    File         |      |    Block 1      |      |    Block 2      |  |    Block 3      |
|                 |      |                 |      |                 |  |                 |
+-----------------+      +-----------------+      +-----------------+  +-----------------+
```

The above diagram illustrates the basic architecture of HDFS. A file is split into one or more blocks, and each block is stored on one or more DataNodes. The NameNode maintains the metadata of the file system, such as the file names, directories, permissions, and the locations of the blocks. The clients communicate with the NameNode to perform operations on the file system, such as creating, deleting, reading, or writing files. The clients also communicate with the DataNodes to read or write the data blocks. The NameNode and the DataNodes periodically exchange heartbeat and block report messages to monitor the health and status of the cluster.