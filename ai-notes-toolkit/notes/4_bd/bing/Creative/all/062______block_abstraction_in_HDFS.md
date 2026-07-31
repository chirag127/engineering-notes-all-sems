#### Block abstraction in HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing large amounts of data across multiple nodes in a cluster.
- HDFS exposes a file system namespace and allows user data to be stored in files.
- Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes.
- A block is the smallest unit of data that can be read or written in HDFS.
- HDFS block size is usually 64MB-128MB and unlike other filesystems, a file smaller than the block size does not occupy the complete block size’s worth of memory  .
- The block size is kept so large so that less time is made doing disk seeks as compared to the data transfer rate  .
- In HDFS the abstraction is made over the blocks of a file rather than a single file which simplifies the storage subsystem.
- Since the size of the blocks is fixed it is easy to manage and calculate how many blocks can be stored on a single disk.
- The NameNode executes file system namespace operations like opening, closing, and renaming files and directories.
- The NameNode also maintains the metadata of the blocks, such as their locations, sizes, replicas, permissions, etc.
- The DataNodes are responsible for serving read and write requests from the clients, as well as performing block creation, deletion, and replication according to the instructions from the NameNode.
- The block abstraction in HDFS enables the system to handle large files efficiently, distribute the data across the cluster, and provide fault tolerance and reliability.