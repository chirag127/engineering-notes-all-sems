### Obtaining consistent Checkpoints

- Checkpoints are snapshots of the state of a process or a system at a given point in time.
- Checkpoints are useful for failure recovery in distributed systems, as they allow processes to roll back to a previous consistent state and resume execution.
- A consistent checkpoint is one that preserves the causal order of events in the system, i.e., if a process P sends a message m to another process Q, then P's checkpoint must be taken before Q's checkpoint.
- There are two main approaches for obtaining consistent checkpoints in distributed systems: coordinated checkpointing and communication-induced checkpointing.

#### Coordinated checkpointing

- In coordinated checkpointing, all processes in the system agree on when to take a checkpoint, either by using a central coordinator or by exchanging messages among themselves.
- Coordinated checkpointing ensures that no process takes a checkpoint while it has a message in transit, thus avoiding the creation of orphan messages (messages that are received after the checkpoint but were sent before the checkpoint).
- Coordinated checkpointing has the advantages of simplicity, low overhead, and minimal storage requirements, as each process only needs to keep one checkpoint at a time.
- Coordinated checkpointing has the disadvantages of blocking the normal execution of the system during the checkpointing process, and requiring global synchronization among all processes.

#### Communication-induced checkpointing

- In communication-induced checkpointing, processes take checkpoints based on the messages they send and receive, without any global coordination.
- Communication-induced checkpointing ensures that the checkpoints form a consistent global state by using a protocol that enforces some rules on when and how to take checkpoints.
- Communication-induced checkpointing has the advantages of avoiding blocking and synchronization, and allowing more flexibility and concurrency in the system.
- Communication-induced checkpointing has the disadvantages of complexity, high overhead, and large storage requirements, as each process may need to keep multiple checkpoints and dependencies among them.