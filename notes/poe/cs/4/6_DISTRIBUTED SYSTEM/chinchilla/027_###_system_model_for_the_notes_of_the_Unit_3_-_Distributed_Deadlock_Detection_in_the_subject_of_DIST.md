### System Model for the Notes of Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In a distributed system, multiple processes may request resources concurrently, leading to a deadlock situation where each process is waiting for a resource held by another process. To detect and resolve deadlocks in a distributed system, we need to understand the system model. 

The system model for distributed deadlock detection consists of the following components:

1. Processes: In a distributed system, processes are running on different machines and may communicate with each other to request resources. Each process has a unique identifier.

2. Resources: Resources can be physical or logical. Physical resources include devices such as printers, disks, and memory, while logical resources can be files, database records, or network connections. Each resource has a unique identifier.

3. Requests: A process can request one or more resources. Each request has a unique identifier.

4. Allocation: A resource can be allocated to a process. Once a resource is allocated, it cannot be allocated to another process until it is released.

5. Hold and Wait: A process holds a resource while waiting for another resource. This can cause a deadlock situation if two or more processes are waiting for a resource held by another process.

6. Wait-for graph: A wait-for graph is a directed graph that represents the allocation and waiting relationships between processes and resources. Each node in the graph represents a process or a resource, and each edge represents a request or an allocation relationship. A cycle in the wait-for graph indicates a deadlock.

7. Distributed Deadlock Detection Algorithm: The distributed deadlock detection algorithm periodically examines the wait-for graph to detect deadlocks. The algorithm can be centralized or distributed. In a centralized algorithm, a central server maintains the wait-for graph and detects deadlocks. In a distributed algorithm, each node maintains a portion of the wait-for graph and communicates with other nodes to detect deadlocks.

#### Learning Tricks:

- Mnemonic: "PRAWHWD" can be used to remember the components of the system model: Processes, Resources, Requests, Allocation, Hold and Wait, Wait-for graph, and Distributed Deadlock Detection Algorithm.
- To understand the wait-for graph, remember that each node represents a process or a resource, and each edge represents a request or an allocation relationship. A cycle in the graph indicates a deadlock.

Understanding the system model is crucial for implementing an effective distributed deadlock detection algorithm. By periodically examining the wait-for graph, the algorithm can detect and resolve deadlocks in a distributed system.