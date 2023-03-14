#### HDFS concepts

- HDFS stands for Hadoop Distributed File System. It is a distributed file system that stores large-scale data across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the namespace, metadata, and access control of the file system. It also coordinates the replication and placement of data blocks among the DataNodes.
- The DataNodes are responsible for storing the actual data blocks of the files. They also perform read and write operations on the data blocks as instructed by the NameNode.
- HDFS splits a file into fixed-size blocks (typically 128 MB) and distributes them across the DataNodes. Each block is replicated a number of times (default is 3) for fault tolerance and availability.
- HDFS provides a high-level abstraction of the file system to the clients. Clients can access the files using the Hadoop API or the command-line interface. They do not need to know the physical location of the data blocks or the replication factor.
- HDFS supports a write-once-read-many model, where a file can be written only once and then read multiple times. HDFS does not support random writes or updates to a file. However, it supports appending data to an existing file.
- HDFS is designed to handle large files (in the order of GBs or TBs) and high-throughput streaming access. It is not suitable for low-latency or interactive applications. It also does not support POSIX semantics or file locking.