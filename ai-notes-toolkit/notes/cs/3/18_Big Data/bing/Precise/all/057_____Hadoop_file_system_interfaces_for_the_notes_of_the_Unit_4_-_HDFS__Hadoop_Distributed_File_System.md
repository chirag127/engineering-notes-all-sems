# Hadoop File System Interfaces

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It provides scalable and reliable data storage, and it is an integral part of the Hadoop ecosystem. Here are some of the key interfaces of HDFS:

1. **Client Interface:** The client interface is used by applications to interact with HDFS. It provides methods for creating, reading, writing, and deleting files, as well as for creating and deleting directories.

2. **NameNode Interface:** The NameNode is the central server that manages the file system namespace and regulates access to files by clients. The NameNode interface is used by DataNodes to report the blocks they are storing and by clients to locate blocks and obtain metadata about the files.

3. **DataNode Interface:** DataNodes are responsible for storing the data blocks of files. The DataNode interface is used by the NameNode to issue commands to the DataNodes, such as to replicate blocks or to delete blocks.

4. **Secondary NameNode Interface:** The Secondary NameNode is responsible for performing periodic checkpoints of the file system metadata. The Secondary NameNode interface is used by the NameNode to transfer a copy of the file system metadata for checkpointing.
