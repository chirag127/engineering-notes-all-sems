#### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system designed to store and process large amounts of data across multiple nodes in a cluster.
- HDFS breaks down files into fixed-size blocks, which are stored as independent units on different nodes. The default block size in HDFS is 128 MB, but it can be configured manually .
- The block size in HDFS is much larger than the typical block size in a traditional file system, such as 4 KB. This is because HDFS is optimized for large files, which can range from gigabytes to terabytes in size.
- The advantages of having a large block size in HDFS are:
  - It reduces the number of disk seeks, which improves the data transfer rate and the overall performance of the system.
  - It reduces the amount of metadata that needs to be stored and managed by the NameNode, which is the master node that keeps track of the location and status of all the blocks in the cluster.
  - It reduces the network overhead, as fewer requests and responses are needed to read or write a file.
- The disadvantages of having a large block size in HDFS are:
  - It increases the disk space wastage, as the last block of a file may not be fully utilized. For example, if a file is 129 MB in size, it will occupy two blocks of 128 MB each, but the second block will only use 1 MB of space, leaving 127 MB unused.
  - It increases the replication factor, which is the number of copies of each block that are stored on different nodes for fault tolerance. By default, the replication factor is 3, which means that each block is replicated three times. This means that a file of 129 MB will consume 768 MB of disk space in total (2 blocks x 3 replicas x 128 MB).
- To overcome the disadvantages of having a large block size in HDFS, some techniques are used, such as:
  - Compression, which reduces the size of the files and the blocks, and improves the disk space utilization and the data transfer rate.
  - Variable block size, which allows different files to have different block sizes, depending on their characteristics and requirements.
  - Small files handling, which involves combining multiple small files into a single large file, or storing them in a different file system, such as HBase or Hive.
- To check the size of a file or a directory in HDFS, some commands are used, such as:
  - `hadoop fs -ls <path>`, which lists the files and directories in the given path, along with their details, such as permissions, owner, group, size, and modification time. The size of the file or directory is shown in the fifth column of the output, in bytes.
  - `hadoop fs -du <path>`, which displays the disk usage of the files and directories in the given path, in bytes. The output shows the base size of the file or directory before replication, which means the actual amount of space that is used by the data.
  - `hadoop fs -du -s <path>`, which summarizes the disk usage of the files and directories in the given path, in bytes. The output shows the total size of the file or directory before replication, which means the sum of the sizes of all the files and directories that match the given path.