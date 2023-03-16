### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- One of the common mechanisms for failure recovery is checkpoint-based, which involves periodically saving the state of the system or its components to a stable storage .
- Checkpoints are snapshots of the system state that can be used to resume the computation from a known point in case of a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple components that may be executing concurrently and communicating with each other.
- A consistent checkpoint is one that reflects a global state of the system that could have occurred during the normal execution of the system.
- A consistent checkpoint should satisfy the following properties:
  - No orphan message: A message is orphan if it is received by a process after its checkpoint, but sent by a process before its checkpoint.
  - No domino effect: The domino effect occurs when a failure forces the system to roll back to an earlier checkpoint, which in turn causes another failure that requires another rollback, and so on.
- There are two main approaches for obtaining consistent checkpoints in distributed systems:
  - Coordinated checkpointing: In this approach, all the processes in the system coordinate with each other to take a global checkpoint at the same time. This ensures that no orphan messages or domino effects occur, but it requires a lot of synchronization and communication overhead.
  - Uncoordinated checkpointing: In this approach, each process in the system takes its own checkpoint independently, without any coordination with other processes. This reduces the overhead of synchronization and communication, but it may result in inconsistent checkpoints that contain orphan messages or domino effects. To resolve these inconsistencies, some additional techniques are needed, such as message logging or dependency tracking.