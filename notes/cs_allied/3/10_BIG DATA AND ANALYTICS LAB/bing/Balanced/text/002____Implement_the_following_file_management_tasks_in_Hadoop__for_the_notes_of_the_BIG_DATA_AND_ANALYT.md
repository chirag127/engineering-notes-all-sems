## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides high-performance access to data across scalable Hadoop clusters.
- HDFS is designed to handle large files that are typically in the range of terabytes or petabytes. It divides files into uniform sized blocks of 128 MB or 64 MB (preferably 128 MB) and distributes them across the cluster nodes.
- HDFS also provides fault tolerance and redundancy by replicating each block on multiple nodes, depending on the replication factor. The default replication factor is 3, which means each block is stored on three different nodes.
- HDFS has a master-slave architecture, where one node acts as the NameNode and the rest of the nodes act as the DataNodes. The NameNode is responsible for managing the file system namespace, the metadata of the files and blocks, and the access control of the files. The DataNodes are responsible for storing the actual data blocks and serving read and write requests from the clients.
- HDFS supports various file operations, such as creating, deleting, renaming, copying, moving, appending, and listing files and directories. These operations can be performed using the Hadoop command-line interface (CLI), the Hadoop web interface, or the Hadoop Java API.
- Some of the common Hadoop commands for file management tasks are:

  - `hadoop fs -ls /`: List the files and directories in the root directory of HDFS.
  - `hadoop fs -mkdir /user`: Create a directory named user in the root directory of HDFS.
  - `hadoop fs -put localfile.txt /user`: Copy a file named localfile.txt from the local file system to the user directory in HDFS.
  - `hadoop fs -get /user/localfile.txt localfile2.txt`: Copy a file named localfile.txt from the user directory in HDFS to the local file system with a new name localfile2.txt.
  - `hadoop fs -cat /user/localfile.txt`: Display the contents of a file named localfile.txt in the user directory in HDFS.
  - `hadoop fs -appendToFile localfile3.txt /user/localfile.txt`: Append the contents of a file named localfile3.txt from the local file system to the end of a file named localfile.txt in the user directory in HDFS.
  - `hadoop fs -mv /user/localfile.txt /user/newfile.txt`: Rename a file named localfile.txt in the user directory in HDFS to newfile.txt.
  - `hadoop fs -cp /user/newfile.txt /user/copyfile.txt`: Copy a file named newfile.txt in the user directory in HDFS to another file named copyfile.txt in the same directory.
  - `hadoop fs -rm /user/copyfile.txt`: Delete a file named copyfile.txt in the user directory in HDFS.
  - `hadoop fs -rmdir /user`: Delete a directory named user in the root directory of HDFS, if it is empty.