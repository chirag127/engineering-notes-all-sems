Write operations in HDFS are the process of storing data blocks in the distributed file system. The basic steps of write operations in HDFS are as follows:

1. The client contacts the namenode and requests to create a new file in the HDFS namespace.
2. The namenode checks if the file already exists and if the client has the permission to write the file. If the checks pass, the namenode makes a record of the new file; otherwise, it throws an IOException to the client.
3. The client gets a FSDataOutputStream object from the DistributedFileSystem to start writing data to the file. The client writes the data in packets and puts them in a data queue. The data queue is consumed by a DataStreamer thread that is responsible for asking the namenode for a list of datanodes to store the replicas of each block.
4. The namenode returns a pipeline of datanodes for each block. The DataStreamer streams the packets to the first datanode in the pipeline, which stores the packet and forwards it to the second datanode, and so on. The last datanode in the pipeline sends an acknowledgment back to the previous datanode, which propagates it back to the DataStreamer.
5. The DataStreamer waits for the acknowledgment of all the packets for a block before sending the next block to the namenode. If the acknowledgment is not received within a timeout, or an error occurs, the DataStreamer removes the failed datanode from the pipeline and asks the namenode for a new pipeline to continue with the write operation.
6. When the client finishes writing the data, it calls the close() method on the FSDataOutputStream object. This flushes all the remaining packets to the datanode pipeline and waits for the acknowledgments. Then it tells the namenode that the file write is complete. The namenode commits the file creation operation to its persistent store.

The following diagram illustrates the basic architecture of a write operation in HDFS using ASCII characters:

```
+---------+    +-----------+    +-----------+    +-----------+
| Client  |    | NameNode  |    | DataNode1 |    | DataNode2 |
+---------+    +-----------+    +-----------+    +-----------+
     |              |                |                |
     | create file  |                |                |
     |------------->|                |                |
     |              |                |                |
     |    <OK>      |                |                |
     |<-------------|                |                |
     |              |                |                |
     | write block  |                |                |
     |------------->|                |                |
     |              |                |                |
     |  pipeline    |                |                |
     |<-------------|                |                |
     |              |                |                |
     |   packet1    |                |                |
     |------------->|                |                |
     |              |   packet1      |                |
     |              |--------------->|                |
     |              |                |   packet1      |
     |              |                |--------------->|
     |              |                |                |
     |              |                |     ack1       |
     |              |                |<---------------|
     |              |     ack1       |                |
     |              |<---------------|                |
     |     ack1     |                |                |
     |<-------------|                |                |
     |              |                |                |
     |   packet2    |                |                |
     |------------->|                |                |
     |              |   packet2      |                |
     |              |--------------->|                |
     |              |                |   packet2      |
     |              |                |--------------->|
     |              |                |                |
     |              |                |     ack2       |
     |              |                |<---------------|
     |              |     ack2       |                |
     |              |<---------------|                |
     |     ack2     |                |                |
     |<-------------|                |                |
     |              |                |                |
     |   close()    |                |                |
     |------------->|                |                |
     |              |                |                |
     |  file done   |                |                |
     |<-------------|                |                |
     |              |                |                |
```