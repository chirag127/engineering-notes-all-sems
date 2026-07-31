### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to recover from failures in distributed systems by restoring the system to a previous consistent state. This is done by undoing the effects of any actions that were taken after the last known consistent state.

- **Forward recovery** is a technique used to recover from failures in distributed systems by continuing to execute the system from the point of failure, using additional information to correct the effects of the failure.

- Both backward and forward recovery techniques are used to ensure the consistency and reliability of distributed systems.

- In backward recovery, the system maintains a log of all actions taken, and uses this log to undo any actions that were taken after the last known consistent state. This is known as **rollback**.

- In forward recovery, the system uses additional information, such as redundant data or error-correcting codes, to correct the effects of the failure and continue execution from the point of failure. This is known as **rollforward**.

- The choice between backward and forward recovery depends on the specific requirements of the distributed system, such as the cost of maintaining a log, the availability of additional information, and the time required to perform recovery.

- Both backward and forward recovery techniques can be used in combination to provide a robust and reliable failure recovery mechanism for distributed systems.