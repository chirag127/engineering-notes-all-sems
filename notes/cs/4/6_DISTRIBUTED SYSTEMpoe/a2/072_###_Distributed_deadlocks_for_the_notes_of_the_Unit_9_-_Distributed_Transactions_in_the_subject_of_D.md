 Here is the content in markdown format:

### Distributed deadlocks for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Distributed deadlocks can occur in distributed systems when multiple processes are waiting for each other to release locks on resources. Since the locks and processes are distributed across multiple nodes, it is more difficult to detect and resolve distributed deadlocks.

Some key points about distributed deadlocks:

- Resources can be databases, memory, CPUs, etc. residing on different nodes.
- Processes requesting and holding locks on resources can be on different nodes.
- Wait-for graphs are more complex involving multiple nodes and processes.
- Centralized deadlock detection algorithms do not work due to decentralization.
- Distributed deadlock detection algorithms involve coordination between nodes to detect global deadlocks.

**Mnemonics:** Think of distributed deadlocks as a 'Mexican standoff' between multiple processes on different nodes, all waiting for each other to release locks. None can proceed without the other letting go of its lock.

**Advantages:** Allowing parallelism and decentralization in distributed systems.
**Disadvantages:** Difficulty in detecting and resolving distributed deadlocks leading to system halting states.

_Detailed examples and diagrams can be included if required. Let me know if you would like me to add or modify anything in the content._