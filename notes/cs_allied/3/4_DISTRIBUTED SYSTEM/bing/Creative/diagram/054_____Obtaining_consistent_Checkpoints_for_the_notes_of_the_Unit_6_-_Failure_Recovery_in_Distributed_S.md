Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for the unit 6 - Failure Recovery in Distributed Systems.

### Obtaining consistent Checkpoints

- A checkpoint is a snapshot of the state of a process or a system at a given point in time.
- Checkpoints are useful for failure recovery in distributed systems, as they allow the system to resume from a consistent state after a failure, without losing or repeating any work.
- A consistent checkpoint is a set of checkpoints from different processes or components of the system that are taken at the same logical time, or that reflect a consistent global state of the system.
- Obtaining consistent checkpoints in distributed systems is challenging, as there may be concurrent and asynchronous events, such as message exchanges, process executions, and failures, that can affect the state of the system.
- There are different approaches for obtaining consistent checkpoints in distributed systems, such as:

  - Coordinated checkpointing: In this approach, all the processes or components of the system coordinate with each other to take checkpoints at the same time, or to agree on a global checkpointing algorithm. This ensures that the checkpoints are consistent, but it may incur high overhead and synchronization costs, and it may not be feasible in large or dynamic systems.
  - Uncoordinated checkpointing: In this approach, each process or component of the system takes checkpoints independently, without any coordination or communication with others. This reduces the overhead and synchronization costs, but it may result in inconsistent checkpoints, or the need for additional mechanisms, such as message logging or dependency tracking, to ensure consistency.
  - Communication-induced checkpointing: In this approach, each process or component of the system takes checkpoints based on the messages it receives or sends, according to some rules or protocols. This allows the checkpoints to be consistent, without requiring global coordination or synchronization, but it may depend on the communication patterns and the checkpointing rules of the system.