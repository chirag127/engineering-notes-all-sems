## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- A distributed mutual exclusion algorithm must satisfy the following requirements :
  - Safety: Only one process can execute the critical section (CS) at any given time.
  - Liveness: Every request for the CS is eventually granted.
  - Fairness: No process is indefinitely postponed or starved while requesting the CS.
- Distributed mutual exclusion algorithms can be classified into two categories :
  - Permission-based algorithms: A process must obtain permission from other processes before entering the CS. Examples are Lamport's algorithm, Ricart-Agrawala algorithm, Maekawa's algorithm, etc.
  - Token-based algorithms: A process must hold a special message called token to enter the CS. The token is passed among the processes in a predefined order. Examples are Suzuki-Kasami's algorithm, Raymond's algorithm, etc.