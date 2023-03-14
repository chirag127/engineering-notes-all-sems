 Here is the content in markdown format:

### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Checkpoints are consistent global states of the distributed system that can be used to recover from failures.
- Obtaining consistent checkpoints is challenging in distributed systems due to concurrent execution of processes and messages in transit.
- Two phase commit protocol can be used to obtain consistent checkpoints:
    - In the first phase, each process takes local checkpoint and logs it locally.
    - In the second phase, each process either commits to the local checkpoint or aborts and rolls back to the previous checkpoint. This ensures all-or-nothing property and consistency.
- Chandy-Lamport snapshot algorithm can be used to obtain consistent distributed snapshots (checkpoints):
    - Each process tracks messages sent but not yet received (messages in transit).
    - Special marker messages are exchanged to track dependency between messages and processes.
    - When all marker messages have been received, a consistent global state (snapshot) has been reached. This state can be used as a checkpoint.

Advantages: Provides consistent recovery line and simplifies failure recovery.
Disadvantages: Can be expensive to obtain consistent checkpoints due to coordination overhead and blocking.
Applications: Used in databases, distributed systems, and distributed transactions to enable recovery and fault tolerance.

Mnemonics:
Two phase - all or nothing,
Chandy Lamport - messages in transit.

I hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.