#### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster, meaning that if the NameNode became unavailable, the entire cluster would be inaccessible.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes in an Active/Passive configuration with a hot standby  .
- This feature is called NameNode high availability (HA) and it allows the cluster to continue working even if the Active NameNode fails or is shut down for maintenance  .
- The Passive NameNode, also called the Standby NameNode, is configured for automatic failover, meaning that it can take over the role of the Active NameNode in case of a failure  .
- The Standby NameNode keeps its state synchronized with the Active NameNode by reading the shared edit logs and applying the same namespace changes .
- The shared edit logs can be stored in a shared storage system, such as NFS or a Quorum Journal Manager (QJM), which is a dedicated Hadoop daemon that coordinates updates from multiple NameNodes .
- The failover process can be triggered manually or automatically by a ZooKeeper-based Failover Controller (ZKFC), which monitors the health of the NameNodes and initiates the failover when needed .
- The DataNodes and the clients are aware of both the NameNodes and can switch to the new Active NameNode after the failover .
- NameNode HA improves the reliability and availability of the HDFS cluster and reduces the downtime and data loss caused by NameNode failures  .