## Unit 2 - Distributed Mutual Exclusion

- Mutual exclusion is a property of concurrency control, which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously, and the outcome depends on the order of execution.
- Mutual exclusion ensures that only one process is allowed to execute the critical section (CS) at any given time, where the CS is the part of the code that accesses the shared resource or data  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion, because there is no global memory or clock .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token, which is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the other processes in the system, using request and reply messages.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a weighted majority of the processes in the system, using voting sets.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution .
  - Synchronization delay: The time elapsed between the instant a process requests the CS and the instant it is granted the CS, assuming no other process is in the CS .
  - Response time: The time elapsed between the instant a process requests the CS and the instant it is granted the CS, assuming some other process may be in the CS .
  - System throughput: The number of times the CS is executed per unit time in the system .
  - Fault tolerance: The ability of the algorithm to handle process or message failures .