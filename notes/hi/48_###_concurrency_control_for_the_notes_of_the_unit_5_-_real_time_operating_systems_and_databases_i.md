### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System
Concurrency Control in Real-Time Systems and Databases:
- It is a technique to manage multiple transactions accessing a shared database simultaneously.
- Ensures consistency and integrity of data by preventing conflicting transactions from executing simultaneously.
- Two main approaches: Locking and Timestamping.
- Locking: resources are locked for exclusive access by a transaction. Deadlocks can occur if two transactions hold locks on each other's resources.
- Timestamping: assigns a unique timestamp to each transaction to order their execution. Conflicts are resolved by aborting the transaction with the lower timestamp.
- Both approaches have trade-offs in terms of performance and complexity.
- Real-time databases may use specialized concurrency control algorithms to meet timing constraints.
