### Data Flow in HDFS (Hadoop Distributed File System)

1. HDFS is a distributed file system designed to store large data sets across multiple machines.
2. Data is divided into blocks and distributed across the nodes in the cluster.
3. Each block is replicated multiple times for fault tolerance.
4. When a client wants to read a file, it contacts the NameNode for the locations of the blocks.
5. The NameNode returns the locations of the blocks, and the client reads the data directly from the DataNodes.
6. When a client wants to write a file, it contacts the NameNode to determine the location of the first block.
7. The client writes the data to the first DataNode, which then forwards the data to the next DataNode in the pipeline.
8. This process continues until all the data has been written to the specified number of replicas.
9. The NameNode is responsible for managing the file system namespace and regulating access to files.
10. The DataNodes are responsible for storing the data and serving read and write requests from clients.
