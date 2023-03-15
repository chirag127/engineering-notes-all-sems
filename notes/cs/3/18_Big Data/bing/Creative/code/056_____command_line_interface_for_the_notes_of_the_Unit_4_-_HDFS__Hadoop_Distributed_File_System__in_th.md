### Command Line Interface for HDFS

- The command line interface (CLI) is one of the simplest ways to interact with HDFS.
- The CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories in HDFS.
- The CLI can be accessed by running `$HADOOP_HOME/bin/hdfs dfs` followed by a subcommand and its arguments.
- The CLI can also be used to perform administrative tasks such as checking the status, health, and configuration of HDFS.
- The CLI can be used with different file systems that Hadoop supports, such as local, S3, Azure, etc.
- The CLI can be used with different Hadoop clusters, such as HDInsight, by specifying the `-fs` option with the cluster URL.
- The CLI can be used to get detailed help on every subcommand by running `$HADOOP_HOME/bin/hdfs dfs -help` or `$HADOOP_HOME/bin/hdfs dfs -help <subcommand>`.

Some examples of CLI subcommands are:

- `-cat`: Concatenates files and prints them to standard output.
- `-chgrp`: Changes the group of files and directories in HDFS.
- `-chmod`: Changes the permissions of files and directories in HDFS.
- `-chown`: Changes the owner of files and directories in HDFS.
- `-copyFromLocal`: Copies files from the local file system to HDFS.
- `-copyToLocal`: Copies files from HDFS to the local file system.
- `-count`: Counts the number of files, directories, and bytes in HDFS.
- `-cp`: Copies files and directories in HDFS.
- `-du`: Displays the disk usage of files and directories in HDFS.
- `-get`: Copies files from HDFS to the local file system.
- `-ls`: Lists files and directories in HDFS.
- `-mkdir`: Creates directories in HDFS.
- `-mv`: Moves files and directories in HDFS.
- `-put`: Copies files from the local file system to HDFS.
- `-rm`: Deletes files and directories in HDFS.
- `-rmdir`: Deletes empty directories in HDFS.
- `-tail`: Displays the last part of a file in HDFS.
- `-test`: Tests the existence, accessibility, or type of a file or directory in HDFS.

: https://www.guru99.com/learn-hdfs-a-beginners-guide.html
: https://citizenchoice.in/course/big-data/Chapter%203/9-command-line-interface
: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html
: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-use-hdfs-data-lake-storage