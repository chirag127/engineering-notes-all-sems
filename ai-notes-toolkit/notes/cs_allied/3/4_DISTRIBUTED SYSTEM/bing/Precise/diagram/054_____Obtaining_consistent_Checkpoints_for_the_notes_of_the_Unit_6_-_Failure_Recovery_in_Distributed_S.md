### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Checkpointing is a technique used in distributed systems to ensure that the system can recover from failures.
2. A checkpoint is a snapshot of the state of the system at a particular point in time.
3. To obtain consistent checkpoints, all processes in the system must agree on a global state and take a snapshot of their local state at the same time.
4. This can be achieved through the use of a coordination protocol, such as the Chandy-Lamport algorithm.
5. The Chandy-Lamport algorithm involves sending marker messages between processes to indicate the start of a checkpointing round.
6. Once all processes have received a marker message, they take a snapshot of their local state and send an acknowledgement to the coordinator.
7. The coordinator collects all acknowledgements and determines if a consistent global state has been reached.
8. If a consistent global state has been reached, the checkpoint is considered successful and can be used for recovery in the event of a failure.
9. If a consistent global state has not been reached, the checkpointing round is considered unsuccessful and must be repeated.