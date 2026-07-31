## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS operations and commands are used to perform various file management tasks on Hadoop, such as creating, copying, deleting, updating, and listing files and directories.
- Some of the common HDFS commands are:

  - `hadoop fs -ls <path>`: This command lists the files and directories in the given path. If no path is given, it lists the contents of the current working directory.
  - `hadoop fs -mkdir <path>`: This command creates a new directory with the given path. If the parent directories do not exist, they are created automatically.
  - `hadoop fs -put <local_path> <hdfs_path>`: This command copies a file from the local file system to the HDFS. If the destination file already exists, it is overwritten.
  - `hadoop fs -get <hdfs_path> <local_path>`: This command copies a file from the HDFS to the local file system. If the destination file already exists, it is overwritten.
  - `hadoop fs -cat <path>`: This command displays the contents of a file on the standard output. It can also be used to concatenate multiple files and display them.
  - `hadoop fs -rm <path>`: This command deletes a file from the HDFS. If the path is a directory, it deletes the directory and all its contents recursively.
  - `hadoop fs -mv <src_path> <dest_path>`: This command moves a file or a directory from one location to another in the HDFS. If the destination file or directory already exists, it is overwritten.
  - `hadoop fs -cp <src_path> <dest_path>`: This command copies a file or a directory from one location to another in the HDFS. If the destination file or directory already exists, it is overwritten.
  - `hadoop fs -chmod <mode> <path>`: This command changes the permissions of a file or a directory in the HDFS. The mode is a three-digit octal number that represents the read, write, and execute permissions for the owner, group, and others.
  - `hadoop fs -chown <owner>[:<group>] <path>`: This command changes the owner and/or the group of a file or a directory in the HDFS. If the group is not specified, it is left unchanged.

- These are some of the basic file management tasks that can be performed on Hadoop using HDFS commands. For more details and examples, refer to the official documentation or the tutorials   .