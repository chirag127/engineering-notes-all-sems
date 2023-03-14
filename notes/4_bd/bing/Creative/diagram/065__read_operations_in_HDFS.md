#### Read operations in HDFS

A read operation in HDFS involves the following steps:

1. The client contacts the NameNode and requests the locations of the blocks that make up the file to be read. The NameNode responds with the list of DataNodes that store the replicas of each block. The list is sorted by the network distance from the client to the DataNodes.
2. The client contacts the closest DataNode for the first block of the file and establishes a data stream. The DataNode sends the data to the client. If the client wants to read the next block, it contacts the closest DataNode for that block and repeats the process.
3. The client reads the data from the DataNodes until the end of the file or an error occurs. The client then closes the data stream and releases the resources.

The following diagram illustrates the basic architecture of a read operation in HDFS using ASCII characters:

```
    +-----------------+        +-----------------+
    |    Client       |        |    NameNode     |
    +-----------------+        +-----------------+
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |---------------------->|  |  Request block locations
          |  |                       |  |
          |  |<----------------------|  |  Response with block locations
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  V                       |  |
    +-----------------+              |  |
    |    DataNode     |<-------------|  |
    +-----------------+              |  |
          |  |                       |  |
          |  |---------------------->|  |  Request data stream
          |  |                       |  |
          |  |<----------------------|  |  Response with data stream
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  V                       |  |
    +-----------------+              |  |
    |    DataNode     |<-------------|  |
    +-----------------+              |  |
          |  |                       |  |
          |  |---------------------->|  |  Request data stream
          |  |                       |  |
          |  |<----------------------|  |  Response with data stream
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          |  V                       |  |
    +-----------------+              |  |
    |    DataNode     |<-------------|  |
    +-----------------+              |  |
          |  |                       |  |
          |  |---------------------->|  |  Request data stream
          |  |                       |  |
          |  |<----------------------|  |  Response with data stream
          |  |                       |  |
          |  |                       |  |
          |  |                       |  |
          V  V                       V  V
```