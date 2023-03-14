Data replication in HDFS is the process of copying the data blocks of a file from one node to another for fault tolerance and high availability. The replication factor is the number of copies of each block that are stored in the cluster. The default replication factor is 3, which means that each block has one primary copy and two secondary copies. The primary copy is called the first replica, and the secondary copies are called the second and third replicas.

The following diagram illustrates the basic architecture of data replication in HDFS:

```
    +-----------------+       +-----------------+       +-----------------+
    | NameNode (NN)   |       | DataNode (DN1)  |       | DataNode (DN2)  |
    |-----------------|       |-----------------|       |-----------------|
    | Metadata        |       | Data blocks     |       | Data blocks     |
    | Replica map     |       | Replica reports |       | Replica reports |
    +-----------------+       +-----------------+       +-----------------+
          |  |  |                  |  |  |                  |  |  |
          |  |  +------------------+  |  +------------------+  |  |
          |  |                       |                       |  |  |
          |  +-----------------------+-----------------------+  |  |
          |                                                     |  |
          +-----------------------------------------------------+  |
                                                                   |
                                                                   |
                                                                   |
                                                             +-----------------+
                                                             | DataNode (DN3)  |
                                                             |-----------------|
                                                             | Data blocks     |
                                                             | Replica reports |
                                                             +-----------------+
```

The NameNode (NN) is the master node that manages the metadata of the file system, such as the file names, directories, permissions, and locations of the blocks. The NameNode also maintains a replica map that tracks the locations of the replicas of each block. The NameNode communicates with the DataNodes (DNs) that store the actual data blocks of the files. The DataNodes periodically send replica reports to the NameNode, informing it of the blocks they have and their health status.

When a client wants to write a file to HDFS, it first contacts the NameNode and requests a list of DataNodes that can store the blocks of the file. The NameNode allocates a pipeline of DataNodes for each block, and returns the list to the client. The client then writes the data to the first DataNode in the pipeline, which in turn writes the data to the second DataNode, and so on, until the block is replicated to all the DataNodes in the pipeline. The client then writes the next block to the next pipeline of DataNodes, and repeats the process until the file is complete. The client then notifies the NameNode that the file is closed, and the NameNode updates the metadata and the replica map accordingly.

When a client wants to read a file from HDFS, it first contacts the NameNode and requests the locations of the blocks of the file. The NameNode returns the list of DataNodes that have the replicas of the blocks. The client then contacts the closest DataNode and reads the data from it. If the DataNode is unavailable or corrupted, the client can contact another DataNode that has the same block, and read the data from it. The client then reads the next block from the next DataNode, and repeats the process until the file is complete.

The NameNode is responsible for ensuring that the replication factor of each block is maintained. If a DataNode fails or becomes corrupted, the NameNode detects the loss of the replicas and initiates the replication of the missing blocks to other DataNodes. The NameNode also balances the load of the cluster by moving the blocks from over-utilized DataNodes to under-utilized DataNodes. The NameNode can also change the replication factor of a file or a directory based on the user's request or the cluster's policy.