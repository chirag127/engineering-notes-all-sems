### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster. If the NameNode machine or process became unavailable, the cluster would be inaccessible until the NameNode was restarted or brought up on a different machine.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes. It introduces Hadoop 2.0 High Availability feature that brings in an extra NameNode (Passive Standby NameNode) to the Hadoop Architecture which is configured for automatic failover  .
- The Active NameNode is responsible for all client operations, while the Standby NameNode maintains enough state to provide a fast failover if necessary.
- The two NameNodes use a shared storage directory to keep their states synchronized. The shared storage can be a NFS mount, a Quorum Journal Manager (QJM), or a ZooKeeper Failover Controller (ZKFC) .
- The DataNodes send block reports and heartbeats to both NameNodes, and the Standby NameNode performs checkpoints of the namespace state.
- In case of a failure of the Active NameNode, the Standby NameNode takes over the role of the Active NameNode after ensuring that it has read all the edits from the shared storage. The failover process is transparent to the clients, who can continue to access the HDFS cluster .
- The Hadoop 2.0 High Availability feature enables the HDFS cluster to be available 24/7 for large data applications, and eliminates the need for manual intervention in case of NameNode failures.