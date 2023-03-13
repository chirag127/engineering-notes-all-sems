#### Data flow in HDFS

HDFS stands for Hadoop Distributed File System, which is the storage layer of Hadoop that stores data in a distributed and reliable manner. HDFS splits a file into one or more blocks and stores them across a cluster of DataNodes. The NameNode manages the file system namespace and the metadata of the blocks. The client interacts with the NameNode and the DataNodes to perform read and write operations on HDFS files.

The following are the main steps involved in the data flow of HDFS read and write operations:

- **HDFS write operation:**

  1. The client creates the file by calling `create()` on the DistributedFileSystem (DFS) object, which is an instance of the FileSystem class that represents HDFS.
  2. DFS makes a remote procedure call (RPC) to the NameNode to create a new file in the file system namespace, with no blocks associated with it. The NameNode checks if the file already exists or if the parent directory is valid, and returns an exception if any of these conditions are not met.
  3. The client obtains a DFSOutputStream object to write data to the file. The DFSOutputStream splits the data into packets, which are stored in an internal queue called the data queue. The data queue is consumed by the DataStreamer, which is responsible for asking the NameNode to allocate new blocks and to locate DataNodes to store those blocks.
  4. The DataStreamer picks a list of suitable DataNodes to store a replica of each block. The list of DataNodes forms a pipeline, and the default replication factor is three. The DataStreamer streams the packets to the first DataNode in the pipeline, which stores the packet and forwards it to the second DataNode, and so on.
  5. The DFSOutputStream also maintains an internal queue of packets that are waiting to be acknowledged by the DataNodes, called the ack queue. A packet is removed from the ack queue only when it has been acknowledged by all the DataNodes in the pipeline.
  6. When the client has finished writing data, it calls `close()` on the DFSOutputStream. This flushes all the remaining packets to the DataNodes and waits for the acknowledgments. Then, the DFSOutputStream tells the NameNode that the file is complete. The NameNode commits the file creation operation to its persistent store.

- **HDFS read operation:**

  1. The client opens the file by calling `open()` on the DFS object, which returns a DFSInputStream object to read data from the file.
  2. The DFSInputStream communicates with the NameNode to obtain the list of blocks and their locations for the file. The locations of each block are ordered by their proximity to the client.
  3. The client reads data from the closest DataNode for each block. If the read fails or the DataNode is not available, the client tries the next DataNode in the list.
  4. The client can also perform seek operations to move to a different position in the file. This may involve contacting the NameNode again to get the new locations of the blocks.

A mnemonic to remember the data flow in HDFS is:

- Write: Create, Queue, Stream, Ack, Close
- Read: Open, Locate, Read, Seek