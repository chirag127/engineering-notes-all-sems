### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A checkpoint is a snapshot of the state of a process or a system at a given point in time.
- Checkpoints are useful for failure recovery in distributed systems, as they allow processes to roll back to a previous state and resume execution after a failure.
- However, checkpoints must be consistent, meaning that they reflect a global state of the system that is reachable by normal execution.
- Inconsistent checkpoints may lead to incorrect or incomplete recovery, as they may contain contradictory or missing information about the system state.
- There are two main approaches for obtaining consistent checkpoints in distributed systems: coordinated and uncoordinated.
- Coordinated checkpointing requires all processes to agree on when to take a checkpoint, and to synchronize their checkpointing activities. This ensures that the checkpoints are consistent, but it also introduces overhead and delays in the system.
- Uncoordinated checkpointing allows each process to take a checkpoint independently, without any coordination with other processes. This reduces the overhead and delays, but it may result in inconsistent checkpoints. To deal with this, processes need to use additional mechanisms, such as message logging or dependency tracking, to ensure that the checkpoints can be used for correct recovery.