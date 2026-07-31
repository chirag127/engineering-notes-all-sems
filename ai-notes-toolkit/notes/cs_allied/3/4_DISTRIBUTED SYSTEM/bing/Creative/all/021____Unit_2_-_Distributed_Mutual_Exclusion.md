# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It prevents race conditions, which are situations where the outcome of a computation depends on the relative timing of events.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or based on some request-reply scheme.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The permission is granted or denied based on some logical or physical clock values or some priority scheme.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The quorum is defined based on some voting scheme or some graph-theoretic properties.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between the instant a process requests to enter the critical section and the instant it is allowed to do so, assuming that no other process is in the critical section.
  - Response time: The time elapsed between the instant a process requests to enter the critical section and the instant it actually enters the critical section, assuming that no other process is in the critical section.
  - System throughput: The number of times the critical section is executed per unit time in the system.