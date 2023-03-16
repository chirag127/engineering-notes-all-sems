### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. A process can enter the critical section only if it has the token. After exiting the critical section, the process passes the token to another process that is waiting for it.
  - Token based algorithms guarantee mutual exclusion and fairness, since the token is passed in a predefined order or based on requests. However, they have some drawbacks, such as the possibility of losing the token due to failures, the overhead of passing the token, and the delay of waiting for the token.
  - Examples of token based algorithms are the Suzuki-Kasami algorithm, the Raymond's tree algorithm, and the Maekawa's algorithm.

- Non token based algorithms
  - In non token based algorithms, a process communicates with a set of other processes to determine who should enter the critical section next. The communication is done by sending and receiving messages, such as requests, replies, and releases. A process can enter the critical section only if it receives a positive reply from all the processes in its set.
  - Non token based algorithms do not require a token, so they avoid the problems of token loss, token passing, and token waiting. However, they have other drawbacks, such as the possibility of deadlock, the overhead of message exchanges, and the dependency on the reliability of the communication channels.
  - Examples of non token based algorithms are the Ricart-Agrawala algorithm, the Lamport's timestamp algorithm, and the Singhal's dynamic information structure algorithm.