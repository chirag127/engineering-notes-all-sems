# File Sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing and processing large-scale data sets.
- HDFS stores the data in the form of blocks, which are fixed-sized chunks of data that are distributed across the cluster nodes.
- The default size of each block in HDFS is 128 MB, but it can be configured according to the requirements in the hdfs-site.xml file .
- The block size in HDFS is typically much larger than the block size in a traditional file system, because HDFS is designed to handle large files that are gigabytes to terabytes in size .
- The advantage of having a large block size in HDFS is that it reduces the overhead of managing the metadata, improves the data transfer rate, and enables the use of replication for fault tolerance.
- The disadvantage of having a large block size in HDFS is that it may cause internal fragmentation, which is the wasted space within a block that is not used by the file.
- To find the size of a file or a directory in HDFS, the following commands can be used :
  - `hadoop fs -du -s -h /path/to/file` : This command displays the size of the file in human-readable format (e.g., MB, GB, etc.).
  - `hadoop fs -du -s -h /path/to/directory` : This command displays the total size of all the files in the directory in human-readable format.
  - `hadoop fs -dus /path/to/directory` : This command displays the total size of all the files in the directory in bytes.
  - `hadoop fs -dus /path/to/file` : This command displays the size of the file in bytes.
  - `hdfs dfsadmin -report` : This command displays a cluster-level storage report, which shows the total capacity, used space, and remaining space of each node in the cluster.