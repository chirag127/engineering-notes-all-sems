 Here is the formal content on Hadoop Distributed File System in points:

#### Hadoop Distributed File System

1. HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.

2. HDFS has a master/slave architecture. An HDFS cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients. In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on.

3. HDFS exposes a file system namespace and allows user data to be stored in files. Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes.

4. The NameNode executes file system namespace operations like opening, closing, and renaming files and directories. It also determines the mapping of blocks to DataNodes. The DataNodes are responsible for serving read and write requests from the file system's clients.

5. The DataNodes also perform block creation, deletion, and replication upon instruction from the NameNode.

6. HDFS has a very large default block size (typically 128MB) and a default replication factor of 3. This leads to very high throughput for large files due to fewer metadata operations and fewer seeks, while still maintaining high data reliability.