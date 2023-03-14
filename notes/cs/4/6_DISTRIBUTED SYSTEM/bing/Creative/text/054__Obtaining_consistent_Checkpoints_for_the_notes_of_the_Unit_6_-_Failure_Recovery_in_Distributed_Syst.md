### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Checkpointing is a technique that allows processes to make progress in spite of failures by saving their state on stable storage from time to time .
- When a failure occurs, the process rolls back to its most recent checkpoint, assumes the state saved in that checkpoint, and resumes execution.
- In a distributed system, checkpointing involves taking a distributed snapshot, often known as a consistent global state, of the system.
- A consistent global state is one that reflects a possible execution of the system, i.e., it does not contain any causal inconsistency .
- A causal inconsistency occurs when a checkpoint of a process reflects the occurrence of an event, but the checkpoint of another process does not reflect the receipt of the message corresponding to that event .
- There are two main approaches for creating checkpoints in a distributed system:
  - Independent checkpointing: every process takes checkpoints independently and the currently committed results are stored in permanent storage. When one or more of the processes fail, they need to communicate with other processes in the system to find a consistent set of checkpoints among the saved ones. All the affected processes are rolled back to this set of checkpoints and then restarted.
  - Coordinated checkpointing: processes coordinate with each other to take checkpoints in such a way that the resulting global state is consistent. This avoids the need for communication and rollback after a failure, but requires synchronization and blocking during checkpointing .
- There are various algorithms for obtaining consistent checkpoints in a distributed system, such as the Chandy-Lamport algorithm, the Koo-Toueg algorithm, and the Manivannan-Singhal algorithm.
- The main challenges and trade-offs in designing checkpointing algorithms are :
  - Minimizing the overhead of checkpointing, such as the number of checkpoints, the size of checkpoints, the frequency of checkpoints, and the blocking time of processes.
  - Minimizing the rollback distance, i.e., the amount of computation that needs to be redone after a failure.
  - Avoiding the domino effect, i.e., the situation where a process rolls back to a checkpoint that causes another process to roll back to an earlier checkpoint, and so on, until the entire system reaches the initial state.
  - Avoiding livelock, i.e., the situation where processes keep taking checkpoints and rolling back without making any progress.
  - Tolerating failures that occur during checkpointing or recovery.