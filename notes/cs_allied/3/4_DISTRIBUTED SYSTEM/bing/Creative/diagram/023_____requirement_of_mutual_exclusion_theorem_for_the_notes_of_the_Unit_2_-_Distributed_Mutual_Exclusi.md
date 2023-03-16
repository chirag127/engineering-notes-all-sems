### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a section of code that accesses a shared resource or data that must not be accessed by more than one process at a time.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties :
  - Safety: No two processes can be in the critical section at the same time.
  - Liveness: Every request to enter the critical section is eventually granted.
  - Fairness: No process is indefinitely postponed or starved while waiting to enter the critical section.
  - Fault-tolerance: The algorithm can tolerate a bounded number of process or message failures without violating the safety property.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in a logical ring. A process can enter the critical section only if it possesses the token.
  - Permission-based algorithms: A process requests permission from a set of processes before entering the critical section. A process can enter the critical section only if it receives permission from all the processes in the set.
  - Quorum-based algorithms: A process requests permission from a subset of processes (called a quorum) before entering the critical section. A process can enter the critical section only if it receives permission from a majority of the processes in the quorum.