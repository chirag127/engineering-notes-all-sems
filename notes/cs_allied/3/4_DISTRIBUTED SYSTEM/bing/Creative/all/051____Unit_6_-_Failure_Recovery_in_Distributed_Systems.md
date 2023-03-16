## Unit 6 - Failure Recovery in Distributed Systems

- A distributed system is a collection of independent computers that communicate and cooperate to achieve a common goal.
- A failure in a distributed system is an event that prevents one or more components from functioning correctly or at all.
- Failure recovery is the process of restoring the system to a consistent and correct state after a failure.
- Failure recovery is important for ensuring the availability, reliability, and performance of distributed systems.
- Failure recovery can be classified into two types: backward recovery and forward recovery.

### Backward Recovery
- Backward recovery is the process of restoring the system to a previous consistent and correct state before the failure occurred.
- Backward recovery can be implemented using techniques such as checkpoints, logging, and rollback.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage.
- Logging is the process of recording the actions or events that occur in the system on stable storage.
- Rollback is the process of restoring the system state to a previous checkpoint and replaying the logged actions or events until the failure point is reached.
- Backward recovery can be performed at different granularities, such as process-level, transaction-level, or system-level.
- Backward recovery can also be performed in different modes, such as pessimistic, optimistic, or causal.
- Pessimistic mode ensures that the system is always in a consistent state by using synchronous checkpoints and logging, but it incurs high overhead and latency.
- Optimistic mode allows the system to continue execution without waiting for checkpoints and logging, but it may require more rollback and replay in case of a failure.
- Causal mode ensures that the system is in a consistent state that respects the causal dependencies among the actions or events, by using asynchronous checkpoints and logging, but it may require some coordination and synchronization among the components.

### Forward Recovery
- Forward recovery is the process of restoring the system to a new consistent and correct state after the failure occurred.
- Forward recovery can be implemented using techniques such as redundancy, replication, and reconfiguration.
- Redundancy is the provision of extra resources or components that can take over the functionality of the failed ones.
- Replication is the process of creating and maintaining multiple copies of the same data or service on different components.
- Reconfiguration is the process of changing the structure or configuration of the system to adapt to the failure.
- Forward recovery can be performed at different levels, such as hardware-level, software-level, or application-level.
- Forward recovery can also be performed in different modes, such as passive, active, or hybrid.
- Passive mode relies on a primary component that performs the functionality and a backup component that takes over in case of a failure, but it may incur high recovery time and data loss.
- Active mode relies on multiple components that perform the functionality in parallel and coordinate with each other, but it may incur high resource consumption and complexity.
- Hybrid mode combines the advantages of passive and active modes by using a primary component and multiple backup components that perform the functionality in parallel, but it may incur high communication overhead and inconsistency.