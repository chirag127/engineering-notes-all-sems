#### Command line interface to HDFS

The command line interface (CLI) is one of the simplest ways to interact with HDFS. The CLI has support for filesystem operations like reading the file, creating directories, moving files, deleting data, and listing directories. The CLI can be accessed by using the `hdfs dfs` command, which is a subcommand of the `hdfs` command. The `hdfs` command is a part of the Hadoop distribution and can be found in the `$HADOOP_HOME/bin` directory. The `hdfs dfs` command takes various options and arguments to perform different operations on HDFS. For example, to list the files and directories in the root directory of HDFS, one can use the command `hdfs dfs -ls /`.

The following diagram illustrates the basic architecture of the command line interface to HDFS:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    User Shell   |      |    HDFS Shell   |      |    HDFS Client  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  hdfs command   |----->|  hdfs dfs       |----->|  FileSystem API |
|                 |      |  subcommand     |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  hdfs dfs -ls / |----->|  -ls /          |----->|  listStatus()   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The user shell is the terminal where the user enters the `hdfs` command. The HDFS shell is the component that parses the `hdfs` command and invokes the appropriate subcommand. The HDFS client is the component that communicates with the HDFS cluster using the FileSystem API. The FileSystem API is a Java interface that abstracts the details of the underlying file system. The HDFS client implements the FileSystem API for HDFS and provides methods for performing various operations on HDFS. The HDFS client interacts with the NameNode and the DataNodes of the HDFS cluster to perform the operations. For example, when the user executes the `hdfs dfs -ls /` command, the HDFS client calls the `listStatus()` method of the FileSystem API, which returns the metadata of the files and directories in the root directory of HDFS. The HDFS shell then displays the output of the command to the user shell.