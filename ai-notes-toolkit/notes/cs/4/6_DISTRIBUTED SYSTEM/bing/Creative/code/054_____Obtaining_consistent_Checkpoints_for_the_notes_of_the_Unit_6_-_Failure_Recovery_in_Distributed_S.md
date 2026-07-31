### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of the system.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- A checkpoint is a snapshot of the system state at a certain point in time.
- Checkpoints can be used to recover from failures by rolling back the system to a previous checkpoint and resuming the execution from there.
- However, checkpoints must be consistent, meaning that they reflect a global state of the system that could have occurred during the normal execution.
- Inconsistent checkpoints may lead to incorrect or incomplete recovery, such as losing some messages, violating causality, or repeating some operations.
- Obtaining consistent checkpoints in distributed systems is challenging because of the lack of a global clock, the concurrency of processes, and the possibility of partial failures.
- There are different techniques for obtaining consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing.
- Coordinated checkpointing requires all processes to agree on when to take a checkpoint, and to coordinate their message sending and receiving during the checkpointing.
- Uncoordinated checkpointing allows each process to take a checkpoint independently, without any synchronization with other processes.
- Communication-induced checkpointing uses piggybacking or control messages to force some processes to take checkpoints based on the causal dependencies among messages.
- Each technique has its own advantages and disadvantages, such as overhead, latency, storage, and recovery time.
- A trade-off must be made between the frequency and the cost of checkpointing, depending on the system requirements and the failure characteristics.

: Failure Recovery in Distributed Systems - 1000 Projects
: Various Failures in Distributed Systems - tutorialspoint.com
: Recovery in Distributed Systems - GeeksforGeeks