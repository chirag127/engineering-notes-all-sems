 Here is the content in markdown format with formal tone and without emojis:

#### Design of HDFS

1. HDFS has a master-slave architecture. The master is called NameNode and slave is called DataNode.
2. HDFS cluster has only one NameNode whereas multiple DataNodes. NameNode controls and manages the file system namespace and regulates access to files by clients. DataNodes are responsible for storing the blocks and serving read/write requests from the clients.
3. HDFS is designed for streaming access of large files. It is not suitable for random access of small files as it can affect the performance. HDFS is optimized for throughput rather than latency.
4. HDFS provides fault tolerance using replication. The blocks of a file are replicated at multiple DataNodes. The replication factor can be 3 or more based on the usage. If one DataNode fails, the data can be accessed from other replicas.
5. HDFS follows write once read many access model. Once data is written, it cannot be modified. HDFS supports append operation to append data to the existing file.
6. HDFS has a master-slave architecture. The master NameNode performs the directory namespace operations like opening, closing, renaming files and directories. The DataNodes serve read and write requests from clients for their data blocks.
7. HDFS has rack awareness to place blocks on different racks for fault tolerance. This reduces the impact of rack failure and provides data locality for reads.
8. The files in HDFS are broken into blocks of fixed size, typically 128 MB or 256 MB. This helps in efficient storage and replication. The blocks are replicated for fault tolerance.