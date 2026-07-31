
### Hadoop 2.0 New Features - NameNode High Availability

* Hadoop 2.0 introduced NameNode High Availability (HA) to ensure that the cluster remains available in the event of a NameNode failure.
* In order to implement HA, a pair of NameNodes are created and run in an Active/Passive configuration. The active NameNode handles all client operations, while the passive NameNode acts as a standby, constantly monitoring the active NameNode.
* In the event of the active NameNode failing, the passive NameNode will take over as the active NameNode, ensuring that the cluster remains available.
* Hadoop Eco System and YARN are two components of the Hadoop framework which are used to process and manage Big Data.
* Hadoop Eco System consists of various components such as Hadoop Common, Hadoop Distributed File System (HDFS), MapReduce and YARN.
* YARN is a resource management platform that is responsible for managing resources in the cluster and scheduling applications.
* YARN also provides a framework for developing distributed applications on top of Hadoop.
* With NameNode High Availability, Hadoop 2.0 provides a reliable and highly available platform for managing and processing Big Data.