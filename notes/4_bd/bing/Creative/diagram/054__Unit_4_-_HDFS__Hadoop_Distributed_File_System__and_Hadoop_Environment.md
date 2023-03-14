## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

HDFS is a distributed file system that runs on commodity hardware and provides high throughput access to large data sets. HDFS has a master/slave architecture, where a single NameNode manages the file system namespace and coordinates the access to files by clients, and multiple DataNodes store the actual data blocks on local disks. HDFS also replicates the data blocks across different DataNodes to achieve fault tolerance and high availability.

The following diagram illustrates the basic architecture of HDFS using ASCII characters:

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
        +---------------------+---------------------+
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
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    | Secondary       |    | Backup          |
|                 |    | NameNode        |    | NameNode        |
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
        +---------------------+---------------------+
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
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
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
        +---------------------+---------------------+
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
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the following components and relationships:

- Clients are the applications that access the HDFS file system to read or write data.
- NameNode is the master server that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the file system, such as the file names, directories, permissions, and locations of the data blocks.
- Secondary NameNode is a helper node that periodically merges the namespace image and the edit log from the NameNode to prevent the edit log from becoming too large. It also acts as a backup for the NameNode in case of failure.
- Backup NameNode is another helper node that provides a checkpointing service for the NameNode. It keeps an in-memory copy of