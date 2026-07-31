#### File Sizes in HDFS

- HDFS is designed to handle very large files.
- The default block size in HDFS is 128 MB, which means that files are split into 128 MB chunks and distributed across the cluster.
- Files smaller than the block size will not be split and will be stored on a single DataNode.
- Files larger than the block size will be split into multiple blocks and distributed across multiple DataNodes.
- The NameNode keeps track of the location of each block and coordinates access to the file.
- HDFS is optimized for streaming large files, so it is not well-suited for handling many small files.
- Storing many small files can lead to inefficient use of disk space and increased load on the NameNode.
- It is recommended to combine small files into larger files before storing them in HDFS. This can be done using tools such as Hadoop Archives (HAR) or Sequence Files.