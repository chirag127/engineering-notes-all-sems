#### Data replication in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- Data replication is the process of creating and maintaining multiple copies of the same data on different nodes for fault tolerance, load balancing, and high availability.
- HDFS follows a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes.
- The NameNode is responsible for managing the metadata of the file system, such as the file names, directories, permissions, and the locations of the data blocks on the DataNodes.
- The DataNodes are responsible for storing the actual data blocks of the files, and for performing read and write operations on them as instructed by the NameNode or the clients.
- HDFS divides each file into fixed-size blocks (typically 128 MB or 256 MB), and stores them on the DataNodes. Each block is replicated on a configurable number of DataNodes (default is 3) for fault tolerance.
- The NameNode maintains a mapping of each file to its blocks, and each block to its replicas on the DataNodes. This information is stored in memory and on disk in the NameNode.
- The NameNode also periodically receives heartbeat and block report messages from the DataNodes, which indicate their status and the list of blocks they store.
- The NameNode uses a replication policy to decide where to place the replicas of each block, based on factors such as the rack awareness, the available space, the network bandwidth, and the data locality.
- The rack awareness is a feature that allows the NameNode to know the physical location of each DataNode in terms of the rack or the network switch they are connected to. This helps to improve the data reliability and the network performance by minimizing the cross-rack data transfers.
- The NameNode tries to place the replicas of each block on different racks, so that if one rack fails, the data can still be accessed from another rack. The default policy is to place the first replica on the same node as the client, the second replica on a different node in the same rack, and the third replica on a node in a different rack.
- The NameNode also balances the load and the space utilization of the DataNodes by moving the blocks from one node to another, based on the cluster status and the administrator's commands.
- The NameNode also handles the failure and recovery of the DataNodes by detecting the missing heartbeats or block reports, and by re-replicating the under-replicated blocks on other available DataNodes.
- The NameNode also handles the addition and removal of the DataNodes by updating the metadata and by re-balancing the blocks accordingly.
- The NameNode also handles the corruption and deletion of the blocks by verifying the checksums and by re-replicating the corrupted or deleted blocks on other DataNodes.

A simple diagram of the data replication in HDFS is shown below:

```
    +---------+             +---------+             +---------+
    | Client  |             | NameNode|             | DataNode|
    +---------+             +---------+             +---------+
         |                      |                      |
         |  Write request      |                      |
         |--------------------->|                      |
         |                      |                      |
         |                      |  Allocate blocks     |
         |                      |--------------------->|
         |                      |                      |
         |                      |  Return block IDs    |
         |                      |<---------------------|
         |                      |                      |
         |  Write data to      |                      |
         |  first DataNode     |                      |
         |--------------------->|                      |
         |                      |                      |
         |                      |  Replicate data to   |
         |                      |  other DataNodes     |
         |                      |--------------------->|
         |                      |                      |
         |                      |  Acknowledge write   |
         |                      |<---------------------|
         |                      |                      |
         |  Return write status |                      |
         |<---------------------|                      |
         |                      |                      |
         |                      |                      |
         |  Read request        |                      |
         |--------------------->|                      |
         |                      |                      |
         |                      |  Locate blocks       |
         |                      |--------------------->|
         |                      |                      |
         |                      |  Return block IDs    |
         |                      |<---------------------|
         |                      |                      |
         |  Read data from      |                      |
         |  any DataNode        |                      |
         |--------------------->|                      |
         |                      |                      |
         |  Return read data    |                      |
         |<---------------------|                      |
         |                      |                      |
         |                      |