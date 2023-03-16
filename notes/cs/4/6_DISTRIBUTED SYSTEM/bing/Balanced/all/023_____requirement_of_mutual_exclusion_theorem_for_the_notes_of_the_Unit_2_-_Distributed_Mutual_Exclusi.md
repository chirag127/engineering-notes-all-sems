# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and at least one of them modifies it.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section (CS) is a segment of code that accesses a shared resource or data  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter its CS only if it possesses a unique token that is circulated among the processes.
  - Permission-based algorithms: A process can enter its CS only if it receives permission from all or a subset of the processes.
  - Quorum-based algorithms: A process can enter its CS only if it receives permission from a majority or a weighted majority of the processes.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system.
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following properties:
  - Safety: No two processes can be in their CS at the same time.
  - Liveness: Every request to enter the CS eventually succeeds.
  - Fairness: No process is indefinitely postponed from entering its CS.
  - Fault-tolerance: The algorithm can tolerate some failures of processes or messages.