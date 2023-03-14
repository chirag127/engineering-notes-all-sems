## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the problem of finding and resolving deadlocks in a distributed system, where a set of processes request and hold resources that are shared by other processes in the system. There are three main approaches to distributed deadlock detection: centralized, distributed, and hierarchical.

In the centralized approach, there is a single node that is responsible for collecting information about the resource requests and allocations of all the processes in the system, and detecting deadlocks using a global wait-for graph (WFG). A WFG is a directed graph that represents the dependencies among processes and resources. A node in the WFG can be either a process or a resource, and an edge from a process to a resource means that the process is requesting the resource, while an edge from a resource to a process means that the resource is allocated to the process. A deadlock exists in the system if and only if the WFG contains a cycle.

The following diagram illustrates the basic architecture of a centralized deadlock detection approach:

```
+-----------------+       +-----------------+
|                 |       |                 |
|  Process P1     |       |  Process P2     |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       v                         v
+-----------------+       +-----------------+
|                 |       |                 |
|  Resource R1    |       |  Resource R2    |
|                 |       |                 |
+-----------------+       +-----------------+
       ^                         ^
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       +-------------------------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       v                         v
+-----------------+
|                 |
|  Deadlock       |
|  Detector       |
|                 |
+-----------------+
```

The advantages of the centralized approach are that it is simple and easy to implement, and that it can detect deadlocks quickly and accurately. The disadvantages are that it imposes a high workload and communication overhead on the single node, and that it is vulnerable to single-point failures.

In the distributed approach, there is no single node that is in charge of deadlock detection, but rather each node participates in the process of collecting and analyzing information about the resource requests and allocations of the processes in the system. There are two main techniques for distributed deadlock detection: edge chasing and diffusing computation.

Edge chasing is a technique that involves sending probe messages along the edges of the WFG to detect cycles. A probe message contains the identity of the sender node and a list of nodes that have been visited by the message. When a node receives a probe message, it checks if it is already in the list of visited nodes. If yes, then a cycle has been detected and the node initiates the deadlock resolution. If no, then the node appends itself to the list and forwards the message to the next node along the edge of the WFG.

The following diagram illustrates the basic idea of edge chasing:

```
+-----------------+       +-----------------+
|                 |       |                 |
|  Process P1     |       |  Process P2     |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |<------------------------|
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |<------------------------|
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |