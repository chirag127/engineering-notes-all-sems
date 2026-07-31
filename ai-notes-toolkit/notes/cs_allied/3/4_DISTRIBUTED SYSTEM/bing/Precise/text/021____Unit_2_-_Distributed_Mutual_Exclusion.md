## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing. It refers to the problem of ensuring that, in a distributed system, no two processes access a shared resource simultaneously.

1. **Lamport's Algorithm**: This algorithm uses a logical clock to order requests for the critical section. Each process maintains a queue of requests, sorted by their timestamps. When a process wants to enter the critical section, it sends a request message to all other processes and waits for their replies. Once it has received replies from all other processes, it can enter the critical section.

2. **Ricart-Agrawala Algorithm**: This algorithm is an improvement over Lamport's algorithm. It uses the same basic idea of ordering requests using timestamps, but it reduces the number of messages required. When a process receives a request message, it only sends a reply if it is not currently in the critical section and if it has not already sent a request with a lower timestamp.

3. **Maekawa's Algorithm**: This algorithm reduces the number of messages required even further by dividing the processes into groups, called "voting sets". Each process belongs to multiple voting sets, and each voting set contains a majority of the processes. When a process wants to enter the critical section, it sends a request message to all processes in its voting sets and waits for their replies. Once it has received replies from a majority of the processes in each of its voting sets, it can enter the critical section.

These are some of the algorithms used for distributed mutual exclusion. Each has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.