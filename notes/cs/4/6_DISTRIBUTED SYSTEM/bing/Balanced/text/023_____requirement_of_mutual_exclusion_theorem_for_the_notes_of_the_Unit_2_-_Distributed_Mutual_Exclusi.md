### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and the outcome depends on the order of execution.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is a piece of code that accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the processes in the system. The process sends request messages and waits for reply messages before entering the CS.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a quorum of the processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the CS.
- The mutual exclusion theorem states that any algorithm for implementing distributed mutual exclusion must satisfy the following properties:
  - Safety: At most one process can execute the CS at any given time.
  - Liveness: Every request to enter the CS eventually succeeds.
  - Fairness: No process is indefinitely postponed from entering the CS.