# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data concurrently and the outcome depends on the order of execution.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time .
- A critical section (CS) is a piece of code that accesses a shared resource or data .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token that is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the CS only if it receives permission messages from all or a subset of the other processes in the system.
  - Quorum-based algorithms: A process can enter the CS only if it receives permission messages from a majority or a weighted majority of the processes in the system.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system and to avoid conflicts and inconsistencies among the processes .
- The mutual exclusion theorem also imposes some performance criteria for the distributed mutual exclusion algorithms, such as fairness, bounded delay, message complexity, and synchronization delay .