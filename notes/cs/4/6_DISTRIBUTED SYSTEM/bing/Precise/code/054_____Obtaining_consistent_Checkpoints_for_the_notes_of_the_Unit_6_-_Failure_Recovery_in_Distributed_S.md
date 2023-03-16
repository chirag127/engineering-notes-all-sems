### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Checkpointing** is a process of routinely saving the state of the system onto stable storage in a fault-tolerant distributed system.
2. There are two main approaches for creating checkpoints in a distributed system.
3. In the first approach, every process takes checkpoints independently and the currently committed results are stored in permanent storage.
4. When one or more of the processes fail, they need to communicate with other processes in the system to find a consistent set of checkpoints among the saved ones.
5. All the affected processes are rolled back to this set of checkpoints and then restarted.
6. Rollback of one process may require that other processes also roll back to an earlier state.
