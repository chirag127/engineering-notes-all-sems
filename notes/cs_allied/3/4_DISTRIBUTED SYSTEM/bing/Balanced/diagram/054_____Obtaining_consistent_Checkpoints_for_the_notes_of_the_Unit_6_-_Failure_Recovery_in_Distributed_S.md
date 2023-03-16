### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure can be a crash, a communication loss, a data corruption, or a malicious attack.
- A consistent state is one that satisfies the system's correctness properties, such as atomicity, consistency, isolation, and durability.
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because different components may have different views of the global state, and concurrent events may cause inconsistencies.
- There are different techniques for obtaining consistent checkpoints, such as:
  - Coordinated checkpointing: All components coordinate to take a checkpoint at the same time, or use a global clock to synchronize their checkpoints. This ensures a consistent global state, but may incur high overhead and blocking.
  - Uncoordinated checkpointing: Each component takes a checkpoint independently, without any coordination with others. This reduces the overhead and blocking, but may result in inconsistent global state and orphan processes.
  - Communication-induced checkpointing: Each component takes a checkpoint based on the messages it receives from others, and piggybacks checkpoint information on the messages it sends. This avoids blocking and reduces the number of checkpoints, but may require complex algorithms to ensure consistency.
- The choice of checkpointing technique depends on the characteristics of the system, such as the frequency and type of failures, the communication pattern, the performance requirements, and the availability of global clock.