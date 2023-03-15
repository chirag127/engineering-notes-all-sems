 Here is the content in markdown format:

### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Checkpointing is a technique to periodically save the state of a distributed system so that it can be recovered to a previous correct state in case of a failure.
- Consistent checkpointing is challenging in distributed systems as the state is distributed across multiple processes/machines.
- For consistent checkpointing, all processes must checkpoint at the same global state. This requires coordination among processes to ensure checkpointing happens at the same point in the execution.
- Two general approaches for consistent checkpointing:
	- Coordinated checkpointing: Processes checkpoint together at coordinated points. Requires synchronization but produces minimal rollback and less overhead.
	- Uncoordinated checkpointing: Processes checkpoint independently but rollback to a common checkpoint in case of failure. No synchronization but may require rollback of more processes and higher overhead.
- Chandy-Lamport algorithm is a classic coordinated checkpointing algorithm. It uses messages to coordinate checkpointing and ensures a global consistent state is captured.
- Advantages of consistent checkpointing:
	- Failure recovery to a consistent state
	- Limited rollback needed
- Disadvantages:
	- Complex to implement
	- Non-trivial overhead due to coordination
	- Does not scale well for large distributed systems

[Diagrams and examples can be added here if helpful for learning]

The content summarizes the key points around obtaining consistent checkpoints in distributed systems. Let me know if you would like me to elaborate on any of the points or add more details.