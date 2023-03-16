## Implement the following file management tasks in Hadoop:

Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models. Hadoop uses a distributed file system called HDFS (Hadoop Distributed File System) to store and manage data. HDFS is designed to handle large files that are split into blocks and replicated across multiple nodes in the cluster. HDFS provides high availability, fault tolerance, scalability, and reliability.

Some of the common file management tasks in Hadoop are:

- Creating and deleting directories and files
- Copying and moving files within or across clusters
- Listing and displaying files and directories
- Changing permissions and ownership of files and directories
- Checking the status and health of the cluster and the file system

To perform these tasks, Hadoop provides a set of commands that can be executed from the command line interface (CLI) or through a Java API. The commands are prefixed with `hadoop fs` or `hdfs dfs` and follow the syntax:

`hadoop fs -command [options] [arguments]`

or

`hdfs dfs -command [options] [arguments]`

Some examples of the commands are:

- To create a directory named `input` in HDFS:

`hadoop fs -mkdir /input`

- To delete a directory named `output` and all its contents in HDFS:

`hadoop fs -rm -r /output`

- To copy a local file named `data.txt` to HDFS:

`hadoop fs -put data.txt /input`

- To copy a file from HDFS to the local file system:

`hadoop fs -get /output/part-00000 result.txt`

- To move a file from one HDFS location to another:

`hadoop fs -mv /input/data.txt /output`

- To list the files and directories in the root of HDFS:

`hadoop fs -ls /`

- To display the contents of a file in HDFS:

`hadoop fs -cat /output/part-00000`

- To change the permission of a file in HDFS to 755 (read, write, and execute for owner, read and execute for group and others):

`hadoop fs -chmod 755 /input/data.txt`

- To change the owner and group of a file in HDFS to `hadoop` and `users` respectively:

`hadoop fs -chown hadoop:users /input/data.txt`

- To check the status of the HDFS cluster:

`hdfs dfsadmin -report`

- To check the health of the HDFS file system:

`hdfs fsck /`

These are some of the basic file management tasks in Hadoop. For more details and options, you can refer to the official documentation   or use the `-help` option with any command.