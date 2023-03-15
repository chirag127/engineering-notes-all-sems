#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters   .
- HDFS is one of the core components of Apache Hadoop, along with MapReduce and YARN .
- HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across nodes in a cluster .
- HDFS employs a master/slave architecture, where one node (called the NameNode) manages the file system namespace and regulates access to files by clients, and the other nodes (called the DataNodes) store the actual data in the local disks.
- HDFS provides fault tolerance by replicating each block across multiple DataNodes, and by periodically checking the health of each node.
- HDFS supports a write-once-read-many model, where files are written by a single client and then read by multiple clients.
- HDFS is designed to handle large files (gigabytes to terabytes) and streaming data access, rather than random access to small files.
- HDFS can be accessed through a variety of interfaces, such as Java API, WebHDFS REST API, command-line interface, and Hadoop-compatible file systems (such as S3 or Azure Blob Storage).

A possible ASCII diagram of HDFS architecture is:

```
+----------------+            +----------------+
|                |            |                |
|    Client      |            |    Client      |
|                |            |                |
+----------------+            +----------------+
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
+----------------+            +----------------+
|                |            |                |
|    NameNode    |            |    DataNode    |
|                |            |                |
+----------------+            +----------------+
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
        |                            |
+----------------+            +----------------+
|                |            |                |
|    DataNode    |            |    DataNode    |
|                |            |                |
+----------------+            +----------------+
```

Some possible mnemonics and learning tricks for HDFS are:

- HDFS stands for Hadoop Distributed File System, which can be remembered as "Huge Data Files System".
- NameNode is the master node that names the files and blocks, and DataNode is the slave node that stores the data blocks.
- HDFS blocks are large (64 MB or 128 MB) and replicated across multiple DataNodes, which can be remembered as "Big Blocks Backup".
- HDFS supports write-once-read-many model, which can be remembered as "Write Once, Read Many".