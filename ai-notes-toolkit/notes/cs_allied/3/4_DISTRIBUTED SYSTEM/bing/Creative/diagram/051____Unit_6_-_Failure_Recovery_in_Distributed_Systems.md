## Unit 6 - Failure Recovery in Distributed Systems

- In a distributed system, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state, such as using checkpoints, logging, or rollback.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state, such as using redundancy, replication, or fault tolerance.
- The choice of recovery technique depends on the type and frequency of failures, the system requirements, and the cost and complexity of implementation.
- Some of the challenges and trade-offs of failure recovery in distributed systems are:
  - How to detect and identify failures in a timely and accurate manner.
  - How to coordinate and synchronize the recovery actions among multiple components or nodes.
  - How to ensure the consistency and correctness of the system state after recovery.
  - How to minimize the overhead and performance impact of recovery mechanisms.
  - How to balance the trade-off between availability and consistency in the presence of failures.