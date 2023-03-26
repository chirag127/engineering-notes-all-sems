## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed systems, where several processes compete for accessing a shared resource. In this unit, we will study the different algorithms used to achieve distributed mutual exclusion in a distributed system.

### 1. Introduction

- Distributed mutual exclusion is a problem that arises when several processes in a distributed system need to access a shared resource simultaneously.
- The goal of distributed mutual exclusion is to ensure that only one process can access the shared resource at a time to maintain consistency and avoid conflicts.

### 2. Centralized Algorithm

- The centralized algorithm uses a central server to manage the access to the shared resource.
- Each process sends a request to the central server to gain access to the shared resource, and the server grants access to one process at a time.
- The centralized algorithm is simple to implement, but it is not scalable and can be a single point of failure.

### 3. Token-based Algorithm

- The token-based algorithm is a distributed algorithm where a token is passed among the processes to grant access to the shared resource.
- A process can access the shared resource only if it holds the token.
- When a process finishes using the shared resource, it passes the token to the next process in a pre-defined order.
- The token-based algorithm is scalable, but it requires a pre-defined order to pass the token, which can be a challenge in a dynamic system.

### 4. Distributed Queuing Algorithm

- The distributed queuing algorithm is a distributed algorithm where each process maintains a queue of requests to access the shared resource.
- A process can access the shared resource only if it is at the head of the queue.
- When a process finishes using the shared resource, it removes itself from the queue and notifies the next process in the queue that it can access the shared resource.
- The distributed queuing algorithm is scalable and does not have a single point of failure, but it requires a robust communication mechanism to maintain the queue.

### 5. Conclusion

- Distributed mutual exclusion is a fundamental problem in distributed systems that requires careful consideration when designing distributed algorithms.
- The centralized algorithm, token-based algorithm, and distributed queuing algorithm are three widely used algorithms to achieve distributed mutual exclusion.
- Each algorithm has its advantages and disadvantages depending on the system's requirements and the type of shared resource being accessed.