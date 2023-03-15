#### Command Line Interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- Command Line Interface (CLI) is one of the simplest ways to interact with HDFS. CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories.
- To use CLI, we need to have Hadoop installed and configured on our system. We can run the following command to check the Hadoop version and the HDFS URI:

```bash
hadoop version
hdfs getconf -confKey fs.defaultFS
```

- The HDFS commands are prefixed with `hdfs dfs` or `hadoop fs`. For example, to list the files and directories in the root directory of HDFS, we can run:

```bash
hdfs dfs -ls /
```

- We can also use the `-help` option to get detailed help on every command. For example, to get help on the `-ls` command, we can run:

```bash
hdfs dfs -help ls
```

- Some of the common HDFS commands are:

  - `hdfs dfs -mkdir`: to create a directory in HDFS.
  - `hdfs dfs -put`: to copy a file from the local file system to HDFS.
  - `hdfs dfs -get`: to copy a file from HDFS to the local file system.
  - `hdfs dfs -cat`: to display the contents of a file in HDFS.
  - `hdfs dfs -rm`: to delete a file or a directory in HDFS.
  - `hdfs dfs -mv`: to move or rename a file or a directory in HDFS.
  - `hdfs dfs -cp`: to copy a file or a directory within HDFS.
  - `hdfs dfs -du`: to display the disk usage of a file or a directory in HDFS.
  - `hdfs dfs -df`: to display the available space in HDFS.
  - `hdfs dfs -chmod`: to change the permissions of a file or a directory in HDFS.
  - `hdfs dfs -chown`: to change the owner and group of a file or a directory in HDFS.

- For more information on the HDFS commands, please refer to the official documentation.