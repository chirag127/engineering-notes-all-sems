#### HDFS concepts

HDFS stands for Hadoop Distributed File System, which is a distributed file system designed to run on commodity hardware. It is one of the core components of Apache Hadoop, an open-source framework for processing large-scale data sets using parallel computing.

Some of the key concepts of HDFS are:

- **Cluster**: A Hadoop cluster is a collection of machines, called nodes, that communicate with each other over the network. Each node can perform different roles, such as NameNode, DataNode, or Client.
- **Blocks**: HDFS stores files as a sequence of fixed-size blocks, usually 128 MB, that are replicated across multiple DataNodes for fault tolerance. Each block has a unique identifier and a metadata file that stores information such as the block location, checksum, and permissions.
- **NameNode**: The NameNode is the master node that manages the namespace and the metadata of the file system. It maintains the file-to-block mapping, the block locations, and the replication factor of each block. It also handles the client requests for file operations, such as creating, deleting, reading, or writing files.
- **DataNode**: The DataNode is the worker node that stores and serves the data blocks to the clients. It periodically sends heartbeat and block report messages to the NameNode to report its status and the blocks it holds. It also performs block operations, such as replication, deletion, or checksum verification, as instructed by the NameNode.
- **Client**: The client is the node that accesses the file system through the Hadoop API or the command-line interface. It interacts with the NameNode to get the metadata and the block locations of a file, and then directly communicates with the DataNodes to read or write the data blocks. It also performs some tasks, such as splitting a file into blocks, choosing the DataNodes for replication, or verifying the checksum of the blocks.