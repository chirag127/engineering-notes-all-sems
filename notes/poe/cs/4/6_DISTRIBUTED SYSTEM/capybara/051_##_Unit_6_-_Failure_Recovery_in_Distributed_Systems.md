## Unit 6 - Failure Recovery in Distributed Systems

In distributed systems, failure is inevitable. Therefore, it is important to have a mechanism in place to recover from failures. This unit focuses on various techniques and strategies for failure recovery in distributed systems.

### 1. Redundancy

Redundancy is the duplication of components or systems in order to increase reliability. There are two types of redundancy:

- **Hardware redundancy:** This involves duplicating the physical hardware components of a system, such as servers, disks, and network connections. If one component fails, the system can continue to function using the duplicate component.

- **Software redundancy:** This involves duplicating the software components of a system, such as processes and data. If one component fails, the duplicate component can take over.

### 2. Replication

Replication involves creating multiple copies of data or services and distributing them across different nodes in a distributed system. If one node fails, another node can take over and continue to provide the service. There are two types of replication:

- **Active replication:** In this approach, all replicas receive the same requests and execute them in parallel. The results are then compared and any discrepancies are resolved. This approach provides high availability but can be expensive in terms of network and computational resources.

- **Passive replication:** In this approach, one replica is designated as the primary and receives all requests. The other replicas are passive and only become active if the primary fails. This approach is more efficient but may result in some downtime during failover.

### 3. Checkpointing

Checkpointing involves periodically saving the state of a distributed system to disk. If the system fails, it can be restarted from the last checkpoint instead of starting from scratch. Checkpointing can be done at different levels:

- **Process-level checkpointing:** This involves saving the state of individual processes.

- **System-level checkpointing:** This involves saving the state of the entire system.

### 4. Failure Detection

Failure detection involves detecting when a component or node in a distributed system has failed. There are two approaches to failure detection:

- **Heartbeat-based detection:** In this approach, each node sends periodic heartbeat messages to its neighbors. If a node does not receive a heartbeat from a neighbor within a certain time interval, it assumes that the neighbor has failed.

- **Timeout-based detection:** In this approach, a node waits for a response from a neighbor for a certain time interval. If no response is received within that interval, the node assumes that the neighbor has failed.

### 5. Recovery Strategies

Once a failure has been detected, there are several strategies for recovering from the failure:

- **Reboot:** This involves restarting the failed component or node.

- **Failover:** This involves switching to a backup component or node.

- **Rollback:** This involves reverting to a previous state of the system.

- **Redundancy:** This involves using redundant components or nodes to continue providing the service.

Mnemonics and learning tricks:

- Remember the acronym "RRFCR" to remember the different recovery strategies: Reboot, Failover, Rollback, Redundancy.

- Remember the phrase "check the heart" to remember the heartbeat-based failure detection approach.

- Remember the phrase "wait for timeout" to remember the timeout-based failure detection approach.