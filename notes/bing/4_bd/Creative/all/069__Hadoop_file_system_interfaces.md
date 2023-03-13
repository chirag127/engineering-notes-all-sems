#### Hadoop file system interfaces

- Hadoop file system (HDFS) is a distributed file system that runs on a cluster of nodes and provides high-throughput access to large data sets.
- HDFS exposes two main interfaces for interacting with the file system: the Java API and the command-line interface (CLI).
- The Java API provides a set of classes and methods that allow applications to perform various operations on HDFS, such as creating, reading, writing, deleting, and appending files, as well as listing, renaming, and moving directories.
- The Java API also supports some advanced features, such as file checksums, snapshots, encryption, erasure coding, and quotas.
- The Java API is organized into three main packages: org.apache.hadoop.fs, org.apache.hadoop.hdfs, and org.apache.hadoop.hdfs.client.
- The org.apache.hadoop.fs package contains the core interfaces and classes that define the abstract file system model, such as FileSystem, Path, FileStatus, FSDataInputStream, and FSDataOutputStream.
- The org.apache.hadoop.hdfs package contains the implementation of HDFS-specific classes and methods, such as DistributedFileSystem, DFSClient, DFSInputStream, and DFSOutputStream.
- The org.apache.hadoop.hdfs.client package contains some additional classes and methods that provide more functionality and convenience for HDFS users, such as HdfsConfiguration, HdfsUtils, and HdfsAdmin.
- The command-line interface (CLI) provides a set of commands that allow users to perform various operations on HDFS from the shell, such as hdfs dfs -ls, hdfs dfs -cat, hdfs dfs -put, and hdfs dfs -get.
- The CLI also supports some advanced commands, such as hdfs dfsadmin, hdfs fsck, hdfs balancer, and hdfs crypto.
- The CLI is implemented by the org.apache.hadoop.fs.shell package, which parses the user input and invokes the corresponding Java API methods.
- The CLI can be accessed by using the hdfs script, which is located in the bin directory of the Hadoop installation.
- The CLI can also be accessed by using the hadoop fs command, which is a wrapper for the hdfs script.
- The CLI supports some common options, such as -conf, -D, -help, and -usage, as well as some HDFS-specific options, such as -skipTrash, -safely, and -storagepolicy.
- The CLI follows the Unix convention of using - for standard input and output, and * for wildcard matching.