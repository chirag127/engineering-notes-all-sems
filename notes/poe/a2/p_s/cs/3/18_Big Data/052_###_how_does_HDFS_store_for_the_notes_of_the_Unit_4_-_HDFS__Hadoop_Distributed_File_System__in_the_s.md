 Here is the content in markdown format for the topic ### how does HDFS store for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

### HDFS Architecture
- HDFS has a master-slave architecture. The master is called NameNode and the slaves are called DataNodes.
- The NameNode manages the file system namespace and regulates access to files by clients. It stores the filesystem metadata within its local storage.
- The DataNodes store data chunks and serve read/write requests from clients. They also perform block creation, deletion, and replication upon instruction from the NameNode.

### HDFS Blocks
- HDFS stores large files as blocks of smaller sizes (typically 128MB). This enables:
-- Efficient streaming access of data.
-- Recovery of corrupted blocks by replicating multiple blocks.
-- Balancing load across nodes by distributing blocks.

- The blocks of a file are replicated for fault tolerance. The block replication factor can be configured per file. A higher replication factor leads to higher fault tolerance but also higher storage space usage.

### HDFS Storage
- HDFS provides a hierarchical namespace and stores data on the DataNodes.
- The directories and files in the namespace are represented by inodes. Each inode stores metadata of the directory/file, but not the file data itself.
- The file data is split into blocks and each block is stored as a file on a DataNode.
- The NameNode maintains mappings of the blocks of each file to the DataNodes storing the blocks.

[Additional details, diagrams, examples, advantages, disadvantages, applications, etc. can be added here for a comprehensive set of study notes.]