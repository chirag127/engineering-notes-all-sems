### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, Raymond's tree-based algorithm, etc.
- **Non-token-based approach**: There is no token in this approach. Instead, a site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm with optimization, Maekawa's algorithm, etc.
- **Quorum-based approach**: This is a generalization of the non-token-based approach. A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Examples of quorum-based algorithms are Maekawa's algorithm, Sankararaman's algorithm, Agrawala-El Abbadi algorithm, etc.

The main criteria for evaluating the performance of distributed mutual exclusion algorithms are:

- **Message complexity**: The number of messages exchanged per critical section entry.
- **Synchronization delay**: The time elapsed between a site's request and its entry to the critical section.
- **Fault tolerance**: The ability of the algorithm to handle failures of sites or communication links.