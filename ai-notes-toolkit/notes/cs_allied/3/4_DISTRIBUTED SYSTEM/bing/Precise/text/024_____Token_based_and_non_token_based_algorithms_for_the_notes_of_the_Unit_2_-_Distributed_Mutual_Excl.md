### Token based and non token based algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It refers to the problem of ensuring that, in a distributed system, only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based algorithms and non-token-based algorithms.

1. **Token-based algorithms:** In token-based algorithms, a token is passed between processes in the system. The process holding the token has the right to access the shared resource. Once it has finished accessing the resource, it passes the token to the next process in line. Examples of token-based algorithms include the Ricart-Agrawala algorithm and the Suzuki-Kasami algorithm.

2. **Non-token-based algorithms:** In non-token-based algorithms, processes communicate with each other to coordinate access to the shared resource. These algorithms typically use message passing to exchange information about which process should access the resource next. Examples of non-token-based algorithms include the Lamport's algorithm and the Maekawa's algorithm.

Both token-based and non-token-based algorithms have their advantages and disadvantages. Token-based algorithms are generally simpler to implement and understand, but can suffer from problems such as token loss or duplication. Non-token-based algorithms can be more efficient in terms of message complexity, but can be more difficult to implement and understand.

In summary, distributed mutual exclusion is an important problem in distributed systems, and can be solved using either token-based or non-token-based algorithms. Each approach has its own advantages and disadvantages, and the choice of algorithm will depend on the specific requirements of the system.