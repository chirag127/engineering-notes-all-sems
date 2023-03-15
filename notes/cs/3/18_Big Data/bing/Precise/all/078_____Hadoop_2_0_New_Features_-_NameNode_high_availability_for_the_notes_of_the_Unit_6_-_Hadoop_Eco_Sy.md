# Hadoop 2.0 New Features - NameNode High Availability

- High Availability was a new feature added to Hadoop 2.x to solve the Single point of failure problem in the older versions of Hadoop.
- As the Hadoop HDFS follows the master-slave architecture where the NameNode is the master node and maintains the filesystem tree.
- Hadoop 2.0 overcomes this shortcoming in the SPOF by providing multiple Name Nodes support.
- It introduces Hadoop 2.0 High Availability feature that brings to the Hadoop Architecture an extra Name Node (Passive Standby Name Node) configured for automatic failover.
- The high availability feature in Hadoop ensures the availability of the Hadoop cluster without any downtime, even in unfavorable conditions like NameNode failure, DataNode failure, machine crash, etc.
- It means if the machine crashes, data will be accessible from another path.
- The HDFS NameNode High Availability feature enables you to run redundant NameNodes in the same cluster in an Active/Passive configuration with a hot standby.
- This eliminates the NameNode as a potential single point of failure (SPOF) in an HDFS cluster.