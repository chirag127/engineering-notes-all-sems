# Command Line Interface for HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing and processing large-scale data sets.
- HDFS can be accessed through various ways, such as Java API, web interface, or command line interface (CLI).
- CLI is one of the simplest and most common ways to interact with HDFS. It allows users to perform file system operations such as reading, writing, creating, deleting, moving, copying, and listing files and directories on HDFS.
- CLI is based on the Hadoop shell commands, which are executed using the `hdfs` command. The general syntax of the `hdfs` command is:

  ```
  hdfs [generic options] [command] [command options] [arguments]
  ```

- The generic options are common to all Hadoop commands, such as `-conf`, `-D`, `-fs`, etc. They can be used to specify configuration files, properties, file system URIs, and so on.
- The command is the specific HDFS operation to be performed, such as `dfs`, `dfsadmin`, `fsck`, `haadmin`, etc. Each command has its own subcommands and options that can be viewed using the `-help` option.
- The arguments are the files or directories on HDFS that are the targets or sources of the command.
- Some examples of the `hdfs` command are:

  - To list the contents of the root directory on HDFS:

    ```
    hdfs dfs -ls /
    ```

  - To copy a local file to HDFS:

    ```
    hdfs dfs -put localfile.txt /user/hadoop
    ```

  - To create a new directory on HDFS:

    ```
    hdfs dfs -mkdir /user/hadoop/newdir
    ```

  - To delete a file or directory on HDFS:

    ```
    hdfs dfs -rm -r /user/hadoop/newdir
    ```

  - To display the help message for a command or subcommand:

    ```
    hdfs dfs -help ls
    ```

- For more details and examples of the HDFS CLI, refer to the official documentation or the online tutorials  .