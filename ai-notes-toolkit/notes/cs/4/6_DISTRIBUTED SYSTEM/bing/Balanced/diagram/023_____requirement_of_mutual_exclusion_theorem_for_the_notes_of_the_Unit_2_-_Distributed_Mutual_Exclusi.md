### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time .
- A critical section is a segment of code that accesses a shared resource or data.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties:
  - Safety: At most one process can execute in the critical section at any time.
  - Liveness: If a process requests to enter the critical section, it will eventually be granted permission.
  - Fairness: No process is indefinitely postponed or starved from entering the critical section.
  - Fault-tolerance: The algorithm can tolerate a bounded number of process or message failures and still guarantee mutual exclusion.