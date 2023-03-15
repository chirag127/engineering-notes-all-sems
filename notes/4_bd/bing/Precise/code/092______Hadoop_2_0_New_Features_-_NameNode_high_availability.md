#### Hadoop 2.0 New Features - NameNode high availability

- Hadoop 2.0 introduced the High Availability feature to solve the Single Point of Failure (SPOF) problem in older versions of Hadoop .
- The Hadoop HDFS follows a master-slave architecture where the NameNode is the master node and maintains the filesystem tree .
- Hadoop 2.0 overcomes the SPOF shortcoming by providing support for multiple NameNodes  .
- It introduces an extra NameNode (Passive Standby NameNode) to the Hadoop Architecture, which is configured for automatic failover  .
- The main motive of the Hadoop 2.0 High Availability project is to render availability to large data applications 24/7 through the deployment of 2 Hadoop NameNodes .
- This eliminates the NameNode as a potential single point of failure (SPOF) in an HDFS cluster .