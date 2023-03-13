## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

HDFS is a distributed file system that runs on commodity hardware and provides high availability, fault tolerance, scalability, and high throughput access to large data sets. HDFS is designed to store and process data in a parallel and distributed manner using the MapReduce framework.

The basic architecture of HDFS consists of the following components:

- **NameNode**: The master node that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the file system, such as the file and directory structure, the permissions, and the locations of the blocks that make up the files. The NameNode is a single point of failure in HDFS, and it is usually configured with a backup node or a secondary node for recovery purposes.
- **DataNode**: The slave node that stores the actual data blocks of the files in the local disks. Each block is typically 64 MB or 128 MB in size, and a file can have one or more blocks. The DataNodes are responsible for serving read and write requests from the clients, and also perform block creation, deletion, and replication upon instruction from the NameNode.
- **Secondary NameNode**: An optional node that periodically merges the namespace image and the edit log from the NameNode, and sends the updated image back to the NameNode. This reduces the startup time of the NameNode and the size of the edit log. The secondary NameNode is not a backup for the NameNode, as it does not store the entire file system state.
- **Checkpoint Node**: An alternative to the secondary NameNode that creates checkpoints of the namespace by downloading the edit log from the NameNode and applying it to a local copy of the namespace image. The checkpoint node then uploads the new image back to the NameNode, which can use it to restart in case of a failure.
- **Backup Node**: Another alternative to the secondary NameNode that provides a backup for the NameNode. The backup node maintains an in-memory copy of the file system namespace, which is always synchronized with the NameNode. The backup node can also create checkpoints of the namespace, and can take over the role of the NameNode in case of a failure.

The following diagram illustrates the basic architecture of HDFS using ASCII art:

```
+----------------+            +----------------+
|                |            |                |
|   NameNode     |            | Secondary      |
|                |            | NameNode       |
|                |            |                |
+----------------+            +----------------+
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
| DN1  | DN2  | DN3  | DN4  | DN5  | DN6  | DN7  |
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
```

DN = DataNode