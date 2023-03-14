#### Data flow in HDFS

HDFS stands for Hadoop Distributed File System, which is a distributed file system designed to run on commodity hardware. It provides high throughput access to large data sets and is suitable for applications that have streaming data access. HDFS stores data in blocks across multiple nodes in a cluster, and replicates each block for fault tolerance. HDFS also maintains metadata about the files and blocks, such as their locations, sizes, permissions, etc.

The data flow in HDFS involves two types of operations: read and write. In both cases, the client interacts with the NameNode and the DataNodes to perform the data transfer. The NameNode is the master node that manages the file system namespace and the metadata. The DataNodes are the slave nodes that store the actual data blocks and serve read and write requests from the clients.

The following are the steps involved in the data flow for each operation:

- **Read operation:**

  1. The client opens the file it wishes to read by calling `open()` on the FileSystem object, which for HDFS is an instance of DistributedFileSystem. This object communicates with the NameNode to obtain the file information, such as the block locations, the block sizes, the replication factor, etc.
  2. The DistributedFileSystem returns an FSDataInputStream object to the client, which is a wrapper over the DFSInputStream object. The DFSInputStream splits the file into one or more chunks, each chunk corresponding to a single block of the file.
  3. For each chunk, the DFSInputStream queries the NameNode for the list of DataNodes that have a copy of that block. The list is sorted by the network distance from the client. The DFSInputStream then connects to the closest DataNode and requests the transfer of the block.
  4. The DataNode sends the block data to the DFSInputStream, which buffers the data in a local buffer. The client can then read the data from the FSDataInputStream as a normal input stream. The DFSInputStream also verifies the checksum of the data to detect any corruption.
  5. If the DFSInputStream encounters an error while reading the data from a DataNode, such as a network failure or a checksum mismatch, it reports the error to the NameNode and tries the next DataNode in the list. The NameNode may also mark the faulty DataNode as dead and exclude it from the list of replicas.
  6. The client can also seek to a different position in the file and read from there. The DFSInputStream will locate the corresponding block and DataNode and repeat the steps 3 to 5.
  7. When the client finishes reading the file, it calls `close()` on the FSDataInputStream, which closes the underlying DFSInputStream and releases any resources.

- **Write operation:**

  1. The client creates the file it wishes to write by calling `create()` on the FileSystem object, which for HDFS is an instance of DistributedFileSystem. This object communicates with the NameNode to create a new file in the file system namespace and obtain a unique file ID. The client also specifies the replication factor, the block size, and other file attributes.
  2. The DistributedFileSystem returns an FSDataOutputStream object to the client, which is a wrapper over the DFSOutputStream object. The DFSOutputStream is responsible for splitting the file into blocks and sending them to the DataNodes.
  3. For the first block of the file, the DFSOutputStream asks the NameNode to choose a list of DataNodes that will host the replicas of the block. The list is sorted by the network distance from the client. The DFSOutputStream then connects to the first DataNode in the list and sends a packet containing the file ID, the block ID, and a portion of the block data. The packet also includes the checksum of the data for error detection.
  4. The first DataNode stores the packet in its local buffer and forwards it to the second DataNode in the list. The second DataNode does the same and forwards it to the third DataNode, and so on. This forms a pipeline of DataNodes that transfer the block data in parallel. The last DataNode in the pipeline sends an acknowledgment back to the previous DataNode, which propagates it back to the DFSOutputStream.
  5. The DFSOutputStream waits for the acknowledgment from the pipeline before sending the next packet. If the acknowledgment is not received within a timeout period, or if an error occurs in the pipeline, the DFSOutputStream reports the error to the NameNode and removes the faulty DataNode from the pipeline. The DFSOutputStream then resends the packet to the remaining