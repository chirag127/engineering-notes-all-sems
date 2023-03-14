 Here is the content in markdown format for the topic #### how does HDFS store:

#### How does HDFS store data?

- HDFS stores data in blocks of 128 MB (configurable) size.
- Data is replicated multiple times (typically 3 times) across different DataNodes for fault tolerance.
- The blocks of a file are typically stored on different racks for higher fault tolerance. This is known as rack-awareness.
- The NameNode acts as the master node and maintains the file system namespace and regulates access to files by clients.
- The DataNodes are slave nodes that store the blocks and serve read/write requests from clients.
- The architecture allows for streaming access of large files since the blocks are large and the networks have high throughput.

**Mnemonics:**
* HDFS blocks are big (128 MB), replicated, and rack-aware
* NameNode is the master, DataNodes are the slaves that store the blocks

**Advantages:**
* Fault tolerance via block replication
* Streaming access of large files
* Scalability - can store very large datasets (petabytes) by adding more DataNodes
* Low cost - commodity hardware can be used

**Disadvantages:**
* Not suitable for small files - can lead to inefficient usage of space
* Higher latency for small reads/writes compared to local filesystems
* Not POSIX compliant - cannot support concurrent writes to the same file

**Applications:**
* Hadoop ecosystem (MapReduce, Hive, Pig)
* Machine Learning with large datasets

[Detailed diagrams and examples can be added here if required to aid understanding]

The content is written in points and in a formal tone as a study material. Mnemonics and learning tricks are included where applicable to make topics easy to remember. Let me know if you would like me to elaborate on any part of the content or add additional details.