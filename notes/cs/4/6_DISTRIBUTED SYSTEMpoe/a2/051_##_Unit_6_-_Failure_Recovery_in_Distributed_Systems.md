 Here is the content in markdown format for the topic ## Unit 6 - Failure Recovery in Distributed Systems:

## Unit 6 - Failure Recovery in Distributed Systems

Failure recovery in distributed systems refers to the techniques and methods to handle failures, faults, and errors in a distributed system and bring the system back to a consistent and operational state.

Some key points about failure recovery in distributed systems:

1. Failures are inevitable: Distributed systems have multiple components spread across networks, hardware, and software. This increases the likelihood of failures occurring. Hence, failure recovery mechanisms are essential to handle failures.
2. Types of failures: Failures can be permanent (complete failure) or transient (temporary fault). Recovery mechanisms need to handle both kinds of failures. Common types of failures include node failures, network partitions, software bugs, etc.
3. Consistency and availability: Failure recovery techniques try to achieve a balance between consistency (correctness) and availability (operational). Techniques that focus more on consistency may reduce availability and vice versa. Trade-offs are made based on system requirements.
4. Redundancy: Redundancy or replication of critical data/components is a common technique to enable recovery. When a failure occurs, the redundant copy can be used. However, this uses more resources.
5. Checkpointing: The state of the system is periodically saved (checkpointed). In case of a failure, the system can recover to the latest checkpoint. However, checkpointing at very high frequencies can degrade performance.
6. Consensus: In distributed systems, consensus algorithms are used to ensure all nodes agree on certain information. These algorithms can also be leveraged for failure recovery to elect new leaders or activate redundant nodes.

Some examples of failure recovery techniques are:

- Replication (primary-backup, multiple backups)
- Checkpointing
- Log replay
- Leader election
- Quorum consensus
- State machine replication

Advantages of failure recovery in distributed systems:

- Increased availability and reliability
- Tolerates component failures
- Prevents system from becoming non-operational due to failures

Disadvantages:

- Increased complexity
- Additional overhead can impact performance
- Trade-offs between consistency and availability

Applications: Failure recovery techniques are commonly used in distributed databases, distributed file systems, distributed transaction processing systems, cloud computing, etc. to increase resilience to failures.