# Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination, and synchronization in distributed systems.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the processes. A process can enter its critical section (CS) only if it possesses the token. Mutual exclusion is ensured because the token is unique. The token is passed from one process to another according to some algorithm. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, and Raymond's algorithm.
- **Non-token-based approach**: There is no token in this approach. Instead, a process requests permission from other processes to enter its CS. The other processes reply with their consent or denial. A process can enter its CS only if it receives consent from all or a majority of the other processes. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm, and Maekawa's algorithm.
- **Quorum-based approach**: This is a variation of the non-token-based approach. A process requests permission from a subset of processes, called a quorum, to enter its CS. A process can enter its CS only if it receives consent from all the processes in the quorum. The quorum is chosen such that any two quorums have at least one process in common. This ensures mutual exclusion. Examples of quorum-based algorithms are Maekawa's algorithm, Sankaranarayanan and Ricart's algorithm, and Agrawala and El Abbadi's algorithm.

The performance of distributed mutual exclusion algorithms can be evaluated based on the following metrics:

- **Message complexity**: The number of messages exchanged per CS execution.
- **Synchronization delay**: The time elapsed between a process requesting the CS and entering the CS.
- **System throughput**: The number of CS executions per unit time in the system.
- **Fault tolerance**: The ability of the algorithm to handle failures of processes or communication links.