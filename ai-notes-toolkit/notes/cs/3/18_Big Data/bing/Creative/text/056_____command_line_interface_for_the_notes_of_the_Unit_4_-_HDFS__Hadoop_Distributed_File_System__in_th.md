### Command Line Interface for HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing and processing large-scale data sets.
- HDFS can be accessed through various ways, such as Java API, web browser, or command line interface (CLI).
- CLI is one of the simplest and most common ways to interact with HDFS. It allows users to perform file system operations such as reading, writing, creating, deleting, moving, copying, and listing files and directories on HDFS.
- CLI is based on the Hadoop shell commands, which are executed using the `hdfs` command. The general syntax of the `hdfs` command is:

  ```
  hdfs [generic options] [command] [command options] [arguments]
  ```

- The generic options are common to all Hadoop commands, such as `-conf`, `-fs`, `-D`, etc. They can be used to specify configuration files, file system URI, system properties, etc.
- The command is the specific HDFS operation to be performed, such as `dfs`, `dfsadmin`, `fsck`, `balancer`, etc. Each command has its own subcommands and options that can be viewed using the `-help` option.
- The arguments are the file or directory names on HDFS or the local file system, depending on the command and subcommand.
- Some examples of the `hdfs` command are:

  - To list the files and directories in the root directory of HDFS:

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

  - To display the usage information of the `hdfs` command:

    ```
    hdfs -help
    ```

- For more details and examples of the `hdfs` command and its subcommands, refer to the official documentation or the online tutorials  .