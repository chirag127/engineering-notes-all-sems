HDFS federation is a feature of Hadoop 2 that allows multiple independent NameNodes to manage different namespaces in the same cluster. Each NameNode has its own block pool, which is a set of blocks that belong to a single namespace. The DataNodes store blocks for all the block pools and register with all the NameNodes. This way, the cluster can scale horizontally and overcome the limitations of a single NameNode architecture.

The following diagram illustrates the basic architecture of HDFS federation in Hadoop ecosystem using ASCII characters:

```
+-----------------+    +-----------------+    +-----------------+
| NameNode 1      |    | NameNode 2      |    | NameNode 3      |
| Namespace 1     |    | Namespace 2     |    | Namespace 3     |
| Block Pool 1    |    | Block Pool 2    |    | Block Pool 3    |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
| DataNode 1      |    | DataNode 2      |    | DataNode 3      |
| Block Pool 1    |    | Block Pool 1    |    | Block Pool 1    |
| Block Pool 2    |    | Block Pool 2    |    | Block Pool 2    |
| Block Pool 3    |    | Block Pool 3    |    | Block Pool 3    |
+-----------------+    +-----------------+    +-----------------+
```