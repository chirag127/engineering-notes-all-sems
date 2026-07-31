### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

Fault-tolerant services are essential in distributed systems to ensure that the system continues to function even when there is a failure in one or more of its components. Replication is a common technique used to achieve fault tolerance in distributed systems. In this unit, we will explore the various fault-tolerant services that can be used in distributed systems.

Here are some important points to keep in mind about fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM:

- Replication is a technique used to create redundant copies of data or services to ensure availability and fault tolerance. 
- There are two types of replication: passive and active. Passive replication involves replicating data to multiple nodes and selecting one of them as the primary node. Active replication involves executing the same operations on multiple nodes and comparing the results to ensure consistency. 
- The primary node is responsible for processing all incoming requests and forwarding them to the replicas. If the primary node fails, one of the replicas takes over as the primary node. 
- One of the challenges of replication is ensuring consistency among the replicas. To achieve this, several consistency models have been proposed, including eventual consistency, strong consistency, and causal consistency. 
- Eventual consistency allows replicas to diverge temporarily and then converge over time. Strong consistency ensures that all replicas have the same state at all times. Causal consistency ensures that events that are causally related are seen in the same order by all replicas. 
- Replication can also be used to improve performance by allowing requests to be processed in parallel on multiple nodes. 
- However, replication also introduces overhead and complexity, such as the need to manage multiple copies of data and ensure consistency among them. 
- To minimize the impact of failures on the system, replication can be combined with other fault-tolerant techniques, such as checkpointing and recovery. 
- Checkpointing involves periodically saving the system state to disk, so that it can be used to recover from a failure. Recovery involves restoring the system state to a previous checkpoint and replaying any operations that occurred after that checkpoint. 
- In summary, fault-tolerant services are essential in distributed systems to ensure availability and reliability. Replication is a common technique used to achieve fault tolerance, but it introduces overhead and complexity. To minimize the impact of failures on the system, replication can be combined with other fault-tolerant techniques, such as checkpointing and recovery.