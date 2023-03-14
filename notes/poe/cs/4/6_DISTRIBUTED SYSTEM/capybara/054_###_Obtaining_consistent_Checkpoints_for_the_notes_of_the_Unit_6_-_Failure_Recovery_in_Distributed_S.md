### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, it is important to have a mechanism to recover from failures. One way to achieve this is through checkpoints. Checkpoints are a way to save the state of the system at a particular point in time so that if a failure occurs, the system can be restored to a previous state. However, in order for checkpoints to be effective, they must be consistent. This means that all processes in the system must take the checkpoint at the same time, and the state saved must be consistent across all processes.

Here are some ways to obtain consistent checkpoints in a distributed system:

1. Synchronous Checkpointing: In synchronous checkpointing, all processes in the system must stop and take a checkpoint at the same time. This ensures that the state saved is consistent across all processes. However, synchronous checkpointing can be expensive as it requires all processes to stop at the same time.

2. Asynchronous Checkpointing: In asynchronous checkpointing, processes can take checkpoints at any time without coordination. However, this can lead to inconsistent checkpointing as different processes may save different states at different times. To mitigate this, processes can periodically exchange messages to ensure that they are all at the same state before taking a checkpoint.

3. Coordinated Checkpointing: Coordinated checkpointing is a compromise between synchronous and asynchronous checkpointing. In coordinated checkpointing, processes are divided into groups. Each group takes a checkpoint at the same time, and the state saved is consistent within the group. After all groups have taken a checkpoint, the checkpoints are compared to ensure that they are consistent across all processes.

4. Incremental Checkpointing: Incremental checkpointing is a way to reduce the overhead of taking checkpoints. Instead of saving the entire state of the system, only the changes since the last checkpoint are saved. This can be done by logging all events that change the system state and then replaying them during recovery.

Mnemonic: Remember the acronym S.A.C.I (Synchronous, Asynchronous, Coordinated, Incremental) to recall the different ways to obtain consistent checkpoints in a distributed system.

In conclusion, checkpoints are an important mechanism for recovering from failures in distributed systems. However, in order for checkpoints to be effective, they must be consistent. There are different ways to obtain consistent checkpoints, including synchronous, asynchronous, coordinated, and incremental checkpointing. Remembering the acronym S.A.C.I can help recall these different approaches during exams.