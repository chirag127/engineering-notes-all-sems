#### Data flow in HDFS

HDFS stands for Hadoop Distributed File System, which is a scalable and reliable storage system for large-scale data processing. HDFS stores data in blocks across multiple nodes in a cluster, and provides fault tolerance, high availability, and parallel access.

The data flow in HDFS involves two main operations: read and write. The following points describe how these operations are performed in HDFS.

- **Write operation**: When a client wants to write data to HDFS, it follows these steps:

  1. The client calls the `create()` method on the `DistributedFileSystem` object, which is an instance of the HDFS file system abstraction.
  2. The `DistributedFileSystem` makes a remote procedure call (RPC) to the name node, which is the master node that maintains the metadata of the file system. The name node creates a new file in the file system namespace, with no blocks associated with it.
  3. The name node returns a response to the `DistributedFileSystem`, which gives a write token to the client. The write token is a permission to write data to the data nodes, which are the slave nodes that store the actual data blocks.
  4. The client splits the data into packets, which are then written to an internal queue called the `data queue`. The client also creates an empty queue called the `ack queue`, which will store the acknowledgments from the data nodes.
  5. The client asks the name node for a list of suitable data nodes to store the first block of the data. The name node returns a list of data nodes based on the replication factor, the rack awareness policy, and the load balancing policy.
  6. The client picks one data node from the list and sends the first packet of the data to it. The data node stores the packet and forwards it to the next data node in the list. This process continues until the last data node in the list receives the packet.
  7. The last data node sends an acknowledgment to the previous data node, which then sends an acknowledgment to its previous data node, and so on until the first data node sends an acknowledgment to the client. The client puts the acknowledgment in the `ack queue`.
  8. The client repeats steps 5 to 7 for the remaining packets of the first block. When the block is full, the client finalizes the block and sends a `blockReceived` message to the name node.
  9. The client repeats steps 5 to 8 for the remaining blocks of the data. When the data is complete, the client calls the `close()` method on the `DistributedFileSystem` object, which tells the name node that the file write is complete.

- **Read operation**: When a client wants to read data from HDFS, it follows these steps:

  1. The client calls the `open()` method on the `DistributedFileSystem` object, which is an instance of the HDFS file system abstraction.
  2. The `DistributedFileSystem` makes a remote procedure call (RPC) to the name node, which is the master node that maintains the metadata of the file system. The name node returns the metadata of the file, such as the block locations, the block sizes, and the block IDs.
  3. The client caches the metadata of the file and contacts the closest data node that has a copy of the first block of the data. The client can use the rack awareness policy to choose the closest data node based on the network topology.
  4. The data node sends the data of the first block to the client. The client verifies the checksum of the data to ensure its integrity. If the checksum does not match, the client reports the error to the name node and tries another data node.
  5. The client repeats step 4 for the remaining blocks of the data. When the data is complete, the client closes the file stream.

- **Mnemonics and learning tricks**: Here are some possible mnemonics and learning tricks to remember the data flow in HDFS:

  - For the write operation, remember the acronym **CSDNA**: Create, Split, Data queue, Name node, Ack queue.
  - For the read operation, remember the acronym **OCVD**: Open, Cache, Verify, Data node.
  - For the data nodes, remember that they are arranged in a **pipeline** for the write operation and a **choice** for the read operation.