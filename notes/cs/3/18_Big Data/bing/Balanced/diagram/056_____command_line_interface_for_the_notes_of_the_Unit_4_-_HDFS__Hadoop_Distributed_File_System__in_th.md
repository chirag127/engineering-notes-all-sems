### Command Line Interface for HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- HDFS can be accessed through various ways, such as Java API, web browser, or command line interface (CLI).
- CLI is one of the simplest ways to interact with HDFS. It allows users to perform filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories on HDFS.
- CLI is based on the Hadoop shell commands, which are executed using the syntax `hdfs dfs <command> <args>`.
- The `hdfs dfs` command supports multiple subcommands, such as `-ls`, `-cat`, `-mkdir`, `-cp`, `-rm`, `-mv`, etc. Each subcommand has its own options and arguments.
- To get detailed help on every subcommand, users can run `hdfs dfs -help <subcommand>`.
- To access HDFS using CLI, users need to have Hadoop installed and configured on their system, and set the environment variable `HADOOP_HOME` to point to the Hadoop installation directory.
- Users can also specify the HDFS URI using the `-fs` option, such as `hdfs dfs -fs hdfs://namenode:port <command> <args>`.
- Here are some examples of using CLI to perform common operations on HDFS:

  - List the contents of the root directory: `hdfs dfs -ls /`
  - Create a new directory named `test`: `hdfs dfs -mkdir /test`
  - Copy a local file named `sample.txt` to HDFS: `hdfs dfs -put sample.txt /test`
  - Display the contents of the file `sample.txt` on HDFS: `hdfs dfs -cat /test/sample.txt`
  - Move the file `sample.txt` to a new location on HDFS: `hdfs dfs -mv /test/sample.txt /test/new.txt`
  - Delete the file `new.txt` on HDFS: `hdfs dfs -rm /test/new.txt`
  - Delete the directory `test` and all its contents on HDFS: `hdfs dfs -rm -r /test`