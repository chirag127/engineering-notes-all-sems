### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Backward recovery** is a technique used to recover from failures in a distributed system by restoring the system to a previous consistent state.
2. This is achieved by maintaining a log of all changes made to the system and using this log to undo any changes made after the last consistent state.
3. **Forward recovery** is a technique used to recover from failures in a distributed system by attempting to correct the error and continue processing.
4. This is achieved by using redundant data or algorithms to correct the error and continue processing without the need to restore the system to a previous state.
5. Both backward and forward recovery techniques are used to ensure the reliability and availability of distributed systems in the event of failures.
6. The choice of recovery technique depends on the nature of the failure and the requirements of the system.
7. Backward recovery is typically used for transient failures, while forward recovery is used for permanent failures.
8. The use of recovery techniques is an important aspect of the design and implementation of distributed systems.
