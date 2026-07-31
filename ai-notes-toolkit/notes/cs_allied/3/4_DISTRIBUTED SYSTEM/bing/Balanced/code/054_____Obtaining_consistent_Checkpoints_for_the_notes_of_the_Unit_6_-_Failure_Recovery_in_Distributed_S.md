### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure can be defined as a deviation of the system from its expected behavior or specification.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple processes that may communicate and synchronize with each other.
- A checkpoint is consistent if it reflects a global state that could have occurred during a correct execution of the system.
- There are different techniques for obtaining consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing.
- Coordinated checkpointing requires all processes to agree on when to take a checkpoint, and to coordinate their communication activities during the checkpointing process.
- Uncoordinated checkpointing allows each process to take a checkpoint independently, without any coordination with other processes.
- Communication-induced checkpointing uses the communication messages between processes to trigger checkpoints, and to ensure that the checkpoints are consistent.
- Each technique has its own advantages and disadvantages, such as performance overhead, storage space, recovery time, etc.
- The choice of the checkpointing technique depends on the characteristics of the system, such as the failure rate, the communication pattern, the checkpoint frequency, etc.