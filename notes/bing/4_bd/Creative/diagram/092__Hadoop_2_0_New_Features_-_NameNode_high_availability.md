Hadoop 2.0 New Features - NameNode high availability

Hadoop 2.0 introduced the feature of NameNode high availability to overcome the single point of failure (SPOF) problem in the older versions of Hadoop. In Hadoop 2.0, there are two NameNodes in the same cluster, one active and one passive (standby). The active NameNode is responsible for managing the file system namespace and coordinating the data nodes. The passive NameNode is a hot standby that maintains enough state to provide a fast failover if the active NameNode fails. The two NameNodes use a shared storage (such as NFS or Quorum Journal Manager) to store the edit log, which is a persistent record of changes made to the file system metadata. The data nodes send block reports and heartbeats to both NameNodes to keep them updated about the cluster state.

The following diagram illustrates the basic architecture of a Hadoop 2.0 cluster with NameNode high availability:

```
+----------------+     +----------------+
|                |     |                |
|   Active NN    |     |  Passive NN    |
|                |     |                |
+----------------+     +----------------+
|                |     |                |
|   Edit Log     |     |   Edit Log     |
|                |     |                |
+----------------+     +----------------+
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        +---------------------+
        |                     |
        |   Shared Storage    |
        |                     |
        +---------------------+
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        +---------------------+
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
+----------------+     +----------------+
|                |     |                |
|   Data Node    |     |   Data Node    |
|                |     |                |
+----------------+     +----------------+
```