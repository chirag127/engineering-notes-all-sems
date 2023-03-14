 Here is the content in markdown format for Unit 6 - Failure Recovery in Distributed Systems:

## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery in distributed systems involves handling faults and crashes to ensure continued availability and correctness of the system. Some key techniques for failure recovery are:

- Checkpointing: Periodically saving the state of the system so that in the event of a failure, the system can be rolled back to the last checkpoint and resumed from there. This minimizes lost work.
- Replication: Maintaining multiple copies of components/data and switching to a replica in the event of a failure. The replicas must be kept consistent.
- Fault-tolerant consensus: Enabling nodes in a distributed system to agree on a value despite failures. Paxos and Raft are popular consensus algorithms.
- Message logging: Persisting messages before delivery so that in the event of a failure, messages can be redelivered to ensure at-least-once delivery.
- Retry and timeout: Retrying operations that fail or time out and have a chance of succeeding if retried. Timeouts bound the retries to avoid infinite waits.

Advantages of failure recovery techniques:
- Increased availability: The system can continue operating even in the face of failures.
- Loss minimization: Lost work is minimized through techniques like checkpointing.

Disadvantages:
- Additional complexity: Failure recovery logic adds complexity to the system.
- Performance overhead: Techniques like checkpointing and replication have runtime overheads.
- Stronger consistency guarantees are harder to achieve.

Examples of applications: Databases, distributed databases, server clusters, distributed caches, consensus systems, etc.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.