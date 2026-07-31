# Token-based and Non-token-based Algorithms

## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed systems. It deals with the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based and non-token-based algorithms.

### Token-based Algorithms

Token-based algorithms use a token to control access to the shared resource. The token is passed between processes in a predefined order, and only the process holding the token is allowed to access the shared resource. Some examples of token-based algorithms include:

1. **Suzuki-Kasami's Algorithm**: This algorithm uses a token that contains a request queue and a vector timestamp. Processes send requests for the token to the current token holder, and the token is passed to the process with the earliest request in the queue.

2. **Raymond's Algorithm**: This algorithm uses a tree structure to organize the processes in the system. The token is passed along the edges of the tree, and processes send requests for the token to their parent in the tree.

### Non-token-based Algorithms

Non-token-based algorithms do not use a token to control access to the shared resource. Instead, they rely on message passing and other mechanisms to coordinate access. Some examples of non-token-based algorithms include:

1. **Lamport's Algorithm**: This algorithm uses a logical clock to timestamp requests for the shared resource. Processes send requests to all other processes in the system, and access is granted based on the timestamp of the request.

2. **Ricart-Agrawala's Algorithm**: This algorithm is similar to Lamport's algorithm, but it uses a vector timestamp instead of a logical clock. Processes send requests to all other processes in the system, and access is granted based on the vector timestamp of the request.

These are some of the token-based and non-token-based algorithms used for distributed mutual exclusion. Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system.