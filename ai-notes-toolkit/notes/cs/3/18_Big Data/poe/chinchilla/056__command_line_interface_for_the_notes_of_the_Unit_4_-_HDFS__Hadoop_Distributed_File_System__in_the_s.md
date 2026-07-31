### Command Line Interface for HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store and manage large datasets across multiple machines. Command Line Interface (CLI) is a tool that allows users to interact with HDFS using commands in a terminal or command prompt. In this section, we will discuss the different CLI commands used to interact with HDFS.

Here are some key points to keep in mind:

- To use HDFS CLI, you need to have Hadoop installed on your system.
- The CLI commands are executed on the NameNode, which is the master node in HDFS.
- The CLI commands are case-sensitive.

#### Basic Commands

1. `hadoop fs` - This command is used to access HDFS and perform various operations. Some common sub-commands are:
   - `ls` - List the contents of a directory.
   - `mkdir` - Create a new directory.
   - `put` - Copy a file from the local file system to HDFS.
   - `get` - Copy a file from HDFS to the local file system.
   - `rm` - Remove a file or directory from HDFS.
2. `hadoop dfsadmin` - This command is used to perform administrative tasks on the HDFS cluster. Some common sub-commands are:
   - `report` - Generate a report on the status of the HDFS cluster.
   - `safemode` - Enter or leave safe mode.
   - `refreshNodes` - Refresh the list of datanodes in the cluster.
3. `hadoop fsck` - This command is used to check the health of the HDFS file system. It can be used to detect and correct errors in the file system.

#### Advanced Commands

1. `hadoop distcp` - This command is used to copy data between two HDFS clusters or between HDFS and other file systems.
2. `hadoop archive` - This command is used to create or extract a Hadoop archive file, which is a compressed file format used to store and distribute Hadoop data.
3. `hadoop fsimage` - This command is used to view the HDFS file system metadata. It can be used to debug issues related to the file system.

#### Conclusion

In this section, we discussed the different CLI commands used to interact with HDFS. The HDFS CLI provides a powerful and flexible interface for managing large datasets in HDFS. By mastering these commands, you will be able to perform various operations on HDFS with ease.