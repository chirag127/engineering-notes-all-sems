# File Sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that handles large data sets running on commodity hardware.
- HDFS stores the data in the form of blocks, which are fixed-sized chunks of data that are stored as independent units .
- The default size of each data block in HDFS is 128 MB, which can be configured according to the requirement in hdfs-site.xml file in the Hadoop directory .
- The advantage of having large block size in HDFS is that it reduces the overhead of managing the metadata and improves the data transfer rate by minimizing the number of disk seeks.
- The disadvantage of having large block size in HDFS is that it may cause internal fragmentation and waste disk space if the file size is not a multiple of the block size.
- To find the size of a file or a directory in HDFS, the following commands can be used :
  - `hadoop fs -du -s -h /path/to/file` : This command displays the size of the file in human-readable format (e.g. MB, GB, etc.).
  - `hadoop fs -du -s -h /path/to/directory` : This command displays the total size of all the files in the directory in human-readable format.
  - `hadoop fs -dus /path/to/directory` : This command displays the total size of all the files in the directory in bytes.
  - `hadoop fs -count -q -h /path/to/directory` : This command displays the number of files, directories, and quota information in the directory in human-readable format.
  - `hadoop fs -count -q -h /path/to/file` : This command displays the number of blocks, bytes, and quota information of the file in human-readable format.