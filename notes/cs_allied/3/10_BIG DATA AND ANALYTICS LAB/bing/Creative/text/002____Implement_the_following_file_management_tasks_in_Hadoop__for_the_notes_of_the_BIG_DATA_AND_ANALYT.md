## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS is designed to handle large files that are typically in the range of terabytes or petabytes. It divides files into uniform sized blocks of 128 MB or 64 MB (preferably 128 MB) and distributes them across the cluster nodes.
- HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as the DataNodes (slaves). The NameNode manages the file system namespace and the metadata of the files and blocks. The DataNodes store the actual data blocks and serve read and write requests from the clients.
- HDFS provides fault tolerance and reliability by replicating each block across multiple DataNodes. The default replication factor is 3, which means each block is stored on three different DataNodes. The replication factor can be configured according to the needs of the application.
- HDFS supports various file operations such as creating, deleting, renaming, copying, moving, appending, and truncating files and directories. It also supports setting and changing permissions, ownership, and quotas of files and directories.
- HDFS can be accessed through a command-line interface (CLI), a web-based user interface (UI), or a Java API. The CLI is the most common way of interacting with HDFS. The CLI commands are similar to the Unix/Linux commands for local file systems.
- Some of the common HDFS commands are:

  - `hadoop fs -ls`: List the contents of a directory.
  - `hadoop fs -mkdir`: Create a directory.
  - `hadoop fs -put`: Copy a file from the local file system to HDFS.
  - `hadoop fs -get`: Copy a file from HDFS to the local file system.
  - `hadoop fs -cat`: Display the contents of a file.
  - `hadoop fs -rm`: Delete a file or a directory.
  - `hadoop fs -mv`: Move or rename a file or a directory.
  - `hadoop fs -cp`: Copy a file or a directory within HDFS.
  - `hadoop fs -appendToFile`: Append data to an existing file.
  - `hadoop fs -setrep`: Change the replication factor of a file or a directory.
  - `hadoop fs -chmod`: Change the permissions of a file or a directory.
  - `hadoop fs -chown`: Change the owner and group of a file or a directory.
  - `hadoop fs -du`: Display the disk usage of a file or a directory.
  - `hadoop fs -df`: Display the available space in HDFS.
  - `hadoop fs -help`: Display the help for a command.

- For more details and examples of HDFS commands, refer to the official documentation or the tutorials .