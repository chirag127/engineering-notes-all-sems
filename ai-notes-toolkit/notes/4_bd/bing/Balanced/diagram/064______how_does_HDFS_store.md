HDFS stands for Hadoop Distributed File System. It is a file system that stores large amounts of data across multiple nodes in a cluster. HDFS divides the data into fixed-size blocks and distributes them among the DataNodes. Each block is replicated on multiple DataNodes for fault tolerance. The NameNode is the master node that manages the file system namespace and the metadata of the blocks. The DataNodes are the slave nodes that store the actual data blocks and report to the NameNode.

#### How does HDFS store

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    NameNode     |      |    DataNode     |      |    DataNode     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  File metadata  |      |  Block 1 (128MB)|      |  Block 1 (128MB)|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Block location |      |  Block 2 (128MB)|      |  Block 2 (128MB)|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  File namespace |      |  Block 3 (128MB)|      |  Block 3 (128MB)|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```