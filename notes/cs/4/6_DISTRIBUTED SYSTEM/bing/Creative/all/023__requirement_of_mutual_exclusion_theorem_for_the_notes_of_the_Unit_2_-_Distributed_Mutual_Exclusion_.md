### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property that prevents race conditions. It means that only one process can enter and execute its critical section (CS) at any given time, while other concurrent processes have to wait .
- Mutual exclusion in a distributed system is more challenging than in a single computer system, because there is no shared memory or common physical clock among the sites. Therefore, shared variables or local kernel cannot be used to implement mutual exclusion. Message passing is the only way to communicate and coordinate among the sites .
- A mutual exclusion algorithm for a distributed system must satisfy the following requirements:
  - No deadlock: No two or more sites should endlessly wait for any message that will never arrive.
  - No starvation: Every site that wants to execute CS should get an opportunity to do so in finite time. No site should wait indefinitely while other sites repeatedly execute CS.
  - Fairness: Each site should get a fair chance to execute CS. The requests for CS should be executed in the order they are made, or in the order of their arrival in the system.
  - Fault tolerance: The algorithm should be able to detect and recover from failures, and continue functioning without any disruption.
- There are three basic approaches for implementing mutual exclusion in a distributed system:
  - Token-based approach: A unique token is shared among all the sites. A site can enter CS only if it possesses the token, and it must release the token after exiting CS. This approach ensures mutual exclusion because the token is unique. Example: Suzuki-Kasami's broadcast algorithm.
  - Non-token-based approach: A site communicates with other sites to determine which site should execute CS next. This requires exchange of two or more rounds of messages among the sites. Example: Ricart-Agrawala's algorithm.
  - Quorum-based approach: A site obtains permission from a subset of sites (called a quorum) to enter CS. The quorum must be chosen such that any two quorums have at least one site in common. This ensures mutual exclusion because any site that enters CS must have the permission of a site that is also in the quorum of another site that wants to enter CS. Example: Maekawa's algorithm.

: Mutual exclusion in distributed system - GeeksforGeeks
: Distributed mutual exclusion algorithms (Chapter 9) - Distributed Computing