#### Hadoop 2.0 New Features - NameNode high availability

One of the major issues faced by Hadoop 1.x was the NameNode being a single point of failure. Hadoop 2.0 introduced the feature of NameNode high availability to overcome this issue. This feature allows multiple NameNodes to run in an active-passive mode, where one NameNode is active while the other(s) remain in standby mode. In the event of a failure of the active NameNode, the standby NameNode takes over without affecting the current running jobs.

Here are some of the features of NameNode high availability:

1. **Quorum-based storage:** The NameNodes use a quorum-based storage mechanism to maintain the metadata of the Hadoop Distributed File System (HDFS). The metadata is stored in a shared storage called the Quorum Journal Manager (QJM), which is replicated across multiple nodes. This ensures that data is not lost even in the event of a failure of one or more nodes.

2. **Automatic failover:** The standby NameNode constantly monitors the health of the active NameNode. In case of a failure, it automatically takes over the responsibilities of the active NameNode. This ensures minimal downtime and uninterrupted service to the users.

3. **Fencing:** Fencing is a mechanism used to ensure that only one NameNode is active at a time. In case of a split-brain scenario, where both NameNodes think they are active, fencing ensures that one NameNode is fenced off from the cluster, preventing it from causing any damage to the data.

4. **Configuration changes:** The configuration changes required to enable NameNode high availability are minimal. It involves setting up the QJM and configuring the NameNodes to use it.

Some mnemonics and learning tricks that can be helpful for remembering the features of NameNode high availability are:

- QJM stands for Quorum Journal Manager, which is the shared storage mechanism used by the NameNodes.
- Automatic failover ensures that there is no fail in the system.
- Fencing ensures that only one NameNode is active at a time, like a fence separating two gardens.

Overall, NameNode high availability is a crucial feature of Hadoop 2.0 that ensures continuous availability of the HDFS even in the event of a failure of the active NameNode. It provides a reliable and fault-tolerant infrastructure for big data processing.