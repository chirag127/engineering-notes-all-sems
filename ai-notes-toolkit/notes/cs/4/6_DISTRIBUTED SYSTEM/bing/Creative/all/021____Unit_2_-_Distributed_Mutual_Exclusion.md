# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in the system. Only the process that holds the token can enter the CS.
  - Permission-based algorithms: A process that wants to enter the CS must request permission from other processes in the system. Only if it receives permission from all or a majority of them, it can enter the CS.
  - Quorum-based algorithms: A process that wants to enter the CS must request permission from a subset of processes in the system, called a quorum. Only if it receives permission from all the processes in the quorum, it can enter the CS.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution .
  - Synchronization delay: The time elapsed between the instant a process requests to enter the CS and the instant it is allowed to do so .
  - System throughput: The rate at which the processes execute the CS .
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links .
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and a total ordering multicast to send the requests and replies .
  - Suzuki-Kasami algorithm: A token-based algorithm that uses a vector of sequence numbers to keep track of the requests and a broadcast to send the token .
  - Maekawa algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission and a request queue to handle conflicts .