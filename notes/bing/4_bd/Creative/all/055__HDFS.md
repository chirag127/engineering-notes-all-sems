### HDFS

- HDFS stands for Hadoop Distributed File System. It is a file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS is designed to handle failures gracefully, by replicating data blocks on different nodes and providing fault tolerance and high availability.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the namespace, the metadata, and the access control of the files and directories. It also coordinates the placement and replication of data blocks on the DataNodes.
- The DataNodes are responsible for storing the actual data blocks and serving read and write requests from the clients. They also periodically report to the NameNode about the status of the data blocks they hold.
- HDFS splits a large file into fixed-size blocks (typically 128 MB) and distributes them across the DataNodes. Each block is replicated a number of times (default is 3) for fault tolerance.
- HDFS provides a Java-based API for clients to interact with the file system. It also supports a web-based interface and a command-line interface.
- HDFS supports a write-once-read-many model, where a file can be written only once and then read multiple times. It does not support random writes or updates to a file.
- HDFS is optimized for streaming access of large files, rather than random access of small files. It is suitable for applications that perform batch processing or analytics on large datasets.
- HDFS is not a POSIX-compliant file system, meaning it does not support some of the features and semantics of a standard Unix file system, such as hard links, soft links, file permissions, etc.