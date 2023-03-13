## Unit 6 - Failure Recovery in Distributed Systems

- A distributed system is a collection of independent nodes that communicate and coordinate to achieve a common goal.
- A failure in a distributed system is an event that prevents a node or a communication link from functioning correctly.
- Failure recovery is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is important for maintaining the availability, reliability, and performance of the system.
- Failure recovery can be classified into two types: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of the failure and restoring the system to a previous consistent state. This can be done by using techniques such as checkpoints, logging, rollback, and compensation.
- Forward recovery involves correcting the cause of the failure and continuing the execution from the current state. This can be done by using techniques such as replication, redundancy, fault tolerance, and self-healing.
- The choice of recovery technique depends on the characteristics of the system, such as the failure model, the consistency model, the communication model, and the performance requirements.