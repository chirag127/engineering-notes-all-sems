#### Block sizes in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS breaks down the files into fixed-size blocks, which are stored on different data nodes.
- The default block size in HDFS is 128 MB, but it can be configured manually by changing the `dfs.block.size` property in `hdfs-site.xml` file  .
- The block size can also be specified for a particular file while copying it to HDFS using the `-Ddfs.blocksize` option.
- The advantage of using large blocks in HDFS is that it reduces the number of disk seeks and network transfers, which improves the data throughput and performance .
- The disadvantage of using large blocks in HDFS is that it may cause internal fragmentation and waste disk space if the file size is not a multiple of the block size.
- HDFS also replicates each block across multiple nodes to ensure fault tolerance and availability. The default replication factor is 3, but it can be changed by modifying the `dfs.replication` property in `hdfs-site.xml` file.