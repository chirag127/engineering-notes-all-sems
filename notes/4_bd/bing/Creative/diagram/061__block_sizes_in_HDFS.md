A block in HDFS is a fixed-size chunk of data that is stored in a distributed file system. The size of the block is configurable, but the default value is 128 MB  . HDFS breaks a large file into blocks and distributes them across different nodes in the cluster. Each block is replicated a certain number of times, depending on the replication factor, to ensure fault tolerance and high availability. The NameNode stores the metadata about the blocks, such as their location, size, and checksum. The DataNodes store the actual blocks and serve them to clients on request.

The following diagram illustrates the basic architecture of a block in HDFS:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   NameNode      |     |   DataNode 1    |     |   DataNode 2    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Metadata       |     |  Block 1        |     |  Block 1        |
|                 |     |  Block 2        |     |  Block 3        |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Block Map      |     |  Block Report   |     |  Block Report   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In this example, a file of size 384 MB is split into three blocks of size 128 MB each. The blocks are replicated twice and stored on two DataNodes. The NameNode maintains a block map that records the location of each block and its replicas. The DataNodes periodically send block reports to the NameNode to update the block map. The client can access the file by contacting the NameNode and getting the block locations, then reading the blocks from the DataNodes.