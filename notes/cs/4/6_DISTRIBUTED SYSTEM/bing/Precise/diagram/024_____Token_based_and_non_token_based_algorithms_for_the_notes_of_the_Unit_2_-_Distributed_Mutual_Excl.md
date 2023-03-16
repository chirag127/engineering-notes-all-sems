### Unit 2 - Distributed Mutual Exclusion: Token-based and Non-token-based Algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It deals with the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based and non-token-based algorithms.

#### Token-based Algorithms
Token-based algorithms use a token to control access to the shared resource. The token is passed between processes in a predefined order, and only the process holding the token is allowed to access the shared resource. Some examples of token-based algorithms include:
- **The Ricart-Agrawala Algorithm:** This algorithm uses a logical clock to order requests for the shared resource. Each process maintains a queue of pending requests, and the token is passed to the process with the earliest request.
- **The Suzuki-Kasami Algorithm:** This algorithm uses a vector of sequence numbers to order requests for the shared resource. Each process maintains a queue of pending requests, and the token is passed to the process with the highest sequence number.

#### Non-token-based Algorithms
Non-token-based algorithms do not use a token to control access to the shared resource. Instead, they rely on message passing and other mechanisms to coordinate access. Some examples of non-token-based algorithms include:
- **The Lamport Algorithm:** This algorithm uses a logical clock to order requests for the shared resource. Each process maintains a queue of pending requests, and the process with the earliest request is granted access to the shared resource.
- **The Maekawa Algorithm:** This algorithm uses a voting mechanism to coordinate access to the shared resource. Each process maintains a set of voting processes, and a process is granted access to the shared resource only if it receives a majority of votes.

In summary, distributed mutual exclusion can be achieved using either token-based or non-token-based algorithms. Each approach has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system.