### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a program object that refers to the requirement of satisfying that no two concurrent processes are in a critical section at the same time.
- A critical section is a segment of code that accesses a shared resource or data that must be executed in a mutually exclusive manner.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time.
- A distributed system is a collection of independent and geographically dispersed processes that communicate by message passing and do not share memory or a common physical clock.
- To eliminate the mutual exclusion problem in a distributed system, an approach based on message passing is used.
- A site in a distributed system does not have complete information of the state of the system due to lack of shared memory and a common physical clock.
- Therefore, a mutual exclusion algorithm for a distributed system must satisfy the following requirements:

  - **Safety**: No two processes can execute the critical section simultaneously.
  - **Liveness**: Every process that requests to enter the critical section eventually gets the permission to do so.
  - **Fairness**: No process is indefinitely postponed from entering the critical section.
  - **Efficiency**: The algorithm should minimize the number and size of messages, the synchronization delay, and the system overhead.

- A mnemonic to remember these requirements is **SELF** (Safety, Liveness, Fairness, Efficiency).
- There are different types of mutual exclusion algorithms for distributed systems, such as:

  - **Centralized algorithms**: A single coordinator process grants permission to enter the critical section based on a request queue.
  - **Distributed algorithms**: Every process maintains a request queue and exchanges messages with other processes to reach an agreement on who can enter the critical section.
  - **Token-based algorithms**: A special message called a token is circulated among the processes and only the process that holds the token can enter the critical section.

- A mnemonic to remember these types is **CDT** (Centralized, Distributed, Token-based).
- An example of a centralized algorithm is the **Ricart-Agrawala algorithm**, which works as follows:

  - Each process has a logical clock that is incremented on every local event and updated on every message received.
  - A process that wants to enter the critical section sends a request message to the coordinator with its logical clock value.
  - The coordinator maintains a request queue ordered by the logical clock values and grants permission to the first process in the queue.
  - The coordinator sends a reply message to the requesting process, which can then enter the critical section.
  - After exiting the critical section, the process sends a release message to the coordinator, which removes the process from the queue and grants permission to the next process.

- An example of a distributed algorithm is the **Lamport's algorithm**, which works as follows:

  - Each process has a logical clock that is incremented on every local event and updated on every message received.
  - A process that wants to enter the critical section sends a request message to all other processes with its logical clock value.
  - A process that receives a request message replies with an acknowledgment message if it is not interested in the critical section or if its request has a higher logical clock value.
  - A process that receives an acknowledgment message from all other processes can enter the critical section.
  - After exiting the critical section, the process sends a release message to all other processes, which can then update their request queues.

- An example of a token-based algorithm is the **Suzuki-Kasami algorithm**, which works as follows:

  - There is a single token that contains a vector of sequence numbers, one for each process, indicating the number of requests made by each process.
  - A process that wants to enter the critical section sends a request message to the process that holds the token with its sequence number.
  - A process that receives a request message updates its vector with the received sequence number and compares it with its own vector to determine if the requesting process should get the token.
  - A process that receives the token can enter the critical section and updates its vector with its own sequence number.
  - After exiting the critical section, the process sends the token to the process with the highest sequence number in the vector that has not yet received the token.