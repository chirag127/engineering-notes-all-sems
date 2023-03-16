### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- **Non-token-based approach**: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by the voting mechanism. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm and Singhal's algorithm.
- **Quorum-based approach**: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.