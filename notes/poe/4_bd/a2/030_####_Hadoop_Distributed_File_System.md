 Here is the content in markdown format for #### Hadoop Distributed File System:

#### Hadoop Distributed File System

- HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.
- HDFS has a master-slave architecture. The NameNode is the master that manages the file system namespace and regulates access to files by clients. DataNodes are slaves that store the data blocks and serve read/write requests from clients.
- HDFS is optimized to store large files. It has fast writes and sequential reads, but seeks and small writes/reads are slow. Blocks are very large (typically 128MB) for efficiency.
- HDFS is a highly fault-tolerant system. HDFS actively replicates data across multiple datanodes, allowing it to remain operational even in the event of some node failures. There are three common replication levels: 3, 5, and 7.
- HDFS distributes files across blocks that are spread across Datanodes. Thus, an application that is reading a file can read the blocks in parallel, substantially increasing read throughput and allowing large files to be read very quickly.
- Mnemonics to remember:
-- NameNode (master) manages files and metadata
-- DataNodes (slaves) store blocks and serve read/write requests
-- Optimized for large files with large blocks (typically 128MB)
-- Fault tolerant with replication of blocks across DataNodes
-- Reading can be parallelized since file is split into blocks across nodes

Advantages:
- Scalable - can store and process extremely large data sets
- Fault tolerant - replication provides data redundancy
- Inexpensive - commodity hardware can be used
- Stream oriented access - high throughput for large files

Disadvantages:
- Not suitable for small files - inefficient handling of many small files due to block sizes
- Seeking within files is slow
- Limited metadata - no support for directories, links, etc.

[Additional details, diagrams, examples, applications, etc. can be added here if required.]