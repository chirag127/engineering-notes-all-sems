#### Data replication in HDFS

Here is an ASCII diagram that illustrates the data replication process in Hadoop Distributed File System (HDFS):

```
+-----------------+     +-----------------+     +-----------------+
|  DataNode 1     |     |  DataNode 2     |     |  DataNode 3     |
|                 |     |                 |     |                 |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  | Block A   |  |     |  | Block A   |  |     |  | Block A   |  |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In HDFS, data is stored in blocks and replicated across multiple DataNodes for fault tolerance. In this example, Block A is replicated across DataNode 1, DataNode 2, and DataNode 3. This ensures that even if one or two of the DataNodes fail, the data is still available on the remaining DataNode(s).