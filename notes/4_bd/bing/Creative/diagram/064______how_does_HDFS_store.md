HDFS (Hadoop Distributed File System) is a distributed file system that stores large amounts of data across multiple nodes in a cluster. It provides high availability, fault tolerance, scalability, and parallel processing of data.

HDFS stores data in the form of blocks, which are fixed-sized chunks of data. Each block is replicated on multiple DataNodes, which are the nodes that store and serve the data. The default block size is 128 MB, but it can be configured according to the needs of the application.

The NameNode is the master node that manages the file system namespace and the metadata of the blocks. It keeps track of the location, size, and replication factor of each block. It also handles the operations on files and directories, such as opening, closing, renaming, and deleting.

The DataNodes communicate with the NameNode and report the status of the blocks they store. They also perform the read and write operations on the blocks as requested by the clients or the NameNode.

The following diagram shows a simplified representation of how HDFS stores data:

```
    +-----------------+     +-----------------+     +-----------------+
    |    NameNode    |     |    DataNode 1   |     |    DataNode 2   |
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  File1 (256 MB) |     |  Block1 (128 MB)|     |  Block1 (128 MB)|
    |  - Block1       |     |  Block2 (128 MB)|     |  Block2 (128 MB)|
    |  - Block2       |     |  Block3 (128 MB)|     |  Block3 (128 MB)|
    |                 |     |                 |     |                 |
    |  File2 (384 MB) |     |  Block4 (128 MB)|     |  Block4 (128 MB)|
    |  - Block4       |     |  Block5 (128 MB)|     |  Block5 (128 MB)|
    |  - Block5       |     |  Block6 (128 MB)|     |  Block6 (128 MB)|
    |  - Block6       |     |                 |     |                 |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
```