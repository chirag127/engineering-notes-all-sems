### How does HDFS store data?

HDFS is a distributed file system that stores data across multiple nodes in a cluster. It is designed to handle large amounts of unstructured data and provide high-performance access to it. HDFS has the following characteristics:

- It follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode manages the file system namespace, the metadata of the files and directories, and the mapping of blocks to DataNodes. It also coordinates the replication and recovery of blocks among DataNodes.
- The DataNodes store the actual data in the form of blocks, which are fixed-sized chunks of data (typically 64 MB or 128 MB). Each block is replicated across multiple DataNodes for fault-tolerance and load-balancing. The default replication factor is 3, which means each block has 3 copies on different DataNodes.
- The clients interact with the NameNode to perform file system operations, such as creating, deleting, reading, or writing files. The NameNode returns the list of DataNodes that store the blocks of a file, and the clients directly communicate with the DataNodes to transfer the data.
- HDFS supports a write-once-read-many model, where a file can be written only once by a single writer, and then read by multiple readers. HDFS does not support random writes or updates to a file, only appends.
- HDFS provides a command-line interface and a Java API for accessing the file system. It also supports other interfaces, such as WebHDFS, NFS, and FTP.