### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Checkpointing** is a technique used in distributed systems to recover from failures.
2. It involves periodically saving the state of the system to stable storage, so that in the event of a failure, the system can be restored to a consistent state.
3. A **consistent checkpoint** is one where all processes in the system have saved their state in such a way that the system can be restored to a consistent state.
4. To obtain consistent checkpoints, all processes must coordinate to ensure that their individual checkpoints are taken at the same point in the distributed computation.
5. One approach to achieving this is the **Chandy-Lamport algorithm**, which uses a control message called a marker to coordinate the taking of checkpoints.
6. Another approach is the **synchronous checkpointing** method, where all processes take their checkpoints at the same time, typically using a global clock to synchronize their actions.
7. It is important to note that the goal of checkpointing is not to prevent failures, but to minimize the amount of work lost due to a failure and to speed up the recovery process.