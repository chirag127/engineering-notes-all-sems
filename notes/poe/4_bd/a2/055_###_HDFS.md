 Here is the content written in markdown format about HDFS:

### HDFS

HDFS stands for Hadoop Distributed File System. It is the primary storage system used by Hadoop applications. Some key points about HDFS are:

- HDFS is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS provides high throughput access to application data and is suitable for applications that have large data sets.
- HDFS is designed to scale to thousands of nodes in a single cluster.

**Architecture:** HDFS has a master-slave architecture. The main components are:

- NameNode: The master node that manages the file system namespace and regulates access to files by clients.
- DataNodes: Slave nodes that store the blocks and serve read/write requests from clients.

** Some Mnemonics/Tricks to remember: **

- The blocks of a file are replicated for fault tolerance. The default replication factor is 3.
- The blocks are large (typically 128MB) for efficient streaming of data.
- The NameNode is a single point of failure in HDFS. It keeps the file system metadata in memory and checkpoints it to disk.
- DataNodes send heartbeat messages to the NameNode periodically. If the NameNode does not receive a heartbeat from a DataNode within a certain time interval, it considers that DataNode to have failed.

**Advantages**:

- Fault Tolerance: HDFS is highly fault-tolerant due to replication of data blocks across multiple DataNodes.
- Scalability: HDFS is designed to scale to large clusters with tens of thousands of nodes.
- Streaming Access: HDFS supports streaming access of large files at high throughput.
- Low Cost: HDFS is built from commodity hardware and has low cost.

**Disadvantages**:

- Not suitable for low latency data access. HDFS is optimized for throughput rather than latency.
- Limited File Size: HDFS has a limited file size of a few petabytes.
- Single Point of Failure: The NameNode is a single point of failure in HDFS. If the NameNode goes down, the file system goes offline.

**Applications**: HDFS is well suited for applications that have large data sets and require streaming access. Some examples are:

- Search engines indexing web pages.
- scientific applications that generate large data sets (e.g. physics simulations).
- Log processing applications.

[Detailed diagrams and examples can be added here if required.]