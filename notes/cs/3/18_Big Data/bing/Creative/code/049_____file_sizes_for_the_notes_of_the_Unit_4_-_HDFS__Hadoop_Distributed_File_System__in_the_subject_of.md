### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that handles large data sets running on commodity hardware.
- HDFS stores the data in the form of blocks, which are fixed-sized chunks of data that are stored as independent units .
- The default size of each block in HDFS is 128 MB, which can be configured according to the requirement in the hdfs-site.xml file in the Hadoop directory .
- The block size in HDFS is larger than the typical file system block size, because it reduces the amount of metadata needed to store and manage the files, and it enables high throughput of data access.
- To find the size of a file or a directory in HDFS, the following commands can be used :
  - `hadoop fs -du -s -h /path/to/file` : This command displays the size of the file in human-readable format (such as KB, MB, GB, etc.).
  - `hadoop fs -du -s -h /path/to/directory` : This command displays the total size of all the files in the directory in human-readable format.
  - `hadoop fs -dus /path/to/directory` : This command displays the total size of all the files in the directory in bytes.
  - `hadoop dfsadmin -report` : This command displays a quick cluster level storage report, which shows the total capacity, used space, remaining space, and number of nodes in the cluster.