
### Atomic Commit in Distributed Database System

Atomic Commit is an agreement protocol used in distributed database systems. It ensures that all operations in a distributed transaction are either completed or rolled back in the event of a failure.

- Atomic Commit ensures that all operations in a distributed transaction are executed in an all-or-nothing manner. 
- It helps maintain the integrity of the data in the distributed database system by ensuring that either all operations are successful or none are. 
- Atomic Commit is also known as a two-phase commit protocol. It uses two distinct phases to ensure that all operations in a distributed transaction are successful. 
- The first phase is the "prepare" phase. In this phase, the coordinator node sends a "prepare" message to all nodes participating in the distributed transaction. 
- All nodes must respond with an acknowledgement that they are ready to commit the transaction. 
- If all nodes respond with an acknowledgement, the coordinator node sends a "commit" message to all nodes. 
- The second phase is the "commit" phase. In this phase, all nodes must commit the transaction or else the transaction will be rolled back. 
- Atomic Commit ensures that all operations in a distributed transaction are completed successfully or else the transaction is rolled back. 
- This ensures that the integrity of the data in the distributed database system is maintained.