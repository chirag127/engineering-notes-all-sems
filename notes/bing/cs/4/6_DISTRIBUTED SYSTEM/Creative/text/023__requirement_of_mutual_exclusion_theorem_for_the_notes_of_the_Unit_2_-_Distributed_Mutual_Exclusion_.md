### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a program object that refers to the requirement of satisfying that no two concurrent processes are in a critical section at any given time.
- A critical section is a segment of code that accesses a shared resource or data that needs to be executed in a mutually exclusive manner.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time.
- A distributed system is a collection of independent and geographically dispersed processes that communicate by message passing and do not share memory or a common physical clock .
- To achieve mutual exclusion in a distributed system, a process must request permission from other processes before entering the critical section.
- A mutual exclusion algorithm for a distributed system must satisfy the following requirements:
  - **Safety**: No two processes can execute the critical section simultaneously.
  - **Liveness**: Every process that requests to enter the critical section eventually gets the permission.
  - **Fairness**: No process is indefinitely postponed or starved while waiting for the permission.
- Additionally, a mutual exclusion algorithm for a distributed system should also consider the following performance metrics:
  - **Message complexity**: The number of messages exchanged per critical section entry.
  - **Synchronization delay**: The time elapsed between the last request message and the first permission message.
  - **Response time**: The time elapsed between a process requesting and entering the critical section.
  - **System throughput**: The number of times the critical section is executed per unit time.