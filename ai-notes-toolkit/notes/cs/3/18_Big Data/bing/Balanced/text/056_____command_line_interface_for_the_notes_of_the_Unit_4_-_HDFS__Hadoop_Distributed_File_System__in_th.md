### Command Line Interface for HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing and processing large-scale data sets.
- HDFS can be accessed through various ways, such as Java API, web browser, or command line interface (CLI).
- CLI is one of the simplest and most common ways to interact with HDFS. It allows users to perform file system operations such as reading, writing, creating, deleting, moving, copying, and listing files and directories on HDFS.
- CLI is based on the Hadoop shell commands, which are executed using the `hdfs` command. The general syntax of the `hdfs` command is:

  ```
  hdfs [generic options] [command] [command options] [arguments]
  ```

- The generic options are common to all Hadoop commands, such as `-conf`, `-D`, `-fs`, etc. They can be used to specify configuration files, properties, file system URIs, and so on.
- The command is the specific HDFS operation to be performed, such as `dfs`, `dfsadmin`, `fsck`, `haadmin`, etc. Each command has its own subcommands and options that can be viewed using the `-help` option.
- The arguments are the files or directories on HDFS that are the targets or sources of the command.
- For example, to list the contents of the root directory on HDFS, the command would be:

  ```
  hdfs dfs -ls /
  ```

- Here, `dfs` is the command for file system operations, `-ls` is the subcommand for listing files and directories, and `/` is the argument for the root directory on HDFS.
- Some of the common HDFS commands and their subcommands are:

  - `dfs` : file system operations, such as `-cat`, `-chmod`, `-copyFromLocal`, `-get`, `-mkdir`, `-put`, `-rm`, etc.
  - `dfsadmin` : administrative operations, such as `-report`, `-safemode`, `-refreshNodes`, `-setQuota`, etc.
  - `fsck` : check the health of the file system, such as `-files`, `-blocks`, `-locations`, etc.
  - `haadmin` : manage the high availability of the NameNode, such as `-transitionToActive`, `-transitionToStandby`, `-getServiceState`, etc.

- To get detailed help on any command, subcommand, or option, the `-help` option can be used. For example, to get help on the `dfs` command, the command would be:

  ```
  hdfs dfs -help
  ```

- To get help on a specific subcommand, such as `-ls`, the command would be:

  ```
  hdfs dfs -help ls
  ```

- To get help on a generic option, such as `-fs`, the command would be:

  ```
  hdfs -help -fs
  ```

- To access HDFS using CLI, the user needs to have the Hadoop installation directory in the `PATH` environment variable, or use the full path of the `hdfs` command. The user also needs to have the appropriate permissions and configuration settings to access the HDFS cluster.