
### Resource vs Communication Deadlocks

1. Resource deadlocks occur when two or more processes are waiting for each other to release a resource.
2. Communication deadlocks occur when two or more processes are waiting for each other to send a message.
3. Resource deadlocks can be detected using a distributed algorithm, such as the one proposed by Chandy and Misra.
4. Communication deadlocks can be detected using a distributed algorithm, such as the one proposed by Lamport.
5. The Chandy-Misra algorithm works by having each process send its request for a resource to its neighbors.
6. The Lamport algorithm works by having each process broadcast its request for a message to all other processes.
7. Both algorithms are based on the assumption that each process has a unique identifier, so that the requests can be identified and tracked.
8. In the Chandy-Misra algorithm, each process keeps track of the requests it has received, and the requests it has sent.
9. In the Lamport algorithm, each process keeps track of the messages it has sent and the messages it has received.
10. If a process detects a deadlock, it will send a message to the other processes in the system, informing them of the deadlock.