

#### Hadoop 2.0 New Features - NameNode High Availability

* Hadoop 2.0 introduces a new feature called NameNode High Availability (HA). This feature provides a redundant NameNode and eliminates the single point of failure in the cluster.
* The NameNode HA feature is implemented using a pair of NameNodes in an Active/Passive configuration. The active NameNode is responsible for all client operations and the passive NameNode is used for failover in case of an unexpected failure.
* To ensure data consistency between the two NameNodes, the active NameNode continuously sends a stream of edits to the passive NameNode. This is done using a quorum-based storage mechanism called JournalNodes.
* The NameNode HA feature also provides an automated failover mechanism. In the event of an unexpected failure, the passive NameNode will automatically take over as the active NameNode, ensuring that the cluster is still available.
* The NameNode HA feature also provides a number of other benefits such as improved scalability, better resource utilization, and improved performance.
* The NameNode HA feature is a great addition to the Hadoop platform and provides a reliable and redundant system for managing the cluster.

Mnemonic for remembering NameNode High Availability:

* NHA: NameNode High Availability