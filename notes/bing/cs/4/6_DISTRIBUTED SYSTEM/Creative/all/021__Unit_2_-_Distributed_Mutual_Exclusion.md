## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are different types of distributed mutual exclusion algorithms, such as:
  - Centralized algorithms: A single coordinator process grants permission to enter the CS to the requesting processes .
  - Distributed algorithms: Each process maintains a local state and communicates with other processes to decide who can enter the CS .
  - Token-based algorithms: A special message called token is circulated among the processes and only the process holding the token can enter the CS .
- Some of the performance metrics for evaluating distributed mutual exclusion algorithms are :
  - Message complexity: The number of messages exchanged per CS execution.
  - Synchronization delay: The time elapsed between the first request for the CS and the actual entry to the CS.
  - Response time: The time elapsed between a request for the CS and the actual entry to the CS.
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links.
- Some of the advantages of distributed mutual exclusion are:
  - It avoids the need for a centralized authority or a global state.
  - It allows concurrent access to multiple resources by different processes.
  - It preserves the autonomy and scalability of the distributed system.
- Some of the disadvantages of distributed mutual exclusion are:
  - It requires more communication overhead and coordination among the processes.
  - It may suffer from deadlock, starvation, or livelock situations.
  - It may be vulnerable to malicious attacks or Byzantine failures.

- A possible mnemonic to remember the types of distributed mutual exclusion algorithms is **CDT** (Centralized, Distributed, Token-based).
- A possible learning trick to understand the concept of distributed mutual exclusion is to imagine a group of people sharing a bathroom. Only one person can use the bathroom at a time, and they need to communicate with each other to avoid conflicts. The bathroom is the shared resource, the person using the bathroom is the process in the CS, and the communication is the message passing. Different algorithms can be applied to this scenario, such as:
  - Centralized: One person acts as the coordinator and decides who can use the bathroom next based on a queue or a priority order.
  - Distributed: Each person maintains a local state (such as a timestamp or a request vector) and communicates with other people to decide who can use the bathroom next based on a logical order or a voting scheme.
  - Token-based: A special object (such as a key or a card) is circulated among the people and only the person holding the object can use the bathroom.