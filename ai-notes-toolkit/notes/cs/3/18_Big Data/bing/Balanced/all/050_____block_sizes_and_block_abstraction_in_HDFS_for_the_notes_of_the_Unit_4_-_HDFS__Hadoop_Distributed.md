# Block sizes and block abstraction in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS divides files into fixed-size blocks, which are stored on different DataNodes in the cluster. The default block size is 128 MB, but it can be configured by the user.
- The block size is chosen to be large enough to minimize the overhead of disk seeks and network transfers, and to maximize the throughput of data processing.
- HDFS block abstraction is the logical division of files into blocks, which is independent of the physical blocks of the underlying file system. A file smaller than the block size does not occupy the whole block's worth of memory, and a file larger than the block size is split into multiple blocks.
- HDFS block abstraction allows HDFS to store the metadata of the files and blocks in the NameNode, which is the master node of the cluster. The NameNode maintains the mapping of files to blocks, and the locations of blocks on DataNodes.
- HDFS block abstraction also enables HDFS to provide fault tolerance and replication of blocks. HDFS replicates each block on multiple DataNodes, and can recover from the failure of a DataNode by copying the blocks from other DataNodes. The replication factor is configurable by the user, and the default value is 3.