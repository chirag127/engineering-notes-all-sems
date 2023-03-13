#### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the filesystem tree and the metadata of all the files and directories.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster. If the NameNode failed, the cluster would become unavailable until the NameNode was manually recovered or restarted on another machine.
- Hadoop 2.0 overcomes this SPOF problem by providing support for multiple NameNodes. It introduces Hadoop 2.0 High Availability feature that enables running redundant NameNodes in the same cluster in an Active/Passive configuration with a hot standby.
- The Active NameNode is the one that serves the client requests and performs all the namespace operations. The Standby NameNode is the one that maintains enough state to provide a fast failover if the Active NameNode fails.
- The Standby NameNode synchronizes its state with the Active NameNode by reading the shared edit logs and applying the namespace changes to its own in-memory filesystem image. The shared edit logs can be stored in a shared storage system such as NFS or a Quorum Journal Manager (QJM).
- The DataNodes send block reports and heartbeat messages to both the Active and the Standby NameNodes. This allows the Standby NameNode to keep track of the cluster block locations and to take over the block management if the Active NameNode fails.
- The failover process can be triggered manually or automatically by using a ZooKeeper-based Failover Controller (ZKFC). The ZKFC is a daemon that runs on the same machine as the NameNode and monitors its health. It also uses ZooKeeper to perform leader election and to ensure that there is only one Active NameNode at a time.
- The advantages of Hadoop 2.0 High Availability feature are:
  - It eliminates the NameNode as a potential single point of failure in an HDFS cluster.
  - It provides a fast and automatic failover mechanism that minimizes the downtime and data loss in case of NameNode failure.
  - It simplifies the administration and maintenance of HDFS clusters by avoiding the need for manual intervention or backup and restore procedures.
- The disadvantages of Hadoop 2.0 High Availability feature are:
  - It introduces additional complexity and overhead in the HDFS architecture and configuration.
  - It requires a reliable and secure shared storage system for the edit logs and a reliable and secure ZooKeeper ensemble for the leader election and coordination.
  - It may not guarantee a consistent view of the filesystem across the Active and the Standby NameNodes in some rare scenarios, such as network partition or split-brain.

- A possible mnemonic to remember the main components of Hadoop 2.0 High Availability feature is:

  - **A**ctive NameNode
  - **S**tandby NameNode
  - **S**hared edit logs
  - **Z**ooKeeper
  - **Z**KFC

  - **ASSZZ** (sounds like "as is")