#### Hadoop 2.0 New Features - NameNode high availability

- NameNode is the master node in HDFS that maintains the file system metadata and controls access to files by clients.
- In Hadoop 1.x, NameNode was a single point of failure (SPOF) in an HDFS cluster. If the NameNode machine or process became unavailable, the entire cluster would be inaccessible until the NameNode was restored or replaced.
- Hadoop 2.0 introduced the High Availability (HA) feature to overcome the SPOF problem by providing support for multiple NameNodes in the same cluster.
- In HA mode, two NameNodes are configured as Active and Standby. The Active NameNode is responsible for all client operations, while the Standby NameNode maintains enough state to provide a fast failover if necessary.
- The Active and Standby NameNodes use a shared storage device (such as NFS) or a Quorum Journal Manager (QJM) to synchronize their edit logs. The edit log records every change made to the file system metadata by the Active NameNode.
- The Standby NameNode applies the edit log to its own namespace in memory and also creates checkpoints of the namespace. A checkpoint is a compact representation of the file system metadata, which reduces the recovery time of the NameNode.
- The Standby NameNode can also perform read-only operations such as listing files or getting file locations, which can improve the performance of the Active NameNode by offloading some of the read requests.
- The HA feature also uses a ZooKeeper Failover Controller (ZKFC) to monitor the health of the NameNodes and perform failover when needed. The ZKFC is a daemon that runs on each NameNode machine and communicates with a ZooKeeper quorum.
- The ZKFC uses a simple heartbeat mechanism to check if the NameNode is running and also verifies that it is either Active or Standby. The ZKFC also uses ZooKeeper to perform leader election and ensure that there is only one Active NameNode at a time.
- If the Active NameNode fails or becomes unresponsive, the ZKFC on the Standby NameNode will try to acquire a lock in ZooKeeper and make the Standby NameNode Active. The ZKFC on the failed NameNode will release the lock and make the NameNode Standby when it recovers.
- The HA feature also requires the DataNodes and the clients to be configured to support failover. The DataNodes send block reports and heartbeats to both NameNodes and receive commands from the Active NameNode. The clients use a logical URI to access the file system and get the address of the Active NameNode from the ZKFC or a configuration file.

- The advantages of using HA mode are:

  - It eliminates the NameNode as a potential single point of failure and improves the availability and reliability of the HDFS cluster.
  - It allows a fast and automatic failover to a new NameNode in case of a machine crash or a planned maintenance event.
  - It reduces the recovery time of the NameNode by using checkpoints and edit log synchronization.
  - It improves the performance of the Active NameNode by offloading some of the read requests to the Standby NameNode.

- The disadvantages of using HA mode are:

  - It adds complexity and overhead to the HDFS architecture and configuration.
  - It requires additional hardware resources and network bandwidth for the Standby NameNode and the shared storage or QJM.
  - It may introduce some inconsistency or data loss in the file system metadata if the edit log synchronization fails or the shared storage or QJM becomes unavailable.

- A mnemonic to remember the components of HA mode is:

  - **N**ameNodes (Active and Standby)
  - **E**dit log (shared or QJM)
  - **Z**ooKeeper (quorum and ZKFC)
  - **D**ataNodes and clients (failover support)

- An example of an ASCII diagram of HA mode is:

```
  +-----------------+  +-----------------+
  | Active NameNode |  | Standby NameNode|
  +-----------------+  +-----------------+
  | ZKFC            |  | ZKFC            |
  +-----------------+  +-----------------+
         |  ^                 |  ^
         |  |                 |  |
         v  |                 v  |
  +-----------------+  +-----------------+
  | Edit log (NFS/QJM) | Checkpoint      |
  +-----------------+  +-----------------+
         |  ^
         |