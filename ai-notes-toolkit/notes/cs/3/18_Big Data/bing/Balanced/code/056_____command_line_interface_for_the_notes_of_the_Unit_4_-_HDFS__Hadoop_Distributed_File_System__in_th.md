### Command Line Interface for HDFS

- The command line interface (CLI) is one of the simplest ways to interact with HDFS.
- The CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories in HDFS.
- The CLI can be accessed by running `$HADOOP_HOME/bin/hdfs dfs` followed by a subcommand and its arguments.
- The CLI can also take a generic option `-fs` to specify the file system URI to use, such as `hdfs://nn1` for the namenode 1.
- The CLI can be used with different file systems that Hadoop supports, such as Azure Data Lake Storage Gen2, by using the appropriate scheme and authority in the URI, such as `abfs://container@account` for ADLS Gen2.
- Some of the common subcommands of the CLI are:

  - `-cat`: Displays the contents of one or more files in HDFS to standard output.
  - `-chgrp`: Changes the group of one or more files or directories in HDFS.
  - `-chmod`: Changes the permissions of one or more files or directories in HDFS.
  - `-chown`: Changes the owner of one or more files or directories in HDFS.
  - `-copyFromLocal`: Copies one or more files from the local file system to HDFS.
  - `-copyToLocal`: Copies one or more files from HDFS to the local file system.
  - `-cp`: Copies one or more files from one location to another within HDFS.
  - `-du`: Displays the disk usage of one or more files or directories in HDFS.
  - `-get`: Similar to `-copyToLocal`, but preserves the replication factor and block size of the source file.
  - `-ls`: Lists the contents of one or more directories in HDFS.
  - `-mkdir`: Creates one or more directories in HDFS.
  - `-mv`: Moves one or more files from one location to another within HDFS.
  - `-put`: Similar to `-copyFromLocal`, but overwrites the destination file if it already exists.
  - `-rm`: Deletes one or more files or directories in HDFS.
  - `-tail`: Displays the last kilobyte of one or more files in HDFS to standard output.

- To get detailed help on every subcommand, run `$HADOOP_HOME/bin/hdfs dfs -help <subcommand>`.
- To get a list of all the subcommands, run `$HADOOP_HOME/bin/hdfs dfs -usage`.