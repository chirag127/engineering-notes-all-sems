# HDFS Federation

- HDFS Federation is a feature of Hadoop 2.x that allows multiple NameNodes to manage different namespaces in the same cluster.
- Each NameNode is independent and does not communicate with other NameNodes.
- Each namespace is associated with a block pool, which is a set of blocks that belong to the files in that namespace.
- DataNodes store blocks from multiple block pools and report them to the respective NameNodes.
- HDFS Federation improves the scalability, performance, and isolation of the HDFS architecture.
- HDFS Federation also enables future innovations such as multiple file systems and storage types.

## Architecture of HDFS Federation

- The architecture of HDFS Federation consists of the following components:

  - Namespace Volume: A self-contained unit of management that includes a namespace and a block pool. A namespace volume can be created, deleted, or upgraded independently.
  - NameNode: A daemon that manages a namespace volume. It maintains the file system metadata, such as the file system tree, file permissions, and file locations. It also performs file system operations, such as creating, deleting, and renaming files and directories.
  - DataNode: A daemon that stores and serves blocks from multiple block pools. It periodically sends block reports and heartbeats to the NameNodes that manage the block pools it belongs to.
  - Block Pool ID: A globally unique identifier for a block pool. It is assigned to a block pool when it is created and remains unchanged throughout its lifetime.
  - Namespace ID: A globally unique identifier for a namespace. It is assigned to a namespace when it is created and remains unchanged throughout its lifetime.
  - Client: A user or an application that accesses the HDFS file system. It interacts with the NameNode to perform file system operations and with the DataNode to read and write data blocks.

- The following diagram illustrates the architecture of HDFS Federation:

![HDFS Federation Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/images/federation.png)

- In this diagram, there are three namespace volumes, each managed by a different NameNode. Each namespace volume has a different block pool ID and namespace ID. The DataNodes store blocks from all three block pools and report them to the corresponding NameNodes. The clients can access any of the namespaces by specifying the NameNode address or using a logical URI that maps to a NameNode.