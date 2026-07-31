### Edge Chasing Algorithms for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In distributed systems, deadlock detection is a crucial task to ensure the system's liveliness. Edge chasing algorithms are a class of distributed deadlock detection algorithms that are commonly used in distributed systems. In this section, we will explore the edge chasing algorithms and their working in detail.

#### What are Edge Chasing Algorithms?

An edge chasing algorithm is a distributed deadlock detection algorithm that is based on the concept of a wait-for graph. In this algorithm, each node maintains a local wait-for graph that represents the dependencies between the processes in the system. Each edge in the graph represents a process that is waiting for a resource held by another process.

#### How do Edge Chasing Algorithms Work?

The following are the steps involved in the working of edge chasing algorithms:

1. Each node maintains a local wait-for graph that represents the dependencies between the processes in the system.

2. When a process requests a resource, it sends a message to the process holding the resource.

3. If the process holding the resource is not able to grant the request, it adds a new edge to its local wait-for graph.

4. The process holding the resource then sends a message to the process that made the request, informing it about the new edge in the wait-for graph.

5. The process that made the request then adds the new edge to its local wait-for graph.

6. If a process detects a cycle in its wait-for graph, it sends a message to all the processes on the cycle, informing them about the deadlock.

7. Upon receiving the message, each process releases all the resources it holds and waits for a random period before re-requesting the resources.

8. The process holding the resource receives the release message and updates its local wait-for graph by removing the edges corresponding to the released resources.

9. The process that initially made the request receives the release message and also updates its local wait-for graph by removing the edges corresponding to the released resources.

10. The system then resumes normal operation, and the processes can continue requesting and releasing resources.

#### Advantages and Disadvantages of Edge Chasing Algorithms

The following are the advantages of edge chasing algorithms:

- Edge chasing algorithms are simple, easy to implement, and require minimal communication overhead.

- These algorithms can detect deadlocks in real-time and have a low detection time.

The following are the disadvantages of edge chasing algorithms:

- These algorithms are not suitable for large-scale systems as they require a lot of communication overhead.

- Edge chasing algorithms can produce false positives, which can result in unnecessary resource releases and system downtime.

#### Conclusion

In conclusion, edge chasing algorithms are a class of distributed deadlock detection algorithms that are widely used in distributed systems. These algorithms are based on the concept of a wait-for graph and are simple to implement, but they have their limitations. Understanding the working and limitations of edge chasing algorithms is crucial for designing efficient and reliable distributed systems.