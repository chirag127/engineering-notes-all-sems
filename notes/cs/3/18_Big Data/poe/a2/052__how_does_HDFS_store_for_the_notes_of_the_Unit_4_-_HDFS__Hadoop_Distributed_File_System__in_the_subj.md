 Here are the notes for HDFS in markdown format:

### How HDFS stores data

1. HDFS splits files into large blocks (typically 128MB) and stores multiple replicas of them (typically 3) across multiple DataNodes for fault tolerance.
2. It uses a master-slave architecture with a NameNode (master) that manages the file system namespace and regulates access to files by clients and a DataNode (slave) that stores the blocks and serves read/write requests from clients.
3. The NameNode stores metadata about the file system tree and the locations of blocks in files in its memory. It does not store the actual data of the files.
4. The DataNodes store the actual blocks of data on their local file system and serve read/write requests from clients.
5. The replication of blocks across multiple DataNodes ensures high availability - if one DataNode fails, the blocks on it can be accessed from other DataNodes.
6. The large block size is suited for large streaming access of files which is a very common access pattern in big data applications. The overhead of the metadata for large blocks is amortized making the access more efficient.
7. The architecture allows the file system to scale to store and process very large datasets (in petabytes) across a large cluster of machines.

[No external links included as directed.]