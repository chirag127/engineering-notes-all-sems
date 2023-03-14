## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a problem of ensuring that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion  .
- The design of distributed mutual exclusion algorithms is complex because these algorithms have to deal with unpredictable message delays and incomplete knowledge of the system state.
- There are three basic approaches for implementing distributed mutual exclusion  :
  - Token-based approach: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token and it continues to hold the token until the execution of the critical section is over. Mutual exclusion is ensured because the token is unique. Example: Suzuki-Kasami’s Broadcast Algorithm.
  - Non-token-based approach: A site communicates with other sites in order to determine which site should execute the critical section next. This requires exchange of two or more successive rounds of messages among sites. Example: Ricart-Agrawala’s Algorithm.
  - Quorum-based approach: A site is allowed to enter its critical section if it obtains permission from a subset of sites (called a quorum) in the system. A quorum is a set of sites such that any two quorums have at least one site in common. Example: Maekawa’s Algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics :
  - Message complexity: The number of messages exchanged per critical section execution.
  - Synchronization delay: The delay between the time a site is ready to enter the critical section and the time it actually enters it.
  - Response time: The delay between the time a site requests to enter the critical section and the time it receives the permission to do so.
  - System throughput: The number of times the critical section is executed per unit time in the system.
- The requirements of distributed mutual exclusion algorithms are:
  - No deadlock: Two or more sites should not endlessly wait for any message that will never arrive.
  - No starvation: Every site who wants to execute the critical section should get an opportunity to execute it in finite time. Any site should not wait indefinitely to execute the critical section while other sites are repeatedly executing the critical section.
  - Fairness: Each site should get a fair chance to execute the critical section. Any request to execute the critical section must be executed in the order they are made, that is, critical section execution requests should be executed in the order of their arrival in the system.
  - Fault tolerance: In case of failure, the algorithm should be able to recognize it by itself in order to continue functioning without any disruption.

: Distributed mutual exclusion algorithms (Chapter 9) - Distributed Computing, https://www.cambridge.org/core/books/distributed-computing/distributed-mutual-exclusion-algorithms/F819BE611EE98FD80D4DF2A6237F79DA

: Mutual exclusion in distributed system - GeeksforGeeks, https://www.geeksforgeeks.org/mutual-exclusion-in-distributed-system/

: 3.1. DISTRIBUTED MUTUAL EXCLUSION ALGORITHMS: INTRODUCTION, https://www.jeppiaarinstitute.org/pdf/lectures/143.pdf