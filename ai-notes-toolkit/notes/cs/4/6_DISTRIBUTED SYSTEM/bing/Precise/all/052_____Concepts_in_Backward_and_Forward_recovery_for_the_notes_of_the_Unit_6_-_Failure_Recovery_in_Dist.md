# Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to recover from failures in distributed systems by restoring the system to a previous consistent state.
- This is achieved by maintaining a log of all changes made to the system and using this log to undo any changes made after the point of failure.
- Backward recovery is also known as **rollback recovery**.
- **Forward recovery** is a technique used to recover from failures in distributed systems by attempting to continue processing despite the failure.
- This is achieved by using redundant components or by attempting to repair the failed component.
- Forward recovery is also known as **rollforward recovery**.
- Both backward and forward recovery techniques can be used in combination to provide a more robust recovery mechanism.
- The choice of recovery technique depends on the nature of the failure and the requirements of the system. For example, backward recovery may be more appropriate for transient failures, while forward recovery may be more appropriate for permanent failures.