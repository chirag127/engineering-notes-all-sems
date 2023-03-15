#### File sizes in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS is designed to handle files that are typically in the range of gigabytes to terabytes in size.
- HDFS splits large files into fixed-size blocks, which are stored on different nodes in the cluster. The default block size is 128 MB, but it can be configured by the user.
- HDFS maintains multiple replicas of each block for fault tolerance and load balancing. The default replication factor is 3, but it can also be configured by the user.
- HDFS supports appending data to existing files, but not random writes or updates. This is because HDFS is optimized for sequential access and batch processing, rather than interactive or real-time applications.
- HDFS provides a command-line interface and a web interface for users to interact with the file system. Users can create, delete, copy, move, rename, and list files and directories in HDFS. Users can also check the status, location, and size of files and blocks in HDFS.