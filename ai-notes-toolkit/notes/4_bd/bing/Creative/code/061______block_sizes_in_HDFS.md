#### Block sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS divides files into fixed-size blocks, which are stored on different slave machines, and the master machine stores the metadata about blocks location.
- The size of the data block in HDFS is 64 MB by default, which can be configured manually. In general, the data blocks of size 128MB is used in the industry  .
- The advantage of using large block sizes in HDFS is that it reduces the number of disk seeks and network transfers, which improves the performance and throughput of data processing .
- The disadvantage of using large block sizes in HDFS is that it may cause internal fragmentation and waste disk space, especially for small files that do not occupy the full block worth of underlying storage .
- HDFS supports variable length blocks, which means that users can start a new block without filling out the last block to the configured block size after the support for append and hsync was added. This feature can reduce the internal fragmentation and improve the space utilization of HDFS.