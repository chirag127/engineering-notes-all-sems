#### Block abstraction in HDFS

- HDFS is a distributed file system that stores large files across multiple machines.
- HDFS breaks down each file into smaller units called blocks, which are stored on different nodes in the cluster.
- Each block has a fixed size, typically 64 MB or 128 MB, which is configurable by the administrator.
- Blocks are the smallest unit of data that can be read or written by HDFS.
- Blocks are also replicated across multiple nodes for fault tolerance and high availability.
- The default replication factor is 3, which means each block has 3 copies on different nodes.
- HDFS maintains a metadata file called the namespace, which records the file names, directories, permissions, and the locations of the blocks for each file.
- The namespace is stored on a special node called the NameNode, which is the master node of the cluster.
- The NameNode also manages the block allocation, replication, and recovery.
- The other nodes in the cluster are called DataNodes, which store the actual blocks and serve read and write requests from clients.
- The DataNodes periodically send heartbeat and block report messages to the NameNode, to report their status and the blocks they have.
- The NameNode uses these messages to keep track of the cluster health and the block locations.
- If a DataNode fails or a block becomes corrupted, the NameNode can initiate the replication of the missing or corrupted block from another DataNode that has a copy of the block.
- The NameNode also balances the load of the cluster by moving blocks from one DataNode to another, if needed.

- A simple mnemonic to remember the block abstraction in HDFS is:

  - **B**reak files into **B**locks
  - **R**eplicate **B**locks across **R**acks
  - **S**tore metadata in the **S**ingle NameNode
  - **M**anage blocks with heart**B**eat and block report
  - **R**ecover and balance blocks with **R**eplication and **R**ebalancing