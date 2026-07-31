#### Command line interface to HDFS

HDFS is the Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data. HDFS can be accessed through a Java API or through a command-line interface (CLI). The CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories. The CLI can be invoked by using the `hdfs` command, which is located in the `$HADOOP_HOME/bin` directory. The general syntax of the `hdfs` command is:

```
hdfs <command> <options> <arguments>
```

Some of the common commands and their options are:

- `hdfs dfs -ls <path>`: List the contents of the specified path in HDFS.
- `hdfs dfs -mkdir <path>`: Create a directory in HDFS.
- `hdfs dfs -put <local_path> <hdfs_path>`: Copy a file from the local filesystem to HDFS.
- `hdfs dfs -get <hdfs_path> <local_path>`: Copy a file from HDFS to the local filesystem.
- `hdfs dfs -cat <path>`: Display the contents of a file in HDFS.
- `hdfs dfs -rm <path>`: Delete a file or directory in HDFS.
- `hdfs dfs -mv <source_path> <destination_path>`: Move or rename a file or directory in HDFS.
- `hdfs dfs -cp <source_path> <destination_path>`: Copy a file or directory in HDFS.
- `hdfs dfs -du <path>`: Display the disk usage of a file or directory in HDFS.
- `hdfs dfs -help <command>`: Display the help information for a specific command.

To use the CLI, you need to have access to a Hadoop cluster and its configuration files. You can also specify the HDFS URI as an option to the `hdfs` command, such as `hdfs -fs hdfs://namenode:port`. For more information, please refer to the HDFS Commands Guide.