Hadoop 2.0 New Features - NameNode high availability

Hadoop 2.0 introduced the feature of high availability for NameNode, which is the master node of HDFS that maintains the file system metadata and controls access to files. In the previous versions of Hadoop, NameNode was a single point of failure (SPOF), meaning that if it crashed or became unavailable, the entire cluster would be inaccessible until it was restored or replaced. This could cause data loss, downtime, and performance degradation.

To overcome this limitation, Hadoop 2.0 allows running two NameNodes in the same cluster, one in active state and the other in standby state. The active NameNode is responsible for all client operations, while the standby NameNode keeps its state synchronized with the active one by reading the same edit logs from a shared storage device (such as NFS or QJM). The standby NameNode can also perform periodic checkpoints of the namespace by creating fsimage files. In case of a failure or maintenance of the active NameNode, the standby NameNode can take over the role of the active one by using a failover mechanism. This mechanism can be either manual or automatic, depending on the configuration of the cluster.

The following diagram illustrates the basic architecture of a Hadoop 2.0 cluster with NameNode high availability using NFS as the shared storage:

```
+-----------------+    +-----------------+
| Active NameNode |    | Standby NameNode|
+-----------------+    +-----------------+
|                 |    |                 |
|  fsimage        |    |  fsimage        |
|  edits          |    |  edits          |
|                 |    |                 |
+--------+--------+    +--------+--------+
         |                     |
         |                     |
         |                     |
         |                     |
         |                     |
         |                     |
         |                     |
         +----------+----------+
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
                    |
                    |
+-----------------+
| NFS Shared Mount |
+-----------------+
|                 |
|  fsimage        |
|  edits          |
|                 |
+-----------------+
```