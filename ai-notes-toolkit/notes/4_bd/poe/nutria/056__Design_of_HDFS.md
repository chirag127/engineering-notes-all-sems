

#### Design of HDFS

1. HDFS (Hadoop Distributed File System) is a distributed file system designed to run on commodity hardware. It is highly fault-tolerant and is designed to be deployed on low-cost hardware.

2. HDFS is designed to store very large files across multiple machines. It stores each file as a sequence of blocks, all of which are of the same size except the last block.

3. HDFS is designed to be highly available and fault-tolerant. It replicates each block of a file to multiple DataNodes. This ensures that even if one of the DataNodes fails, the file can still be read from the other DataNodes.

4. HDFS also supports high bandwidth data access. It allows multiple clients to read the same file simultaneously, making it suitable for applications that require large data sets.

5. HDFS also supports a high degree of data integrity. It checksums each block of a file to ensure data integrity and provides an API for verifying the checksums.

6. HDFS is designed to be highly scalable. It can scale up to hundreds of nodes and petabytes of data. It also supports the addition of new nodes to the cluster without any downtime.