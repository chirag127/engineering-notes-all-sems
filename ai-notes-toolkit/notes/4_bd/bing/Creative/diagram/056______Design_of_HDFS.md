HDFS (Hadoop Distributed File System) is a big data distributed file system storage by Apache. It is designed to store very large files across machines in a large cluster, with high throughput and fault tolerance. HDFS is based on the Google File System  .

#### Design of HDFS

HDFS consists of two types of nodes: a NameNode and multiple DataNodes. The NameNode is the master node that manages the namespace and the metadata of the file system. The DataNodes are the worker nodes that store the actual data blocks of the files. The NameNode and the DataNodes communicate with each other using heartbeats and block reports. The NameNode also maintains the replication factor of each file, which is the number of copies of each data block stored on different DataNodes  .

The following diagram shows the basic design of HDFS:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Namespace      |    |  Data Block 1   |    |  Data Block 2   |
|  Metadata       |    |  Data Block 2   |    |  Data Block 3   |
|  Replication    |    |  Data Block 3   |    |  Data Block 4   |
|  Factor         |    |  Data Block 4   |    |  Data Block 5   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Heartbeats     |<-->|  Heartbeats     |    |  Heartbeats     |<-->|
|  Block Reports  |<-->|  Block Reports  |    |  Block Reports  |<-->|
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram illustrates how a file is split into data blocks and stored on different DataNodes. For example, a file with a size of 256 MB and a block size of 64 MB will be divided into four data blocks of 64 MB each. Each data block will be replicated on different DataNodes according to the replication factor. The default replication factor is 3, which means that each data block will have three copies on different DataNodes. The NameNode will keep track of the location and the status of each data block and DataNode. The NameNode will also handle the read and write requests from the clients, and coordinate the data transfer between the DataNodes  .