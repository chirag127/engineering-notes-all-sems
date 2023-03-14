## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a problem of ensuring that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- The design of distributed mutual exclusion algorithms is complex because these algorithms have to deal with unpredictable message delays and incomplete knowledge of the system state.
- There are three basic approaches for implementing distributed mutual exclusion  :
  - Token-based approach: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token and it continues to hold the token until the execution of the critical section is over. Mutual exclusion is ensured because the token is unique. Example: Suzuki-Kasami’s Broadcast Algorithm.
  - Non-token-based approach: A site communicates with other sites in order to determine which site should execute the critical section next. This requires exchange of two or more successive rounds of messages among sites. Example: Ricart-Agrawala’s Algorithm.
  - Quorum-based approach: A site is allowed to enter its critical section if it obtains permission from a subset of sites (called a quorum) in the system. A quorum is a set of sites whose size and intersection properties ensure mutual exclusion. Example: Maekawa’s Algorithm.
- The requirements of distributed mutual exclusion algorithms are:
  - No deadlock: Two or more sites should not endlessly wait for any message that will never arrive.
  - No starvation: Every site who wants to execute the critical section should get an opportunity to execute it in finite time. Any site should not wait indefinitely to execute the critical section while other sites are repeatedly executing the critical section.
  - Fairness: Each site should get a fair chance to execute the critical section. Any request to execute the critical section must be executed in the order they are made, i.e., critical section execution requests should be executed in the order of their arrival in the system.
  - Fault tolerance: In case of failure, the algorithm should be able to recognize it by itself in order to continue functioning without any disruption.