#### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster, meaning that if the NameNode became unavailable, the entire cluster would be inaccessible.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes in an Active/Passive configuration with a hot standby  .
- This feature is called NameNode high availability (HA) and it allows the cluster to continue working even if the Active NameNode fails or is shut down for maintenance  .
- The Passive NameNode, also called the Standby NameNode, is synchronized with the Active NameNode through a shared storage system (such as NFS or Quorum Journal Manager) and a heartbeat mechanism   .
- The shared storage system stores the edit logs and the fsimage of the HDFS namespace, which are updated by the Active NameNode and read by the Standby NameNode   .
- The heartbeat mechanism monitors the health of the Active NameNode and triggers a failover process if it detects a failure   .
- The failover process involves the Standby NameNode taking over the role of the Active NameNode and the DataNodes and clients switching to the new Active NameNode   .
- The failover process can be either manual or automatic, depending on the configuration of the cluster   .
- The NameNode HA feature improves the reliability, availability, and scalability of HDFS and enables the cluster to run large data applications 24/7  .