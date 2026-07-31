#### Hadoop 2.0 New Features - NameNode high availability

- High Availability was a new feature added to Hadoop 2.x to solve the Single point of failure (SPOF) problem in the older versions of Hadoop.
- Hadoop 2.0 overcomes this SPOF shortcoming by providing support for multiple NameNodes .
- It introduces Hadoop 2.0 High Availability feature that brings in an extra NameNode (Passive Standby NameNode) to the Hadoop Architecture which is configured for automatic failover .
- The main motive of the Hadoop 2.0 High Availability project is to render availability to large data applications 24/7 through the deployment of 2 Hadoop Name Nodes.
- This eliminates the NameNode as a potential single point of failure (SPOF) in an HDFS cluster.