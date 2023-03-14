#### Java interfaces to HDFS

Hadoop is implemented in Java language, so HDFS has a good Java interface for programming. The focus is Hadoop's FileSystem class, which is an abstract class of all file systems, and HDFS instances (DistributedFileSystem) are also implemented based on it.

A file in a Hadoop filesystem is represented by a Hadoop Path object. FileSystem is a general filesystem API, so the first step is to retrieve an instance for the filesystem we want to use—HDFS, in this case. There are several static factory methods for getting a FileSystem instance.

The following diagram illustrates the basic architecture of a Java interface to HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Java Program   |    |  FileSystem     |    |  HDFS Cluster   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Path           |    |  Configuration  |    |  NameNode       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  File           |    |  Distributed-   |    |  DataNode       |
|                 |    |  FileSystem     |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  InputStream    |    |  FSData-        |    |  Block          |
|                 |    |  InputStream    |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  OutputStream   |    |  FSData-        |    |  Block          |
|                 |    |  OutputStream   |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The Java program uses the Path class to represent a file or directory in HDFS. The Configuration class holds the configuration settings for the Hadoop cluster, such as the URI of the NameNode. The DistributedFileSystem class is a subclass of FileSystem that implements the HDFS-specific operations. The FSDataInputStream and FSDataOutputStream classes are subclasses of InputStream and OutputStream that provide methods for reading and writing data to HDFS. The HDFS cluster consists of a NameNode that manages the namespace and metadata, and DataNodes that store the data blocks. The Java interface communicates with the NameNode and DataNodes using RPC protocols   .