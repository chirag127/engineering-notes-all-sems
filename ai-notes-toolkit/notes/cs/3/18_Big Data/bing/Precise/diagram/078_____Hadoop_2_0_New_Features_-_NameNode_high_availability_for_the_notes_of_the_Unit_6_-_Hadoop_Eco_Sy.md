### Hadoop 2.0 New Features - NameNode high availability

- High Availability was a new feature added to Hadoop 2.x to solve the Single point of failure problem in the older versions of Hadoop.
- As the Hadoop HDFS follows the master-slave architecture where the NameNode is the master node and maintains the filesystem tree.
- Hadoop 2.0 overcomes this shortcoming in the SPOF by providing multiple Name Nodes support.
- It introduces Hadoop 2.0 High Availability feature that brings to the Hadoop Architecture an extra Name Node (Passive Standby Name Node) configured for automatic failover.
- The main motive of the Hadoop 2.0 High Availability project is to render availability to large data applications 24/7 through the deployment of 2 Hadoop Name Nodes. One in active configuration and the other is the passive Standby Node.
- The high availability feature in Hadoop ensures the availability of the Hadoop cluster without any downtime, even in unfavorable conditions like NameNode failure, DataNode failure, machine crash, etc.
- It means if the machine crashes, data will be accessible from another path.