#### Data replication in HDFS

- HDFS is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- Data replication is a technique that creates multiple copies of the same data block and stores them on different nodes for fault tolerance and high availability.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store the actual data blocks.
- When a file is written to HDFS, it is split into fixed-size blocks (default 128 MB) and each block is replicated to a number of DataNodes (default 3) based on the replication factor.
- The NameNode decides which DataNodes to store the replicas of each block, and maintains a mapping of file names, block IDs, and DataNode locations.
- The NameNode also periodically receives heartbeat and block report messages from the DataNodes, which indicate the health and status of each DataNode and the blocks they store.
- The NameNode uses a replication policy to balance the load and ensure the reliability of the data across the cluster. The policy considers factors such as rack awareness, node capacity, node availability, and block placement.
- The NameNode can initiate replication or deletion of blocks to maintain the desired replication factor and free up space on the DataNodes.
- The DataNodes are responsible for serving read and write requests from the clients, and performing block operations such as creation, deletion, and replication as instructed by the NameNode.
- The DataNodes also communicate with each other to transfer blocks for replication or recovery purposes.
- The clients interact with the NameNode to obtain the metadata of the files and the locations of the blocks, and then directly communicate with the DataNodes to read or write the data blocks.