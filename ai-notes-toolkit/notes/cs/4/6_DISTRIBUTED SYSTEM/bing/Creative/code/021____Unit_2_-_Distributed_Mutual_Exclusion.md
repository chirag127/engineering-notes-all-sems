# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time  .
- Distributed mutual exclusion is necessary to prevent race conditions, which are situations where the outcome of a computation depends on the order or timing of concurrent processes.
- Distributed mutual exclusion cannot be implemented using shared variables or local kernels, as they are not available or reliable in a distributed system. Message passing is the only means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token that is circulated among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of the processes in the system.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a weighted majority of the processes in the system.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting and entering the critical section.
  - System throughput: The number of times the critical section is executed per unit time.
  - Fault tolerance: The ability of the algorithm to handle process or link failures.