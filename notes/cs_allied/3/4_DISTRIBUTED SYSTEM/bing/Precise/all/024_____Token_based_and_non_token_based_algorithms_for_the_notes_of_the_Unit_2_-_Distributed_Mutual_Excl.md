# Unit 2 - Distributed Mutual Exclusion

## Token based and non token based algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It refers to the problem of ensuring that, in a distributed system, only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based algorithms and non-token-based algorithms.

### Token-based algorithms

Token-based algorithms use a token to control access to the shared resource. The token is passed between processes in the system, and only the process that holds the token is allowed to access the shared resource. This approach has the advantage of being simple and easy to implement. However, it can suffer from performance issues, as the token must be passed between processes, which can take time.

Some examples of token-based algorithms include:
- The Ricart-Agrawala algorithm
- The Suzuki-Kasami algorithm
- The Raymond's tree-based algorithm

### Non-token-based algorithms

Non-token-based algorithms do not use a token to control access to the shared resource. Instead, they use other mechanisms, such as message passing or timestamps, to ensure that only one process can access the shared resource at a time. This approach can be more efficient than token-based algorithms, as it does not require the passing of a token between processes. However, it can be more complex to implement.

Some examples of non-token-based algorithms include:
- The Lamport's algorithm
- The Maekawa's algorithm
- The Carvalho-Roucairol algorithm

Both token-based and non-token-based algorithms have their advantages and disadvantages, and the choice of which approach to use will depend on the specific requirements of the distributed system in question. It is important to carefully evaluate the trade-offs between the two approaches before making a decision.