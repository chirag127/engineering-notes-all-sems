### Hadoop 2.0 New Features - NameNode high availability

Hadoop 2.0 introduced several new features, one of which is NameNode high availability. In Hadoop 1.0, NameNode was a single point of failure, which means that if the NameNode failed, the entire Hadoop cluster would become unavailable. This was a major issue for large-scale production environments, where downtime could result in significant financial losses. The NameNode high availability feature in Hadoop 2.0 addresses this issue by providing a highly available NameNode architecture.

The following are the key features of NameNode high availability in Hadoop 2.0:

1. Active and Standby NameNodes:
   - In Hadoop 2.0, NameNode high availability is achieved through the use of two NameNodes: an active NameNode and a standby NameNode.
   - The active NameNode is responsible for managing the Hadoop cluster, while the standby NameNode monitors the health of the active NameNode.
   - If the active NameNode fails, the standby NameNode takes over the cluster management responsibilities.

2. Quorum-based Journaling:
   - To ensure that both NameNodes have the same metadata, Hadoop 2.0 uses a quorum-based journaling mechanism.
   - Each NameNode maintains its own journal, and these journals are replicated to a set of journal nodes.
   - The active NameNode writes to a majority of the journal nodes, ensuring that the standby NameNode can read the same metadata.

3. Automatic Failover:
   - In the event of a NameNode failure, the standby NameNode automatically takes over the management responsibilities of the Hadoop cluster.
   - The failover process is automatic and transparent to Hadoop users, minimizing downtime and ensuring high availability.

4. Configurable Checkpoints:
   - To minimize the amount of metadata that needs to be replayed during failover, Hadoop 2.0 introduces configurable checkpoints.
   - Checkpoints are periodic snapshots of the Hadoop metadata, which are stored on the NameNodes' local disks.
   - During failover, the standby NameNode only needs to replay the metadata from the last checkpoint, reducing the recovery time.

In conclusion, NameNode high availability is a critical feature in Hadoop 2.0 that addresses one of the major limitations of Hadoop 1.0. Through the use of active and standby NameNodes, quorum-based journaling, automatic failover, and configurable checkpoints, Hadoop 2.0 provides a highly available NameNode architecture that is essential for large-scale production environments.