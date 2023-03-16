## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS is designed to handle large files that are typically in the range of terabytes or petabytes. It divides files into uniform sized blocks of 128 MB or 64 MB (preferably 128 MB) and distributes them across the cluster nodes.
- HDFS also provides fault tolerance and reliability by replicating each block on multiple nodes. The default replication factor is 3, which means each block is stored on 3 different nodes.
- HDFS supports various file management tasks such as creating, deleting, copying, moving, renaming, and appending files and directories. These tasks can be performed using Hadoop commands or Hadoop APIs.
- Some of the common Hadoop commands for file management tasks are:

  - `hadoop fs -ls`: List the contents of a directory in HDFS.
  - `hadoop fs -mkdir`: Create a directory in HDFS.
  - `hadoop fs -put`: Copy a file from the local file system to HDFS.
  - `hadoop fs -get`: Copy a file from HDFS to the local file system.
  - `hadoop fs -cp`: Copy a file or directory from one location to another in HDFS.
  - `hadoop fs -mv`: Move a file or directory from one location to another in HDFS.
  - `hadoop fs -rm`: Delete a file or directory in HDFS.
  - `hadoop fs -cat`: Display the contents of a file in HDFS.
  - `hadoop fs -tail`: Display the last part of a file in HDFS.
  - `hadoop fs -chmod`: Change the permissions of a file or directory in HDFS.
  - `hadoop fs -chown`: Change the owner and group of a file or directory in HDFS.
  - `hadoop fs -du`: Display the disk usage of a file or directory in HDFS.
  - `hadoop fs -df`: Display the available space in HDFS.
  - `hadoop fs -setrep`: Change the replication factor of a file or directory in HDFS.
  - `hadoop fs -help`: Display the help message for a Hadoop command.

- For more details and examples of Hadoop commands, refer to the official documentation .