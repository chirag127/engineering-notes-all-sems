## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- Distributed mutual exclusion algorithms can be classified into two categories: token-based and permission-based.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. The token is passed among the processes in a predefined order or by request. Only the process that holds the token can enter the critical section. Examples of token-based algorithms are the ring algorithm, the Suzuki-Kasami algorithm, and the Raymond algorithm.
- Permission-based algorithms use a voting scheme, where a process that wants to enter the critical section must request permission from a set of processes, called the quorum. The process can enter the critical section only if it receives a positive reply from all the processes in the quorum. Examples of permission-based algorithms are the Ricart-Agrawala algorithm, the Maekawa algorithm, and the Lamport algorithm.
- Distributed mutual exclusion algorithms must satisfy the following properties:
  - Safety: No two processes can be in the critical section at the same time.
  - Liveness: Every request to enter the critical section is eventually granted.
  - Fairness: No process is indefinitely postponed from entering the critical section.
- Distributed mutual exclusion algorithms can be evaluated based on the following performance metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting and entering the critical section.
  - Response time: The time elapsed between a process requesting and receiving the token or permission.
  - System throughput: The number of critical section executions per unit time.