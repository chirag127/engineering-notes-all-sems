 Here is the content in markdown format for the topic #### Hadoop 2.0 New Features - NameNode high availability:

#### Hadoop 2.0 New Features - NameNode high availability

- **Active/Standby Architecture:** In Hadoop 2.0, the NameNode high availability is achieved through an active/standby architecture with two NameNodes - a primary/active NameNode and a secondary/standby NameNode. At any given time, only one NameNode is active and serving all the client requests. The standby NameNode remains on standby mode and takes over the active NameNode if it fails. This ensures there is no single point of failure for the NameNode.
- **Checkpoints:** The edits files are continuously checkpointed into the fsimage file by the active NameNode. The timestamps of the checkpoint are also updated in the edit logs. In case of a failover, the standby NameNode can load the latest fsimage file and apply only those edit logs which have timestamps after the most recent checkpoint. This reduces the amount of data that the standby NameNode needs to process during a failover.
- **ZooKeeper for Coordination:** ZooKeeper is used for coordinating between the active and standby NameNodes. It stores configuration information and manages the failover process. ZooKeeper monitors the health of the active NameNode and triggers an automatic failover if the active NameNode fails. It also manages the reconciliation process to ensure both NameNodes have the same namespace when the original active NameNode comes back up.

**Advantages:**
- Prevents single point of failure and provides high availability for the NameNode
- Faster failover process through checkpointing and editing logging
- Automatic failover is handled by ZooKeeper without manual intervention

**Disadvantages:**
- Additional complexity of setting up and managing an active/standby architecture
- Additional resources required to run two NameNodes

**Applications:** Hadoop 2.0 with NameNode high availability is ideal for mission-critical Hadoop clusters where high availability of the NameNode is essential.