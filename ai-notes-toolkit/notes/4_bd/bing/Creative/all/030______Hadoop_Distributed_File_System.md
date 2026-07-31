#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters .
- HDFS is one of the core components of Apache Hadoop, along with MapReduce and YARN.
- HDFS is designed to handle large data sets running on commodity hardware, and to scale up to thousands of nodes.
- HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the others act as the DataNodes (slaves).
- The NameNode manages the file system namespace, the metadata, and the access control. It also coordinates the replication and the placement of data blocks among the DataNodes.
- The DataNodes store the actual data blocks and serve read and write requests from the clients. They also perform block creation, deletion, and replication as instructed by the NameNode.
- HDFS splits files into fixed-size blocks (typically 64 MB or 128 MB) and distributes them across the DataNodes in the cluster. Each block is replicated a number of times (default is 3) for fault tolerance .
- HDFS provides a Java API for applications to access the file system, as well as a command-line interface and a web interface.
- HDFS supports the write-once-read-many model, where a file can be written only once and then read multiple times. HDFS does not support random write or append operations.
- HDFS is optimized for streaming data access, where the data is read sequentially and processed in batches. HDFS is not suitable for low-latency or interactive applications.
- HDFS can be integrated with other storage systems, such as Amazon S3, Google Cloud Storage, or Azure Blob Storage, using connectors or gateways.
- HDFS can be extended with additional features, such as encryption, compression, erasure coding, snapshots, quotas, or federation.

Some possible mnemonics and learning tricks for HDFS are:

- HDFS stands for Hadoop Distributed File System, where Hadoop is the name of the elephant mascot of the project, Distributed means the data is spread across multiple nodes, File System means it organizes the data into files and directories, and System means it is a software component that runs on the nodes.
- HDFS has a master-slave architecture, where the master is called the NameNode and the slaves are called the DataNodes. You can remember this by thinking of the NameNode as the "boss" who knows the names and locations of all the data blocks, and the DataNodes as the "workers" who store and serve the data blocks.
- HDFS splits files into blocks and replicates them for fault tolerance. You can remember this by thinking of the blocks as the "pieces" of the files, and the replication as the "backup" copies of the pieces. The default block size is 64 MB or 128 MB, and the default replication factor is 3. You can use the acronym BRR (Block, Replication, Replication) to remember these values.
- HDFS supports the write-once-read-many model, where a file can be written only once and then read multiple times. You can remember this by thinking of the file as a "book" that can be published only once and then read by many readers. HDFS does not support random write or append operations, which means you cannot edit or add new pages to the book.