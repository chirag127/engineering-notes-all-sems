# Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories in the cluster.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster, meaning that if the NameNode machine or process became unavailable, the cluster would be inaccessible until the NameNode was restored or replaced.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes in an HDFS cluster, which is called NameNode high availability (HA) feature .
- NameNode HA feature introduces an extra NameNode (called Passive Standby NameNode) to the Hadoop architecture, which is configured for automatic failover in case of the Active NameNode failure .
- The Active NameNode and the Passive Standby NameNode use a shared storage (such as NFS or Quorum Journal Manager) to store the edit logs, which are the transactions that modify the filesystem metadata .
- The Passive Standby NameNode keeps reading the edit logs from the shared storage and applies them to its own namespace image in memory, so that it is always synchronized with the Active NameNode .
- The DataNodes in the cluster send block reports and heartbeats to both the Active and the Passive NameNodes, so that both of them are aware of the cluster status .
- The clients that access the HDFS cluster use a configuration that lists both the NameNodes, and use ZooKeeper to determine which one is the Active NameNode at any given time .
- If the Active NameNode fails or becomes unresponsive, ZooKeeper will trigger a failover process that will make the Passive Standby NameNode take over the role of the Active NameNode, and update the configuration of the clients and the DataNodes accordingly .
- The NameNode HA feature enables the HDFS cluster to be highly available and resilient to NameNode failures, without compromising the performance or the consistency of the filesystem .