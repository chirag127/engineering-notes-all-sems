### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a segment of code that accesses a shared resource or data.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion.
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of the other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of the processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting to enter the critical section and being granted permission to do so.
  - System throughput: The number of times the critical section is executed per unit time in the system.