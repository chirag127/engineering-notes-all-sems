 Here is the markdown content for the given topic:

### Data Replication for HDFS (Hadoop Distributed File System)

1. Data replication is a key feature of HDFS. It provides fault tolerance by replicating the blocks of data on multiple DataNodes.
2. The default replication factor is 3, i.e. every block is replicated to 3 DataNodes.
3. Replication ensures availability of data and protection against DataNode failures. If one or more DataNodes fail, the data will still be available on the remaining replicas.
4. The NameNode keeps track of which blocks are replicated on which DataNodes. When a client retrieves a block from DataNode, the NameNode returns locations of all the replicas of that block. The client contacts a replica Node directly to read or write data.
5. When a DataNode fails, the NameNode detects the failure and performs necessary replication tasks to restore the target replication factor for files stored on that DataNode.
6. Over replicating leads to wasted storage space and under replicating leads to less fault tolerance. Replication factor can be customized based on the storage capacity and fault tolerance requirements of the application.

The above points cover the key aspects of data replication in HDFS. The replication factor and replication tasks on DataNode failures ensure high availability and fault tolerance which are essential for a distributed file system like HDFS.