#### Command Line Interface to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store and manage large datasets across multiple nodes in a cluster. It is a core component of the Apache Hadoop ecosystem and is widely used in big data applications.

To interact with HDFS, users can use the HDFS command-line interface (CLI), which provides a set of commands to perform various operations on files and directories in HDFS. Here are some of the most commonly used HDFS CLI commands:

1. `hadoop fs -ls <path>`: This command lists the files and directories at the specified path in HDFS.
2. `hadoop fs -mkdir <path>`: This command creates a new directory at the specified path in HDFS.
3. `hadoop fs -put <local_path> <hdfs_path>`: This command copies a file from the local file system to HDFS.
4. `hadoop fs -get <hdfs_path> <local_path>`: This command copies a file from HDFS to the local file system.
5. `hadoop fs -cat <hdfs_path>`: This command displays the contents of a file in HDFS on the console.
6. `hadoop fs -rm <hdfs_path>`: This command deletes a file or directory in HDFS.
7. `hadoop fs -chmod <mode> <hdfs_path>`: This command changes the permissions of a file or directory in HDFS.
8. `hadoop fs -chown <owner>:<group> <hdfs_path>`: This command changes the owner and group of a file or directory in HDFS.
9. `hadoop fs -du -s <hdfs_path>`: This command displays the disk usage of a file or directory in HDFS.

Using the HDFS CLI, users can perform various operations on HDFS without the need for a graphical user interface. This makes it easier to automate tasks and perform operations in batch mode. Additionally, the HDFS CLI is a powerful tool for debugging and troubleshooting issues in Hadoop applications.

In conclusion, the HDFS CLI provides a set of commands to interact with HDFS and perform various operations on files and directories. It is an essential tool for Hadoop developers and administrators and can help simplify tasks and improve productivity.