### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that handles large data sets running on commodity hardware.
- HDFS stores the data in the form of blocks, which are fixed-sized chunks of data that are stored as independent units .
- The default size of each data block in HDFS is 128 MB, which is configurable in the hdfs-site.xml file in the Hadoop directory .
- The block size in HDFS is larger than the typical file system block size, because HDFS is designed to accommodate applications that have data sets typically gigabytes to terabytes in size.
- The larger block size in HDFS reduces the number of disk seeks and network transfers, and improves the data throughput and scalability of the system.
- To find the size of a file or a directory in HDFS, the following commands can be used :
  - `hadoop fs -du -s -h /path/to/file` : This command displays the size of the file in human-readable format (e.g. MB, GB, etc.).
  - `hadoop fs -du -s -h /path/to/directory` : This command displays the total size of all the files in the directory in human-readable format.
  - `hadoop fs -dus /path/to/directory` : This command displays the total size of all the files in the directory in bytes.
  - `hdfs dfsadmin -report` : This command displays a quick cluster level storage report, which shows the total capacity, used space, and remaining space of each data node in the cluster.