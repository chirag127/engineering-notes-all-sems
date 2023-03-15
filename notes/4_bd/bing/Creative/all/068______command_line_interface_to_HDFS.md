#### Command Line Interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing large amounts of data in clusters of machines.
- Command Line Interface (CLI) is one of the ways to access and manipulate HDFS files and directories using shell-like commands.
- To use CLI, we need to have Hadoop installed and configured on our system, and run the commands using the `hdfs` utility under the `$HADOOP_HOME/bin` directory.
- Some of the common CLI commands for HDFS are:

  - `hdfs dfs -ls <path>`: List the files and directories in the given path.
  - `hdfs dfs -mkdir <path>`: Create a new directory in the given path.
  - `hdfs dfs -put <local_path> <hdfs_path>`: Copy a file from the local file system to the HDFS.
  - `hdfs dfs -get <hdfs_path> <local_path>`: Copy a file from the HDFS to the local file system.
  - `hdfs dfs -cat <path>`: Display the contents of a file in the HDFS.
  - `hdfs dfs -rm <path>`: Delete a file or an empty directory in the HDFS.
  - `hdfs dfs -rmdir <path>`: Delete a directory and its contents recursively in the HDFS.
  - `hdfs dfs -cp <source_path> <destination_path>`: Copy a file or a directory within the HDFS.
  - `hdfs dfs -mv <source_path> <destination_path>`: Move a file or a directory within the HDFS.
  - `hdfs dfs -du <path>`: Display the disk usage of a file or a directory in the HDFS.
  - `hdfs dfs -df <path>`: Display the available and used space in the HDFS.
  - `hdfs dfs -help <command>`: Display the usage and options of a command.

- For more details and examples of CLI commands, we can refer to the official documentation or the online tutorials  .