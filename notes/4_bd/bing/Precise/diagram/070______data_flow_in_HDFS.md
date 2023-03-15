#### Data flow in HDFS

Here is an ASCII diagram that illustrates the data flow in HDFS:

```
Client
   |
   | write request
   v
NameNode
   |
   | block locations
   v
Client
   |
   | write data
   v
DataNode 1
   |
   | replicate data
   v
DataNode 2
   |
   | replicate data
   v
DataNode 3
```

When a client wants to write data to HDFS, it sends a write request to the NameNode. The NameNode responds with the block locations where the data should be written. The client then writes the data to the first DataNode. The first DataNode replicates the data to the second DataNode, which in turn replicates the data to the third DataNode. This ensures that the data is stored redundantly across multiple DataNodes for fault tolerance.
