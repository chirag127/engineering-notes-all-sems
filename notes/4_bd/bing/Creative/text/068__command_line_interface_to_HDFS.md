#### Command Line Interface to HDFS

- The command line interface (CLI) is one of the simplest ways to interact with HDFS.
- The CLI has support for filesystem operations like reading files, creating directories, moving files, deleting data, and listing directories.
- The CLI can be invoked by the `hdfs` script, which is located in the `$HADOOP_HOME/bin` directory.
- The `hdfs` script accepts various commands and options, which are documented in the [HDFS Commands Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html).
- Some of the common commands are:

  - `hdfs dfs` : Run a filesystem command on the file system supported in Hadoop.
  - `hdfs fsck` : Check the health of the HDFS file system.
  - `hdfs fetchdt` : Get a delegation token from a NameNode.
  - `hdfs classpath` : Print the class path needed to get the Hadoop jar and the required libraries.
  - `hdfs envvars` : Display computed Hadoop environment variables.

- To get detailed help on every command, use the `-help` option, for example: `hdfs dfs -help`.
- To get the list of all commands, use the `hdfs` script without any arguments.