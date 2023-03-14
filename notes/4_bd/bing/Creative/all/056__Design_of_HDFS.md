#### Design of HDFS

HDFS stands for Hadoop Distributed File System. It is a distributed file system that runs on commodity hardware and provides high throughput access to large data sets. HDFS is designed for batch processing rather than interactive use by users. HDFS is part of the Apache Hadoop project and is based on the Google File System.

Some of the key features and assumptions of HDFS are:

- Hardware failure is the norm rather than the exception. HDFS is highly fault-tolerant and can automatically recover from failures of nodes or disks.
- Applications that run on HDFS need streaming access to their data sets. HDFS supports write-once-read-many access model for files and relaxes some POSIX requirements to enable streaming data access.
- Applications that run on HDFS have large data sets. A typical file in HDFS is gigabytes to terabytes in size. HDFS is tuned to support large files and provides high aggregate data bandwidth.
- HDFS has a simple coherency model. Files are appended to or overwritten, but not modified. Once a file is written, it is visible to all readers without any explicit flushing or closing.
- HDFS follows the principle of "moving computation is cheaper than moving data". HDFS tries to locate the computation near the data to reduce network traffic and improve performance.
- HDFS is portable across heterogeneous hardware and software platforms. HDFS is written in Java and can run on various operating systems.

The main components of HDFS are:

- NameNode: The NameNode is the master node that manages the file system namespace and the metadata of files and directories. It also controls the access to files by clients. There is only one NameNode in a cluster and it is a single point of failure. To overcome this, HDFS supports a secondary NameNode that can periodically merge the namespace image with the edit log to prevent the edit log from becoming too large. HDFS also supports a high-availability mode where two NameNodes run in the same cluster in an active-standby configuration.
- DataNode: The DataNode is the slave node that stores the actual data in files. A file is split into one or more blocks and these blocks are stored in a set of DataNodes. The DataNodes are responsible for serving read and write requests from clients, performing block creation, deletion, and replication as instructed by the NameNode, and sending periodic heartbeats and block reports to the NameNode.
- Client: The client is the application that accesses the file system. The client communicates with the NameNode to perform file system operations such as opening, closing, renaming, or deleting files or directories. The client also communicates with the DataNodes to read or write data to or from the blocks.

The following diagram illustrates the design of HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Client       |    |    Client       |    |    Client       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
        |