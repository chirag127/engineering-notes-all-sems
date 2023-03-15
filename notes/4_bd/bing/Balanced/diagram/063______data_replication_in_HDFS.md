Data replication in HDFS is the process of creating and maintaining multiple copies of the same data blocks across different nodes in a cluster. This is done for fault tolerance and high availability of data. The replication factor is the number of copies of each data block that are stored in HDFS. The default replication factor is 3, which means that each block is replicated on three different nodes. The replication factor can be configured per file or per directory.

Here is a diagram that illustrates the data replication in HDFS:

#### Data replication in HDFS

```
+-----------------+    +-----------------+    +-----------------+
|    NameNode     |    |    DataNode 1   |    |    DataNode 2   |
|                 |    |                 |    |                 |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | | Block A     | |    | | Block A     | |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | | Block B     | |    | | Block B     | |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | | Block C     | |    | | Block C     | |
|                 |    | +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+    +-----------------+
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
        |                       +-----------------------+
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
        +-----------------------+-----------------------+
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
        +-----------------+    +-----------------+    +-----------------+
        |    DataNode 3   |    |    DataNode 4   |    |    DataNode 5   |
        |                 |    |                 |    |                 |
        | +-------------+ |    | +-------------+ |    | +-------------+ |
        | | Block A     | |    | | Block B     | |    | | Block C     | |
        | +-------------+ |    | +-------------+ |    | +-------------+ |
        |                 |    |                 |    |                 |
        +-----------------+    +-----------------+    +-----------------+
```

In this diagram, the NameNode is the master node that manages the metadata of the files and blocks, such as their locations, sizes, permissions, etc. The DataNodes are the slave nodes that store the actual data blocks. The NameNode communicates with the DataNodes to assign and monitor the replication of the blocks. The client is the user or application that interacts with the HDFS to read or write data.

The diagram shows an example of a file that is divided into three blocks: A, B, and C. Each block has a replication factor of 3, which means that there are three copies of each block stored on different DataNodes. The NameNode decides which DataNodes to store the blocks on, based on factors such as network bandwidth, disk space, load balancing, etc. The NameNode also maintains a mapping of the blocks to the DataNodes, so that it can locate the blocks when the client requests them.

The diagram also shows how the client writes data to the HDFS. The client first contacts the NameNode and requests to create a file. The NameNode allocates a unique file ID and returns it to the client. The client then asks the NameNode for a list of DataNodes where the first block of the file can be stored. The NameNode returns a list of three DataNodes, such as Data