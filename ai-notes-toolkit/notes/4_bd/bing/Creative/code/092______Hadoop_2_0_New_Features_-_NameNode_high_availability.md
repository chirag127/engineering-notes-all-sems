#### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories .
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster, meaning that if the NameNode became unavailable, the whole cluster would be inaccessible.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes in an active/passive configuration with a hot standby     .
- This feature is called NameNode high availability (HA) and it allows for automatic failover of the NameNode in case of a failure or a planned maintenance     .
- The main components of NameNode HA are:
  - Active NameNode: the NameNode that is currently serving the client requests and updating the metadata  .
  - Standby NameNode: the NameNode that is in sync with the active NameNode and ready to take over in case of a failover  .
  - JournalNodes: a set of nodes that store the edit logs of the NameNodes and help in keeping them in sync   .
  - ZooKeeper: a service that monitors the health of the NameNodes and performs the failover when needed   .
  - Failover Controller: a daemon that runs on the same node as the NameNode and communicates with ZooKeeper and JournalNodes to perform the failover   .
- The benefits of NameNode HA are:
  - Improved availability and reliability of the HDFS cluster     .
  - Reduced downtime and data loss in case of a NameNode failure     .
  - Simplified administration and maintenance of the HDFS cluster     .