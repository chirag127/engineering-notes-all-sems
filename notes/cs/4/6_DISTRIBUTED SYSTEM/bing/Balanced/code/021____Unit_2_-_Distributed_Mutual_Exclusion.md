## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or by request. Examples are Suzuki-Kasami's algorithm and Raymond's algorithm.
  - Permission-based algorithms: A process can enter the CS only if it receives permission from all or a subset of other processes. The process sends a request message to other processes and waits for their reply messages. Examples are Lamport's algorithm and Ricart-Agrawala's algorithm.
  - Quorum-based algorithms: A process can enter the CS only if it receives permission from a majority or a quorum of other processes. The process sends a request message to a subset of processes and waits for their reply messages. Examples are Maekawa's algorithm and Sopena's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution.
  - Synchronization delay: The time elapsed between a process requesting the CS and being granted the CS, assuming no other process is in the CS or requesting the CS.
  - Response time: The time elapsed between a process requesting the CS and being granted the CS, assuming some other processes may be in the CS or requesting the CS.
  - System throughput: The number of times the CS can be executed per unit time in the system.