### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource. The token is passed from one process to another according to some protocol.
  - Token based algorithms have the advantage of being simple and efficient, as they do not require any communication among processes except for passing the token. They also avoid the problem of deadlock, as there is always a unique token in the system. However, they have some drawbacks, such as the possibility of losing the token due to failures, the overhead of token passing, and the lack of fairness, as some processes may have to wait for a long time to get the token.
  - Examples of token based algorithms are the Raymond's algorithm, the Suzuki-Kasami algorithm, and the Maekawa's algorithm.
- Non token based algorithms
  - In non token based algorithms, there is no token in the system. Instead, the processes communicate with each other using messages to request and grant permission to enter the critical section. The processes use some criteria, such as timestamps or logical clocks, to order the requests and resolve conflicts.
  - Non token based algorithms have the advantage of being more robust to failures, as they do not depend on a single token. They also allow for more flexibility and fairness, as the processes can choose whom to grant permission based on some policy. However, they have some drawbacks, such as the complexity and overhead of message exchange, the possibility of deadlock, and the need for synchronization among processes.
  - Examples of non token based algorithms are the Ricart-Agrawala algorithm, the Lamport's algorithm, and the Singhal's algorithm.