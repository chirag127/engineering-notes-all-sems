## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of detecting deadlocks in a distributed system. A deadlock occurs when two or more processes are blocked, waiting for resources held by each other. In a distributed system, this can happen when processes on different nodes are involved.

1. **Deadlock detection algorithms**: There are several algorithms for detecting deadlocks in distributed systems, including the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.

2. **Path-pushing algorithm**: In the path-pushing algorithm, each node maintains a wait-for graph, which represents the dependencies between processes. When a process is blocked, it sends a probe message to the node holding the resource it is waiting for. The probe message contains the path of nodes it has visited. If the probe message reaches a node that has already been visited, a deadlock is detected.

3. **Edge-chasing algorithm**: The edge-chasing algorithm is similar to the path-pushing algorithm, but instead of sending a probe message, each node sends a probe message to all of its outgoing edges in the wait-for graph. If a node receives a probe message from one of its incoming edges, it forwards the message to all of its outgoing edges. If a node receives a probe message from an edge that it has already sent a probe message to, a deadlock is detected.

4. **Diffusing computation algorithm**: In the diffusing computation algorithm, each node maintains a set of diffusing computations, which represent the dependencies between processes. When a process is blocked, it initiates a diffusing computation. The diffusing computation is propagated to all nodes in the system, and if a cycle is detected, a deadlock is detected.

5. **Deadlock resolution**: Once a deadlock is detected, it must be resolved. This can be done by aborting one or more of the processes involved in the deadlock, or by preempting resources from one or more of the processes.

6. **Challenges**: Detecting deadlocks in a distributed system can be challenging due to the lack of global knowledge and the need for coordination between nodes. Additionally, the detection and resolution of deadlocks can introduce additional overhead and complexity into the system.