# Hadoop File System Interfaces

- Hadoop provides a Java abstract class `org.apache.hadoop.fs.FileSystem` that represents the client interface to a file system in Hadoop  .
- Hadoop supports various file systems that can be implemented concretely, such as HDFS, S3, FTP, local, etc. Hadoop uses the URI scheme to select the appropriate file system instance to communicate with .
- Hadoop also provides a command interface to interact with HDFS, such as `hadoop fs` and `hdfs dfs` commands.
- HDFS is the default and most common file system in Hadoop. It is a distributed file system designed to run on commodity hardware, and it is highly fault-tolerant and scalable.
- HDFS has a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes. The NameNode manages the file system namespace and the metadata, while the DataNodes store the actual data in blocks.
- HDFS provides streaming access to file system data, and supports large files, high throughput, and replication for fault-tolerance.