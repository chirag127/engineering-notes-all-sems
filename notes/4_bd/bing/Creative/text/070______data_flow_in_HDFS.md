#### Data flow in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store the actual data blocks of files.
- A file in HDFS is split into fixed-size blocks (typically 128 MB or 256 MB) and replicated across multiple DataNodes for fault tolerance.
- The default replication factor is 3, which means each block has 3 copies on different DataNodes.
- The NameNode maintains the mapping of files to blocks and blocks to DataNodes, as well as the replication factor and the health status of DataNodes.
- The NameNode does not store the data blocks itself, nor does it directly communicate with clients who want to read or write files.
- The clients interact with the NameNode to get the metadata information, such as the location of blocks, the size of files, the permissions of files, etc.
- The clients then communicate with the DataNodes to read or write the data blocks of files.
- The data flow in HDFS can be summarized as follows:

  - **Write operation:**
    - The client requests the NameNode to create a new file in the file system namespace.
    - The NameNode checks if the file already exists, and if the client has the permission to write the file.
    - If the file does not exist and the client has the permission, the NameNode grants a lease to the client to create the file.
    - The client requests the NameNode for a list of DataNodes that can host the replicas of the first block of the file.
    - The NameNode returns a list of DataNodes, sorted by their network distance from the client.
    - The client writes the data to the first DataNode in the list, which acts as the primary DataNode for the block.
    - The primary DataNode forwards the data to the next DataNode in the list, which in turn forwards it to the next DataNode, and so on, forming a pipeline of DataNodes.
    - The DataNodes send acknowledgments to the previous DataNodes in the pipeline, and the primary DataNode sends the final acknowledgment to the client.
    - The client requests the NameNode for a new list of DataNodes for the next block of the file, and repeats the process until all the blocks of the file are written.
    - The client tells the NameNode that the file is complete, and the NameNode commits the file to the file system namespace.

  - **Read operation:**
    - The client requests the NameNode for the list of DataNodes that host the replicas of the blocks of the file.
    - The NameNode returns the list of DataNodes for each block, sorted by their network distance from the client.
    - The client reads the data from the closest DataNode for each block, and if the read fails, it tries the next DataNode in the list, and so on, until the read is successful or the list is exhausted.
    - The client verifies the checksum of the data to detect any corruption or errors.
    - The client reads all the blocks of the file in sequence, and closes the file when done.