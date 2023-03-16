### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to recover from failures in distributed systems by restoring the system to a previous consistent state.
- This is achieved by maintaining a log of all changes made to the system and using this log to undo any changes made after the point of failure.
- Backward recovery is also known as **rollback recovery**.
- **Forward recovery** is a technique used to recover from failures in distributed systems by attempting to correct the error and continue processing from the point of failure.
- This is achieved by using redundant data or algorithms to correct the error and continue processing.
- Forward recovery is also known as **rollforward recovery**.
- Both backward and forward recovery techniques are used to ensure the **consistency** and **availability** of distributed systems in the event of failures.
- The choice of recovery technique depends on the specific requirements of the system and the nature of the failure.
