# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics :
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between the instant a process requests to enter the critical section and the instant it is allowed to do so, assuming that no other process is in the critical section.
  - System throughput: The number of times the critical section is executed per unit time in the system.
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and replies. It has a message complexity of 2(N-1) per critical section entry, where N is the number of processes in the system .
  - Lamport's bakery algorithm: A token-based algorithm that uses a logical clock and a queue to order the requests and grant the token. It has a message complexity of 3(N-1) per critical section entry, where N is the number of processes in the system .
  - Maekawa's algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission. It has a message complexity of 2√N per critical section entry, where N is the number of processes in the system .