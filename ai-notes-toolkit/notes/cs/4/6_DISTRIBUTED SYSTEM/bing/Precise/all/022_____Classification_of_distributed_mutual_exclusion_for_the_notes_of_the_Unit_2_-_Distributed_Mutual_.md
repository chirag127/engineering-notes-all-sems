# Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed systems. It refers to the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. There are several algorithms for achieving distributed mutual exclusion, and they can be classified into two main categories: token-based and non-token-based.

## Token-based algorithms
In token-based algorithms, a unique token is circulated among the processes in the system. Only the process that holds the token is allowed to access the shared resource. Once the process has finished accessing the resource, it passes the token to the next process in the queue. Examples of token-based algorithms include the Ricart-Agrawala algorithm and the Suzuki-Kasami algorithm.

## Non-token-based algorithms
In non-token-based algorithms, processes communicate with each other to coordinate access to the shared resource. These algorithms can be further classified into permission-based and quorum-based algorithms.

### Permission-based algorithms
In permission-based algorithms, a process must obtain permission from all other processes in the system before accessing the shared resource. Examples of permission-based algorithms include the Lamport algorithm and the Ricart-Agrawala algorithm.

### Quorum-based algorithms
In quorum-based algorithms, a process must obtain permission from a subset of processes, called a quorum, before accessing the shared resource. Examples of quorum-based algorithms include the Maekawa algorithm and the Raymond algorithm.

These are the main classifications of distributed mutual exclusion algorithms. Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system.