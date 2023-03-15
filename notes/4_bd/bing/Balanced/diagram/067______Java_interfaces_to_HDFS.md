#### Java interfaces to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system that runs on a cluster of nodes. HDFS provides high availability, fault tolerance, scalability, and reliability for storing and processing large amounts of data.

HDFS can be accessed by different applications using various interfaces, such as command-line, web, REST, and Java. The Java interface is the most commonly used one, as it provides a rich set of methods and classes for interacting with HDFS programmatically.

The Java interface for HDFS is based on the abstract FileSystem class, which represents a generic file system. HDFS is one of the implementations of this class, along with other file systems such as local, FTP, S3, etc. The FileSystem class provides methods for creating, deleting, renaming, copying, moving, reading, and writing files and directories on a file system.

To use the Java interface for HDFS, one needs to have the following dependencies in the project:

- hadoop-core: This contains the core classes and interfaces for Hadoop, such as Configuration, Path, FileSystem, etc.
- hadoop-common: This contains the common utilities and libraries for Hadoop, such as IO, security, serialization, etc.
- hadoop-hdfs: This contains the classes and interfaces for HDFS, such as DistributedFileSystem, FSDataInputStream, FSDataOutputStream, etc.

The following is a simplified ASCII diagram of the Java interface for HDFS:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Application   |      |   Application   |      |   Application   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   FileSystem    |      |   FileSystem    |      |   FileSystem    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   HDFS Client   |      |   HDFS Client   |      |   HDFS Client   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +----------------------+----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   NameNode      |      |   DataNode      |      |   DataNode      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows how multiple applications can use the FileSystem class to access HDFS. Each application creates an instance of the FileSystem class, which internally creates an instance of the HDFS client. The HDFS client communicates with the NameNode and the DataNodes to perform file system operations. The NameNode is the master node that manages the metadata and the namespace of HDFS. The DataNodes are the worker nodes that store and serve the data blocks of HDFS.