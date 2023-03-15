## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

Here is an ASCII diagram of the Hadoop Distributed File System (HDFS) and Hadoop Environment:

```
+-----------------+      +-----------------+
| NameNode        |      | DataNode        |
|                 |      |                 |
|  +-----------+  |      |  +-----------+  |
|  | FS Image  |  |      |  | Block 1   |  |
|  +-----------+  |      |  +-----------+  |
|  +-----------+  |      |  +-----------+  |
|  | Edit Logs |  |      |  | Block 2   |  |
|  +-----------+  |      |  +-----------+  |
|                 |      |  +-----------+  |
|                 |      |  | Block 3   |  |
|                 |      |  +-----------+  |
+-----------------+      +-----------------+
```

The NameNode is the master node in the Hadoop Distributed File System (HDFS) and is responsible for managing the file system namespace and regulating access to files by clients. The NameNode stores the metadata for the file system, including the file system tree and the mapping of blocks to DataNodes. The FS Image is a file that contains the entire file system namespace, while the Edit Logs record changes to the file system.

The DataNode is a slave node in the Hadoop Distributed File System (HDFS) and is responsible for storing the data blocks of files. Each DataNode stores a set of blocks and periodically sends a report of all the blocks it is storing to the NameNode. The NameNode uses this information to ensure that the data is replicated across multiple DataNodes for fault tolerance.
