
### Fault-tolerant Services for Unit 10 - Replication in DISTRIBUTED SYSTEM

* Fault-tolerant services are services that are designed to remain operational even when there are faults in the system.
* Fault-tolerant services are designed to be resilient to hardware, software, and network failures.
* Replication is a fault-tolerance technique in which multiple copies of data are stored across multiple nodes in a distributed system.
* Replication ensures that data is available even if one or more nodes fail.
* Replication also improves performance by allowing multiple nodes to access the same data simultaneously.
* Replication strategies include primary-backup, active-active, and quorum-based replication.
* Primary-backup replication involves creating a single primary node that is responsible for writing data, and multiple backup nodes that replicate the data from the primary node.
* Active-active replication involves creating multiple nodes that are all responsible for writing data.
* Quorum-based replication involves creating multiple nodes that are responsible for writing data, and a quorum of nodes that must agree on the data before it is written.
* Fault-tolerant services must be designed to handle various types of errors, such as network delays, node failures, and data corruption.
* Fault-tolerant services must also be designed to ensure that data is consistent across all nodes in the system.