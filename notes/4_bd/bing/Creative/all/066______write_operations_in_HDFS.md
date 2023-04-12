#### Write operations in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- To write data in HDFS, the client first interacts with the NameNode, which is the master node that manages the metadata and namespace of the file system.
- The NameNode grants permission to write data and provides the IP addresses of the DataNodes, which are the slave nodes that store the actual data blocks.
- The client then directly interacts with the DataNodes for writing data, following a pipeline mechanism that ensures fault tolerance and replication.
- The steps involved in a write operation in HDFS are as follows:

  1. The client calls the `create()` method of the DistributedFileSystem object, which is a wrapper over the FileSystem class that provides access to HDFS.
  2. The DistributedFileSystem object makes a remote procedure call (RPC) to the NameNode to create a new file in the file system's namespace, with no blocks associated with it.
  3. The NameNode checks if the file already exists, and if the client has the right permissions to create the file. If not, it throws an exception to the client.
  4. If the file creation is successful, the NameNode returns a success response to the DistributedFileSystem object, which returns an FSDataOutputStream object to the client. This object wraps a DFSOutputStream object, which is responsible for communicating with the DataNodes and writing the data packets.
  5. The client writes data to the FSDataOutputStream object, which is buffered internally by the DFSOutputStream object.
  6. The DFSOutputStream object splits the data into fixed-size packets, which are stored in a data queue. Each packet contains a sequence number, a checksum, and a portion of the data block.
  7. The DFSOutputStream object asks the NameNode for a list of suitable DataNodes to store the first block of the file. The list is sorted by network distance from the client.
  8. The NameNode returns the list of DataNodes to the DFSOutputStream object, which selects the first DataNode as the primary DataNode and the rest as secondary DataNodes. The primary DataNode is responsible for coordinating the write operation with the secondary DataNodes and sending an acknowledgment to the DFSOutputStream object.
  9. The DFSOutputStream object sends the first packet to the primary DataNode, which stores the packet in its memory and forwards it to the next DataNode in the pipeline. This process continues until the last DataNode in the pipeline receives the packet.
  10. The last DataNode sends an acknowledgment to the previous DataNode, which propagates it back to the primary DataNode. The primary DataNode then sends an acknowledgment to the DFSOutputStream object, which removes the packet from the data queue and sends the next packet.
  11. The DFSOutputStream object repeats steps 9 and 10 until all the packets for the first block are written. It then asks the NameNode for a new list of DataNodes for the next block and repeats the whole process until all the data is written.
  12. The client calls the `close()` method of the FSDataOutputStream object, which flushes the remaining packets to the DataNodes and tells them to finalize the block. The DataNodes then report to the NameNode that the block is completed.
  13. The NameNode updates the file's metadata with the block locations and the file's length and modification time. The file is now visible to other clients for reading.

- A possible mnemonic to remember the steps of a write operation in HDFS is:

  - **C**reate file with NameNode
  - **W**rite data to FSDataOutputStream
  - **S**plit data into packets
  - **A**sk NameNode for DataNodes
  - **P**ipeline data to DataNodes
  - **A**cknowledge data from DataNodes
  - **C**lose file with DataNodes and NameNode

- A possible ASCII diagram to illustrate the write operation in HDFS is:

```
  Client
    |
    | create()
    |
    v
DistributedFileSystem
    |
    | RPC
    |
    v
  NameNode
    |
    | <success>
    |
    v
DistributedFileSystem
    |
    | FSDataOutputStream
    |
    v
  Client
    |
    | write()
    |
    v
DFSOutputStream
    |
    | data queue
    |
    v
    | ask()
    |
    v

```
