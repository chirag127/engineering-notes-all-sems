HDFS stands for Hadoop Distributed File System. It is a distributed file system designed to run on commodity hardware and to store large amounts of data. HDFS stores data in a distributed manner by dividing it into small pieces called blocks and storing them on different nodes in the cluster. Each block has a default size of 128 MB, which can be configured in the hdfs-site.xml file. HDFS also replicates each block across multiple nodes to ensure fault tolerance and high availability.

The following diagram illustrates the basic architecture of HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Metadata       |    |  Block 1        |    |  Block 1        |
|  (File name,    |    |  Block 2        |    |  Block 2        |
|  block ID,      |    |  Block 3        |    |  Block 3        |
|  location, etc.)|    |  ...            |    |  ...            |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Heartbeat      |<-- |  Heartbeat      |    |  Heartbeat      |<--+
|  (Health check) |    |  (Health check) |    |  (Health check) |   |
|                 |    |                 |    |                 |   |
+-----------------+    +-----------------+    +-----------------+   |
|                 |    |                 |    |                 |   |
|  Block report   |<-- |  Block report   |    |  Block report   |<--+
|  (Block list)   |    |  (Block list)   |    |  (Block list)   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The NameNode is the master node that manages the file system metadata, such as file names, block IDs, locations, permissions, etc. It also coordinates the data access and replication among the DataNodes. The NameNode communicates with the DataNodes through heartbeat messages and block reports. The heartbeat messages are used to check the health and availability of the DataNodes, while the block reports are used to update the block locations and status on the NameNode.

The DataNodes are the worker nodes that store the actual data blocks on their local disks. They also perform read and write operations on the blocks as instructed by the NameNode or the clients. The DataNodes send heartbeat messages and block reports to the NameNode periodically to inform it of their status and the blocks they have. The DataNodes also replicate the blocks to other DataNodes as per the replication factor and the replica placement policy. The replication factor is the number of copies of each block that are stored in the cluster, and the replica placement policy is the algorithm that decides where to place the replicas to ensure data reliability and performance.