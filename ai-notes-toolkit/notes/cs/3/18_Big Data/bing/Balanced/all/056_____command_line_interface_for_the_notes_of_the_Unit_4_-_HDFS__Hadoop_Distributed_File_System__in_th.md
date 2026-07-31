# Command Line Interface for HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system that runs on clusters of commodity hardware.
- HDFS can be accessed through various ways, such as Java API, web browser, or command line interface (CLI).
- CLI is one of the simplest ways to interact with HDFS. It allows users to perform file system operations such as reading, writing, creating, deleting, moving, and listing files and directories.
- CLI commands are executed using the `hdfs` utility, which is located in the `$HADOOP_HOME/bin` directory. The general syntax of the `hdfs` command is:

  ```
  hdfs [generic options] [command] [command options] [arguments]
  ```

- The generic options are common to all Hadoop commands, such as `-conf`, `-fs`, `-D`, etc. They can be used to specify configuration files, file system URI, system properties, etc.
- The command is the name of the subcommand to be executed, such as `dfs`, `dfsadmin`, `fsck`, etc. Each subcommand has its own set of options and arguments.
- The command options are specific to each subcommand, such as `-put`, `-get`, `-ls`, etc. They can be used to specify the operation to be performed on the file system.
- The arguments are the operands of the command, such as source and destination paths, file names, etc.

- Some of the common subcommands and options of the `hdfs` utility are:

  - `dfs`: This subcommand is used to perform file system operations on HDFS. It supports multiple options, such as:

    - `-put`: This option is used to copy one or more files from the local file system to HDFS.
    - `-get`: This option is used to copy one or more files from HDFS to the local file system.
    - `-cat`: This option is used to display the contents of one or more files on the standard output.
    - `-ls`: This option is used to list the files and directories in a given path.
    - `-mkdir`: This option is used to create one or more directories in HDFS.
    - `-rm`: This option is used to delete one or more files or directories from HDFS.
    - `-mv`: This option is used to move one or more files or directories within HDFS.
    - `-cp`: This option is used to copy one or more files or directories within HDFS.

  - `dfsadmin`: This subcommand is used to perform administrative tasks on HDFS, such as reporting, balancing, refreshing, etc. It supports multiple options, such as:

    - `-report`: This option is used to print a report on the status of the cluster, such as the number of nodes, the total and used capacity, the health of the nodes, etc.
    - `-safemode`: This option is used to enter or leave the safe mode of HDFS, which is a state where no changes can be made to the file system.
    - `-refreshNodes`: This option is used to refresh the list of nodes that are allowed to connect to the cluster, based on the configuration file.
    - `-setQuota`: This option is used to set the quota of files and directories for a given path.

  - `fsck`: This subcommand is used to check the health of the file system, such as the number of missing blocks, the replication factor, the corrupted files, etc. It supports multiple options, such as:

    - `-files`: This option is used to print the names of the files that are checked.
    - `-blocks`: This option is used to print the block information of the files that are checked.
    - `-locations`: This option is used to print the locations of the blocks of the files that are checked.
    - `-delete`: This option is used to delete the corrupted files that are found.

- To get detailed help on every subcommand and option, we can run `hdfs [subcommand] -help` or `hdfs [subcommand] [option] -help`. For example, to get help on the `dfs` subcommand, we can run `hdfs dfs -help`. To get help on the `-put` option of the `dfs` subcommand, we can run `hdfs dfs -put -help`.