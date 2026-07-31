### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.   

There are three basic approaches for implementing distributed mutual exclusion algorithms:  

- Token-based approach: A unique token is shared among the sites or processes. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.  
- Non-token-based approach: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by a voting mechanism. Examples of non-token-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm and Singhal's algorithm.  
- Quorum-based approach: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in the quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.  

The performance of distributed mutual exclusion algorithms can be evaluated based on the following metrics:   

- Message complexity: The number of messages exchanged per critical section execution.
- Synchronization delay: The time elapsed between a site's request and its entry to the critical section.
- System throughput: The number of critical section executions per unit time in the system.
- Fault tolerance: The ability of the algorithm to handle failures of sites or communication links.