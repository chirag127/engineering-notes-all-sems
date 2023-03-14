#### Hadoop 2.0 New Features - NameNode high availability

In Hadoop 2.0, the NameNode high availability feature was introduced to address the single point of failure problem in Hadoop 1.x. This feature allows for automatic failover of the active NameNode to a standby NameNode in case of a failure, ensuring high availability and reliability of the Hadoop cluster.

Some of the key features and benefits of NameNode high availability in Hadoop 2.0 are:

1. **Automatic failover:** The active NameNode can automatically failover to a standby NameNode in case of a failure, without any manual intervention.

2. **No downtime:** Failover happens seamlessly and without any downtime, ensuring high availability of the Hadoop cluster.

3. **Shared storage:** The active and standby NameNodes share a common storage, ensuring that both have access to the same metadata and data.

4. **Quorum-based approach:** A quorum-based approach is used to ensure that only one NameNode is active at any given time, avoiding any conflicts that may arise due to multiple active NameNodes.

5. **ZooKeeper coordination:** ZooKeeper is used for coordinating between the active and standby NameNodes, ensuring that the failover process is smooth and seamless.

Some of the Mnemonics and learning tricks for remembering the NameNode high availability feature in Hadoop 2.0 are:

1. **HA = High Availability:** This is a simple mnemonic to remember that the NameNode high availability feature ensures high availability of the Hadoop cluster.

2. **Automatic Failover:** The term "automatic failover" itself can be used as a mnemonic to remember that the failover process happens automatically without any manual intervention.

3. **ZooKeeper coordination:** Remembering that ZooKeeper is used for coordinating between the active and standby NameNodes can help in understanding the technical details of the NameNode high availability feature.

Overall, the NameNode high availability feature in Hadoop 2.0 is a significant improvement over Hadoop 1.x, and ensures that Hadoop clusters are highly available and reliable.