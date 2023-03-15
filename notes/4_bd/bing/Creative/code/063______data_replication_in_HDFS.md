#### Data replication in HDFS

Data replication in HDFS is the process of creating and maintaining multiple copies of the same data blocks across different nodes in a cluster. This is done for fault tolerance, load balancing, and data availability. The replication factor is the number of copies of each block that are stored in the cluster. The default replication factor is 3, but it can be changed per file or per directory.

The data replication in HDFS follows these steps:

- A client writes data to an HDFS file using a write operation.
- The client contacts the NameNode and requests to create a new file with a given replication factor.
- The NameNode checks if the file already exists, if there is enough space in the cluster, and if the client has the permission to write the file.
- If the file creation is successful, the NameNode returns a list of DataNodes that can store the first block of the file. The list is generated using a replication target choosing algorithm that considers the rack awareness, the network topology, the node capacity, and the node load.
- The client writes the data to the first DataNode in the list. The first DataNode starts receiving the data in small packets and stores them in its local disk.
- The first DataNode also forwards the data packets to the second DataNode in the list. The second DataNode does the same as the first DataNode and forwards the data packets to the third DataNode in the list. This way, a pipeline of data transfer is established among the DataNodes.
- When the first block is filled, the client contacts the NameNode again and requests a new list of DataNodes for the next block. The process repeats until all the blocks of the file are written and replicated.
- The client closes the file after writing all the data. The NameNode updates the file metadata and the block locations in its namespace.

The data replication in HDFS can be illustrated by the following diagram:

```
  Client
    |
    | write file
    V
  NameNode
    |
    | return DataNodes for block 1
    V
  DataNode 1 -> DataNode 2 -> DataNode 3
    |             |             |
    | write block 1             |
    |                           |
    | return DataNodes for block 2
    V
  DataNode 4 -> DataNode 5 -> DataNode 6
    |             |             |
    | write block 2             |
    |                           |
    | return DataNodes for block 3
    V
  DataNode 7 -> DataNode 8 -> DataNode 9
    |             |             |
    | write block 3             |
    |                           |
    | close file
    V
  NameNode
    |
    | update metadata
    V
  HDFS file
```