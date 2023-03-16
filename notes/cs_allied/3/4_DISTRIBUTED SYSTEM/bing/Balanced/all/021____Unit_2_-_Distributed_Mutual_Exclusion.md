## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is an interval of time where a process accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or based on some request messages.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the other processes in the system. The permission is granted or denied based on some logical clocks or timestamps.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a quorum of the processes in the system. The quorum can be dynamically or statically defined.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per CS execution.
  - Synchronization delay: The time elapsed between the instant a process requests the CS and the instant it is granted the CS.
  - System throughput: The number of times the CS is executed per unit time in the system.