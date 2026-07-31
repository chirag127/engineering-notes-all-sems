HDFS is a distributed file system that runs on clusters of commodity hardware and is designed for storing very large files with streaming data access patterns. It is based on the Google File System and is a member of the Hadoop Ecosystem. HDFS has a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store the actual data blocks. HDFS provides fault tolerance, scalability, reliability, and high throughput of data access.

#### Design of HDFS

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Client       |  |    Client       |  |    Client       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         |                  |                  |
         +------------------+------------------+-----------------+
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         +------------------+------------------+-----------------+
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
         |                  |                  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    NameNode     |  |    DataNode     |  |    DataNode     |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```

The NameNode is the master node that maintains the namespace tree and the mapping of blocks to DataNodes. The NameNode also performs operations such as opening, closing, and renaming files and directories. The NameNode is a single point of failure in HDFS, and it is protected by a secondary NameNode that periodically checkpoints the namespace and edits log.

The DataNodes are the slave nodes that store the data blocks of the files. The DataNodes are responsible for serving read and write requests from the clients, and performing block creation, deletion, and replication as instructed by the NameNode. The DataNodes periodically send heartbeat and block report messages to the NameNode to report their status and block locations.

The clients are the applications that access the data stored in HDFS. The clients interact with the NameNode to obtain the metadata of the files, such as the locations of the blocks and the replication factor. The clients then directly communicate with the DataNodes to read or write the data blocks. The clients also perform data pipelining, where the output of one DataNode is forwarded as the input of another DataNode for the next block. This reduces the network bandwidth and increases the write performance.

HDFS supports a default block size of 128 MB, which is much larger than the block size of a typical file system. This is because HDFS is optimized for streaming large files, and a large block size reduces the overhead of managing the metadata and the number of disk seeks. HDFS also supports a default replication factor of 3, which means that each block is replicated on three different DataNodes for fault tolerance. The replication factor can be configured for each file or directory according to the application needs. HDFS also supports rack awareness, where the NameNode tries to place the replicas of a block on different racks to improve the availability and reliability of the data.