#### Block abstraction in HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing large amounts of data across multiple machines.
- HDFS exposes a file system namespace and allows user data to be stored in files. Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes.
- The block abstraction in HDFS is a logical unit of data storage that simplifies the management and replication of data across the cluster. A block is typically 64MB or 128MB in size, which is much larger than the block size of a traditional file system  .
- The advantages of having a large block size in HDFS are:
  - It reduces the overhead of managing metadata, as each file has fewer blocks and each block has a unique identifier.
  - It reduces the number of disk seeks, as more data can be read or written in a single disk operation.
  - It improves the network bandwidth utilization, as data can be transferred in large chunks between DataNodes and clients.
- The disadvantages of having a large block size in HDFS are:
  - It may waste some disk space, as a file smaller than the block size does not occupy the complete block size’s worth of memory .
  - It may increase the latency of accessing small files, as the entire block has to be read or written even if only a part of it is needed.
  - It may affect the load balancing of the cluster, as some DataNodes may have more blocks than others depending on the file distribution.
- A possible mnemonic to remember the block abstraction in HDFS is: **B**ig **L**ogical **O**bjects **C**hunked **K**eep **S**torage **S**imple.