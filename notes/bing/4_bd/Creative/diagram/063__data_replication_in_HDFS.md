Data replication in HDFS is the process of copying the data blocks of a file from one node to another in a cluster for fault tolerance and high availability. The number of copies of each block is determined by the replication factor, which can be configured globally or per file. The default replication factor is 3, which means that each block has 3 replicas on different nodes.

The following diagram illustrates the basic architecture of data replication in HDFS using ASCII characters:

    +-----------------+    +-----------------+    +-----------------+
    | NameNode        |    | DataNode 1      |    | DataNode 2      |
    |                 |    |                 |    |                 |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    | | File1       | |    | | Block1      | |    | | Block1      | |
    | | Replication | |    | | Replication | |    | | Replication | |
    | | Factor: 3   | |    | | Factor: 3   | |    | | Factor: 3   | |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    |                 |    |                 |    |                 |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    | | File2       | |    | | Block2      | |    | | Block2      | |
    | | Replication | |    | | Replication | |    | | Replication | |
    | | Factor: 2   | |    | | Factor: 2   | |    | | Factor: 2   | |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    |                 |    |                 |    |                 |
    +-----------------+    +-----------------+    +-----------------+
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
              |                     |                     |
    +-----------------+    +-----------------+    +-----------------+
    | DataNode 3      |    | DataNode 4      |    | DataNode 5      |
    |                 |    |                 |    |                 |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    | | Block1      | |    | | Block2      | |    | | Block3      | |
    | | Replication | |    | | Replication | |    | | Replication | |
    | | Factor: 3   | |    | | Factor: 2   | |    | | Factor: 1   | |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    |                 |    |                 |    |                 |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    | | Block3      | |    | | Block4      | |    | | Block4      | |
    | | Replication | |    | | Replication | |    | | Replication | |
    | | Factor: 1   | |    | | Factor: 2   | |    | | Factor: 2   | |
    | +-------------+ |    | +-------------+ |    | +-------------+ |
    |                 |    |                 |    |                 |
    +-----------------+    +-----------------+    +-----------------+

The NameNode is the master node that manages the metadata of the files and blocks, such as their locations, sizes, permissions, and replication factors. The DataNodes are the slave nodes that store the actual data blocks and report to the NameNode periodically. The NameNode is responsible for assigning the blocks to the DataNodes and balancing the load among them. The NameNode also handles the replication of the blocks according to the replication factor and the rack awareness policy, which tries to place the replicas on different racks for better reliability and performance. The NameNode also handles the failure of the DataNodes and the recovery of the blocks.

The diagram shows an example of how the files and blocks are distributed and replicated across the DataNodes. File1 has a