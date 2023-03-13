Administering Hadoop in Hadoop Environment involves managing the Hadoop clusters and other resources in the Hadoop ecosystem. A Hadoop administrator is responsible for installing, configuring, monitoring, and troubleshooting the Hadoop daemons and services. The basic architecture of a Hadoop cluster consists of a master node and multiple worker nodes. The master node runs the NameNode and the ResourceManager services, which are responsible for managing the metadata and the resources of the cluster. The worker nodes run the DataNode and the NodeManager services, which are responsible for storing the data and executing the tasks. The Hadoop administrator can use the Hadoop shell commands and the web interfaces to interact with the cluster and perform various operations.

The following diagram illustrates the basic architecture of a Hadoop cluster using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    | SecondaryNameNode |  |    ResourceManager |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        ^                      ^                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        ^                      ^                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NodeManager  |    |    NodeManager  |    |    NodeManager  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```