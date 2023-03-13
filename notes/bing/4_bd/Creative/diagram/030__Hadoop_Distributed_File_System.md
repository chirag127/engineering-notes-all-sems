Hadoop Distributed File System (HDFS) is a distributed file system that provides high-throughput access to large data sets across a cluster of nodes. HDFS consists of two main components: a NameNode and multiple DataNodes. The NameNode is the master node that manages the file system namespace and the metadata of the files and blocks. The DataNodes are the worker nodes that store the actual data in blocks and perform read and write operations as instructed by the NameNode. HDFS also supports replication and fault tolerance by creating multiple copies of each block and distributing them across different DataNodes.

#### Hadoop Distributed File System

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    NameNode     |      |    DataNode     |      |    DataNode     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Metadata       |      |  Block 1        |      |  Block 2        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Namespace      |      |  Block 3        |      |  Block 4        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Heartbeat      |<---->|  Heartbeat      |      |  Heartbeat      |<----+
|                 |      |                 |      |                 |     |
+-----------------+      +-----------------+      +-----------------+     |
|                 |      |                 |      |                 |     |
|  Block report   |<---->|  Block report   |      |  Block report   |<----+
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Client request |----->|  Client request |----->|  Client request |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```