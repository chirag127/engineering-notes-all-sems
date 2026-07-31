#### Command line interface to HDFS

HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing. HDFS can be accessed through a Java API or through a command-line interface (CLI). The CLI provides shell-like commands that directly interact with HDFS and other file systems that Hadoop supports. Some of the basic HDFS commands are:

- `hdfs dfs -ls <path>`: List the files and directories in the given path.
- `hdfs dfs -mkdir <path>`: Create a directory in the given path.
- `hdfs dfs -put <local_path> <hdfs_path>`: Copy a file from the local file system to HDFS.
- `hdfs dfs -get <hdfs_path> <local_path>`: Copy a file from HDFS to the local file system.
- `hdfs dfs -cat <path>`: Display the contents of a file in HDFS.
- `hdfs dfs -rm <path>`: Delete a file or directory in HDFS.
- `hdfs dfs -mv <src_path> <dest_path>`: Move or rename a file or directory in HDFS.
- `hdfs dfs -cp <src_path> <dest_path>`: Copy a file or directory in HDFS.
- `hdfs dfs -du <path>`: Display the disk usage of a file or directory in HDFS.
- `hdfs dfs -help <command>`: Display the help information for a specific command.

To use HDFS commands, you need to have Hadoop installed and configured on your system. You can also use the `-fs` option to specify the HDFS URI of the file system you want to access. For example, `hdfs dfs -fs hdfs://nn1 -ls /` will list the files and directories in the root directory of the HDFS file system with the namenode nn1. You can also use the environment variable `HADOOP_CONF_DIR` to point to the directory that contains the Hadoop configuration files. For more information, please refer to the HDFS Commands Guide.