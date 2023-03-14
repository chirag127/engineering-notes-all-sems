A cluster specification in Hadoop environment describes how to install, configure and manage a Hadoop cluster that consists of a network of master and slave nodes that are connected to each other. A Hadoop cluster is designed to store and analyze large amounts of structured, semi-structured, and unstructured data in a distributed environment. It is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.

The following diagram illustrates the basic architecture of a Hadoop cluster:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    NameNode     |       | SecondaryNameNode |     |  JobHistoryServer |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    DataNode     |       |    DataNode     |       |    DataNode     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    NodeManager  |       |    NodeManager  |       |    NodeManager  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    TaskTracker  |       |    TaskTracker  |       |    TaskTracker  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The master nodes are the NameNode, the SecondaryNameNode and the JobHistoryServer. The NameNode is responsible for managing the HDFS namespace and the metadata of the files and directories stored on the cluster. The SecondaryNameNode is a helper daemon that performs periodic checkpoints of the namespace and helps the NameNode recover from failures. The JobHistoryServer is a service that keeps track of the completed MapReduce jobs and their statistics.

The slave nodes are the Data