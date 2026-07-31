### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to recover from failures in a distributed system by restoring the system to a previous consistent state. This is done by undoing the effects of any actions that were performed after the last consistent state was saved.

- **Forward recovery** is a technique used to recover from failures in a distributed system by continuing to execute the system from the point of failure, using redundant or additional information to correct the effects of the failure.

- Both backward and forward recovery techniques are used to ensure the consistency and reliability of distributed systems in the event of failures.

- Backward recovery techniques include checkpointing, logging, and rollback. Checkpointing involves periodically saving the state of the system to stable storage, so that the system can be restored to a previous consistent state in the event of a failure. Logging involves recording the actions performed by the system, so that they can be undone if necessary. Rollback involves undoing the effects of any actions that were performed after the last consistent state was saved.

- Forward recovery techniques include error correction, replication, and redundancy. Error correction involves using additional information to correct the effects of a failure. Replication involves maintaining multiple copies of data or processes, so that if one copy fails, another copy can take over. Redundancy involves adding extra components or resources to the system, so that if one component fails, another component can take over.

- The choice of recovery technique depends on the specific requirements of the distributed system, including the level of reliability and consistency required, the nature of the failures that may occur, and the resources available for recovery.