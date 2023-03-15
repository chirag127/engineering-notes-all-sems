### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster. If the NameNode failed or became unavailable, the entire cluster would be inaccessible until the NameNode was restored or replaced.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes. It introduces Hadoop 2.0 High Availability feature that brings in an extra NameNode (Passive Standby NameNode) to the Hadoop Architecture which is configured for automatic failover  .
- The Active NameNode is the one that serves the client requests and performs the normal NameNode operations. The Standby NameNode is the one that maintains enough state to provide a fast failover if the Active NameNode fails.
- The Standby NameNode synchronizes its state with the Active NameNode by reading the shared edit logs and applying the changes to its own namespace. The shared edit logs can be stored in a shared storage system such as NFS or a Quorum Journal Manager (QJM) that uses a group of JournalNodes .
- The DataNodes send block reports and heartbeats to both the Active and the Standby NameNodes, so that both of them are aware of the cluster state and the block locations.
- The failover process can be triggered manually or automatically by a ZooKeeper-based Failover Controller (ZKFC) that monitors the health of the NameNodes and initiates the failover when needed .
- The failover process involves the following steps:
  - The ZKFC on the Active NameNode detects that the Active NameNode is unhealthy or unreachable and gives up its ZooKeeper lock.
  - The ZKFC on the Standby NameNode tries to acquire the ZooKeeper lock and becomes the new Active NameNode.
  - The new Active NameNode transitions to the active state and starts serving the client requests.
  - The old Active NameNode transitions to the standby state and starts synchronizing with the new Active NameNode.
- The Hadoop 2.0 High Availability feature enables the HDFS cluster to be available 24/7 and to tolerate the failure of a NameNode without losing data or disrupting the operations.