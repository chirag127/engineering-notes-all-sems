## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in the system. A process can enter the critical section only if it possesses the token.
  - Permission-based algorithms: A process requests permission from other processes in the system before entering the critical section. A process can enter the critical section only if it receives permission from all or a majority of the processes.
  - Quorum-based algorithms: A process requests permission from a subset of processes in the system before entering the critical section. A process can enter the critical section only if it receives permission from a quorum of processes.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The delay between the time a process requests to enter the critical section and the time it is granted permission.
  - System throughput: The rate at which processes can execute the critical section.
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links.
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and replies .
  - Suzuki-Kasami algorithm: A token-based algorithm that uses a request vector to keep track of the pending requests and a token that contains a privilege vector to indicate the processes that have executed the critical section .
  - Maekawa's algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission to a requesting process .
  - Lamport's bakery algorithm: A permission-based algorithm that uses a numbering scheme to assign priority to the processes and a shared queue to order the requests .