#### HDFS concepts

- HDFS stands for Hadoop Distributed File System. It is a distributed file system that stores large-scale data across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the namespace, metadata, and access control of the files and directories in HDFS. It also coordinates the replication and placement of data blocks among the DataNodes.
- The DataNodes are responsible for storing, reading, and writing the data blocks of the files in HDFS. They also send periodic heartbeats and block reports to the NameNode to indicate their status and availability.
- HDFS splits a file into fixed-size blocks (typically 128 MB) and distributes them across the DataNodes for parallel processing. Each block is replicated a number of times (default is 3) for fault tolerance and reliability.
- HDFS provides a client interface that allows users and applications to interact with the file system. The client communicates with the NameNode to obtain the location of the data blocks and then directly transfers data to and from the DataNodes.
- HDFS supports a write-once-read-many model, where a file can be written only once and then read multiple times. HDFS does not support random writes or updates to a file, but it supports appending new data to an existing file.
- HDFS is designed to handle large files and high throughput of data. It is optimized for streaming access rather than random access. It also supports compression and decompression of data to reduce the network and storage overhead.