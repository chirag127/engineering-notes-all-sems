Data replication in HDFS is the process of copying the data blocks of a file from one HDFS service to another, or to a different storage system, for fault tolerance and data availability. The replication factor is the number of copies of each data block that are stored in the cluster. The default replication factor is three, which means that each block is replicated on three different nodes. The replication factor can be configured per file or per directory.

The following diagram shows how data replication works in HDFS:

#### Data replication in HDFS

```
+-----------------+     +-----------------+     +-----------------+
|    NameNode     |     |    DataNode 1   |     |    DataNode 2   |
|                 |     |                 |     |                 |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | | Block A     | |     | | Block A     | |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | | Block B     | |     | | Block B     | |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | | Block C     | |     | | Block C     | |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
       |                       +-----------------------+-----------------+
       |                                               |                 |
       |                                               |    DataNode 3   |
       |                                               |                 |
       |                                               | +-------------+ |
       |                                               | | Block A     | |
       |                                               | +-------------+ |
       |                                               | +-------------+ |
       |                                               | | Block B     | |
       |                                               | +-------------+ |
       |                                               | +-------------+ |
       |                                               | | Block C     | |
       |                                               | +-------------+ |
       |                                               |                 |
       +-----------------------------------------------+-----------------+
```

The steps involved in data replication are:

1. A client writes data to an HDFS file with a replication factor of three.
2. The NameNode retrieves the list of DataNodes using a replication target choosing algorithm. This list contains the DataNodes that will store the replicas of the data blocks.
3. The client writes data to the first DataNode in the list. The first DataNode starts receiving the data in small packets and stores each packet in a temporary buffer.
4. The first DataNode forwards the data packets to the second DataNode in the list. The second DataNode does the same as the first DataNode, storing the packets in a buffer and forwarding them to the third DataNode.
5. The third DataNode stores the data packets in a buffer and sends an acknowledgement to the second DataNode, which in turn sends an acknowledgement to the first DataNode, which in turn sends an acknowledgement to the client.
6. The client continues to write data to the first DataNode until the block is full or the file is closed. The DataNodes flush the data packets from the buffer to the disk and create the block file.
7. The client repeats the same process for the next block of the file, until the file is complete. The NameNode updates the metadata of the file and the blocks, and maintains the mapping of blocks to DataNodes.