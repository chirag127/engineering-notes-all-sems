### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.

There are three basic approaches for implementing distributed mutual exclusion algorithms:

- **Token-based approach**: A unique token is shared among the sites or processes. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- **Non-token-based approach**: There is no token in this approach. Instead, a site requests permission from other sites before entering its critical section. The other sites grant or deny the permission based on some rules or conditions. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm and Singhal's algorithm.
- **Quorum-based approach**: A site needs to obtain permission from a subset of sites, called a quorum, before entering its critical section. A quorum is a set of sites that satisfies some properties, such as intersection, majority or availability. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.

Each approach has its own advantages and disadvantages in terms of message complexity, synchronization delay, fault tolerance and scalability.