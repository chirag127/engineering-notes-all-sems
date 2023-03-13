
### Edge Chasing Algorithms for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of DISTRIBUTED SYSTEM

Edge Chasing algorithms are a type of distributed deadlock detection algorithms used in distributed systems. They are used to detect deadlocks in distributed systems by exchanging messages between processes.

The main idea behind Edge Chasing algorithms is that each process maintains a graph of its current state and a set of messages sent by other processes. The graph is updated whenever a message is received from another process. The algorithm then checks for cycles in the graph which indicate a deadlock.

The algorithm works in two phases:

1. **Exploration phase:** In this phase, each process sends a message to its neighbors and waits for a reply. If no reply is received within a certain time, the process assumes that the neighbor is deadlocked and sends a message to its other neighbors. This process is repeated until all processes have received a reply.

2. **Verification phase:** In this phase, each process checks the graph for cycles. If a cycle is found, the process is assumed to be deadlocked.

Advantages:

- Edge Chasing algorithms are relatively simple and easy to implement.
- They are fast and efficient in detecting deadlocks.
- They require minimal communication between processes.

Disadvantages:

- They require a lot of memory to store the graph.
- They cannot detect deadlocks that involve more than two processes.

Mnemonics and Learning Tricks:

- Remember that Edge Chasing algorithms are used to detect deadlocks in distributed systems.
- Think of the graph as a map of the current state of the system.
- The algorithm works in two phases: exploration and verification.