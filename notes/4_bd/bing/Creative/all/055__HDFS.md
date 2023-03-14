### HDFS

HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds or even thousands of nodes. HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN. HDFS should not be confused with or replaced by Apache HBase, which is a column-oriented non-relational database management system that sits on top of HDFS and can better support real-time data needs with its in-memory processing engine .

Some of the main features and benefits of HDFS are:

- **Fault tolerance**: HDFS can detect and recover from failures of servers or storage devices. It replicates each data block across multiple servers (by default, three) to ensure availability and durability. If a server fails, the data can be accessed from another replica. HDFS also performs checksums on each data block to detect and correct any corruption.
- **High throughput**: HDFS is designed for batch processing rather than interactive use, so the emphasis is on high data throughput rates, which accommodate streaming access to data sets. HDFS provides high aggregate data bandwidth and can scale to hundreds of nodes in a single cluster. HDFS also supports data locality, which means that the data is stored close to where it is processed, reducing the network overhead and improving the performance.
- **Large data sets**: HDFS can handle data sets that are typically gigabytes to terabytes or even petabytes in size. It can store any kind of data, whether structured, semi-structured, or unstructured, in its native format. HDFS also supports appending and appending-like operations to files, which are useful for data ingestion and streaming.
- **Portability and compatibility**: HDFS is built to be portable across multiple hardware platforms and to be compatible with a variety of underlying operating systems. It also supports a standard interface for accessing the data, such as the Hadoop FileSystem API, which can be used by various applications and frameworks, such as Apache Spark, Apache Hive, Apache Pig, etc.

The basic architecture of HDFS consists of two types of nodes: a NameNode and multiple DataNodes. The NameNode is the master node that manages the metadata of the file system, such as the file names, directories, permissions, locations of data blocks, etc. The DataNodes are the worker nodes that store and serve the data blocks to the clients. The NameNode and the DataNodes communicate with each other using the TCP/IP protocol.

A typical HDFS file system looks like this:

```
+-----------------+      +-----------------+      +-----------------+
|    NameNode     |      |    DataNode 1   |      |    DataNode 2   |
|                 |      |                 |      |                 |
|  /dir1/file1    |      |  file1: blk_1   |      |  file1: blk_1   |
|  /dir1/file2    |      |  file2: blk_2   |      |  file2: blk_3   |
|  /dir2/file3    |      |  file3: blk_4   |      |  file3: blk_5   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       +-----------------------+----+--------------------+----+
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       +-----------------------+----+--------------------+----+
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       |                       |    |                    |    |
       +-----------------------+----+--------------------+----