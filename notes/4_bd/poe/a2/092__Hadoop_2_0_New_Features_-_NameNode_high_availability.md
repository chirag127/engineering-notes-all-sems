 Here is the content in markdown format with formal tone and without emojis:

#### Hadoop 2.0 New Features - NameNode high availability

1. Introduction
- Hadoop 1.x had a single point of failure at the NameNode
- In Hadoop 2.0, NameNode high availability is achieved through a feature called Active/Passive NameNode. This removes the single point of failure and prevents downtime.

2. How it works
- There are two NameNodes in Active/Passive setup - a primary active NameNode and a secondary passive NameNode.
- The metadata is replicated to the secondary NameNode by the primary NameNode.
- The namenodes use a tool called the ZooKeeper to coordinate which NameNode is active and manage the state transitions.
- In case the primary NameNode fails, the secondary NameNode can take over as the primary and start serving read/write requests. The data is already in sync because of the replication.
- Once the primary NameNode is back, it again becomes active and starts replicating to the now passive NameNode.

3. Benefits
- Removes single point of failure for the NameNode
- Prevents downtime in case of NameNode failures through failover
- The data is always available and in sync on both the NameNodes

The content summarizes the key points around NameNode high availability in Hadoop 2.0 in a formal tone with points and without any emojis or external links. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.