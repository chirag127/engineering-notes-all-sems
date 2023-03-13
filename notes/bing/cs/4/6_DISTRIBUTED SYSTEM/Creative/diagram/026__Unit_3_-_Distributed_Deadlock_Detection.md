## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of finding and resolving deadlocks in a distributed system. A deadlock is a situation where a set of processes are waiting for resources that are held by other processes in the same set, and none of them can proceed. There are three main approaches to distributed deadlock detection: centralized, distributed, and hierarchical.

The following diagram illustrates the basic architecture of a centralized approach:

```
+-----------------+      +-----------------+
| Process 1       |      | Process 2       |
| +-------------+ |      | +-------------+ |
| | Resource R1 | |      | | Resource R2 | |
| +-------------+ |      | +-------------+ |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        +-----------------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+      +-----------------+
| Wait-for Graph  |      | Deadlock        |
| Manager         |----->| Detector        |
+-----------------+      +-----------------+
```

In this approach, there is a single node that collects the wait-for information from all the processes in the system and constructs a global wait-for graph. The wait-for graph is a directed graph that represents the dependencies between processes and resources. A node in the graph is either a process or a resource, and an edge from a process to a resource means that the process is requesting the resource, while an edge from a resource to a process means that the resource is allocated to the process. A cycle in the wait-for graph indicates a deadlock. The deadlock detector periodically checks the wait-for graph for cycles and initiates the resolution of the detected deadlocks.

The advantages of this approach are that it is simple and easy to implement, and it can detect all the deadlocks in the system. The disadvantages are that it requires a lot of communication and computation overhead, and it introduces a single point of failure. If the wait-for graph manager or the deadlock detector fails, the whole system may become unable to detect or resolve deadlocks.

The following diagram illustrates the basic architecture of a distributed approach:

```
+-----------------+      +-----------------+
| Process 1       |      | Process 2       |
| +-------------+ |      | +-------------+ |
| | Resource R1 | |      | | Resource R2 | |
| +-------------+ |      | +-------------+ |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+      +-----------------+
| Local Wait-for  |      | Local Wait-for  |
| Graph           |      | Graph           |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+      +-----------------+
| Deadlock        |      | Deadlock        |
| Detector        |      | Detector        |
+-----------------+      +-----------------+
```

In this approach, each node maintains its own local wait-for graph and runs its own deadlock detector. The local wait-for graph contains only the information about the processes and resources that are local to the node. The deadlock detector periodically checks the local wait-for graph for cycles and initiates the resolution of the local deadlocks. However, this approach may not be able to detect global deadlocks, which involve processes and resources from different nodes. To detect global deadlocks, the nodes need to exchange messages with each other and cooperate in the detection process. There are different algorithms for distributed deadlock detection, such as the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.

The advantages of this approach are that it avoids a single point of failure, reduces