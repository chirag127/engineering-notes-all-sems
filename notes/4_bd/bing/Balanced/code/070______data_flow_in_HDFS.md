#### Data flow in HDFS

HDFS stands for Hadoop Distributed File System, which is a scalable and reliable storage system for large data sets. HDFS stores data in blocks across multiple nodes in a cluster, and replicates each block for fault tolerance. HDFS also maintains metadata about the files and blocks, such as their locations, sizes, permissions, etc.

The data flow in HDFS involves two main operations: reading and writing data. The following is a brief overview of how these operations work in HDFS, based on the search results  .

- Reading data from HDFS:

  - The client opens the file it wishes to read by calling `open()` on the DistributedFileSystem (DFS) object, which is an instance of FileSystem that communicates with the HDFS namenode.
  - DFS makes a remote procedure call (RPC) to the namenode to get the list of blocks and their locations for the file. The namenode returns the information to the DFS object.
  - The DFS object returns a FSDataInputStream object to the client, which provides an input stream for reading data from HDFS.
  - The client calls `read()` on the FSDataInputStream object, which internally uses a DFSInputStream object to read data from the data nodes.
  - The DFSInputStream object contacts the closest data node that has a replica of the first block of the file, and requests to read the data.
  - The data node sends the data to the DFSInputStream object, which buffers the data and returns it to the FSDataInputStream object.
  - The FSDataInputStream object returns the data to the client, which can read the data from the input stream.
  - The client repeats the `read()` operation until it reaches the end of the block, then the DFSInputStream object contacts the next data node that has a replica of the next block, and so on, until the end of the file is reached.

- Writing data to HDFS:

  - The client creates the file by calling `create()` on the DFS object, which makes an RPC to the namenode to create a new file in the HDFS namespace, with no blocks associated with it.
  - The namenode performs various checks, such as the file name, permissions, quotas, etc., and returns a FSDataOutputStream object to the client, which provides an output stream for writing data to HDFS.
  - The client calls `write()` on the FSDataOutputStream object, which internally uses a DFSOutputStream object to write data to the data nodes.
  - The DFSOutputStream object splits the data into packets, which it writes to an internal queue, called the data queue. The data queue is consumed by the DataStreamer, which is responsible for asking the namenode to allocate new blocks and their locations, and for sending the packets to the data nodes.
  - The DataStreamer asks the namenode for a new block, and receives a list of data nodes that will host the replicas of the block. The list forms a pipeline, where the first data node is the closest to the client, and the last data node is the farthest.
  - The DataStreamer sends the packets to the first data node in the pipeline, which stores the packet and forwards it to the second data node, and so on, until the last data node is reached.
  - The data nodes send back acknowledgements to the DataStreamer, which are put into another queue, called the ack queue. The ack queue is consumed by the DFSOutputStream object, which verifies that the packets have been successfully written to the data nodes.
  - The DFSOutputStream object returns the number of bytes written to the FSDataOutputStream object, which returns it to the client.
  - The client repeats the `write()` operation until it finishes writing the data, then it calls `close()` on the FSDataOutputStream object, which flushes the remaining packets to the data nodes, and tells the namenode to mark the file as complete.