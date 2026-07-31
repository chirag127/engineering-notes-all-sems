
## Unit 2 - Distributed Mutual Exclusion

1. Distributed mutual exclusion is a process that ensures that only one process can access a shared resource at a given time. 
2. In a distributed system, multiple nodes can access the same resource, making it difficult to ensure that only one node has access. 
3. Distributed mutual exclusion algorithms enable processes to coordinate access to a shared resource. 
4. The Ricart-Agrawala algorithm is an example of a distributed mutual exclusion algorithm. It uses a distributed token-based approach to ensure that only one process has access to the resource at a given time. 
5. The algorithm requires each node to request access to the shared resource, and then wait for a reply from all other nodes. 
6. If all other nodes grant permission, the requesting node is granted access. If any node denies permission, the requesting node must wait for a predefined period of time before requesting again. 
7. The algorithm is designed to be fair, meaning that all nodes have an equal chance of accessing the resource. 
8. The algorithm is also designed to be deadlock-free, meaning that it is not possible for two nodes to be waiting for each other indefinitely. 
9. The algorithm is also fault-tolerant, meaning that it can continue to function even if one or more nodes fail.