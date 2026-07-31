# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a computer, or a cluster of computers that share resources and execute tasks.
- A resource can be a physical device, such as a printer or a disk, or a logical entity, such as a file or a lock.
- A process can request, use, and release resources according to some protocol.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the same set, and none of them can proceed.
- Deadlock detection is the problem of finding and resolving deadlocks in a distributed system.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.

## Centralized Approach

- In the centralized approach, one node is designated as the deadlock detector, and it is responsible for collecting and analyzing the information about the process-resource interactions in the system.
- The deadlock detector maintains a global wait-for graph (WFG), which is a directed graph that represents the dependencies among processes and resources.
- A node in the WFG is either a process or a resource, and an edge from a process to a resource indicates a request, while an edge from a resource to a process indicates an allocation.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- The deadlock detector periodically requests the local wait-for graphs (LWFGs) from each node, and constructs the global WFG by merging the LWFGs.
- The deadlock detector then runs a cycle detection algorithm on the global WFG, and if a cycle is found, it initiates a recovery action, such as aborting one or more processes in the cycle.
- The advantages of the centralized approach are simplicity and efficiency, as the deadlock detection is performed by a single node with a global view of the system.
- The disadvantages of the centralized approach are scalability and reliability, as the deadlock detector can become a bottleneck and a single point of failure in the system.

## Hierarchical Approach

- In the hierarchical approach, the system is divided into a hierarchy of clusters, and each cluster has a local deadlock detector that is in charge of the nodes in that cluster.
- The local deadlock detectors communicate with each other through a coordinator, which is a node that acts as the deadlock detector for the whole system.
- The coordinator maintains a global WFG, which is a reduced version of the WFG that only contains the inter-cluster dependencies.
- A node in the global WFG is either a cluster or a resource, and an edge from a cluster to a resource indicates a request, while an edge from a resource to a cluster indicates an allocation.
- A deadlock exists in the system if and only if the global WFG contains a cycle.
- The coordinator periodically requests the local WFGs from each cluster, and constructs the global WFG by merging the local WFGs.
- The coordinator then runs a cycle detection algorithm on the global WFG, and if a cycle is found, it notifies the local deadlock detectors of the clusters involved in the cycle, and they initiate a recovery action, such as aborting one or more processes in the cycle.
- The advantages of the hierarchical approach are scalability and reliability, as the deadlock detection is distributed among multiple nodes, and the coordinator can be replicated for fault tolerance.
- The disadvantages of the hierarchical approach are complexity and overhead, as the deadlock detection requires more communication and coordination among the nodes.

## Distributed Approach

- In the distributed approach, there is no central or hierarchical authority for deadlock detection, and each node participates in the deadlock detection process.
- The distributed approach relies on a technique called edge chasing, which is a distributed cycle detection algorithm that uses special messages called probes to trace the dependencies among processes and resources.
- A probe is a message that contains the identity of the sender and a list of nodes that have been visited by the probe.
- A node sends a probe to another node when it suspects that there is a dependency between them, and the probe travels along the edges of the WFG until it either reaches the sender or a dead end.
- If the probe reaches the sender, it means that a cycle has been detected, and the sender initiates a recovery action, such as aborting itself or another process in the cycle.
- If the probe reaches a dead end, it means that there is no cycle, and the probe is discarded.
- The advantages of the distributed approach are scalability and reliability, as the deadlock detection is performed by the nodes themselves, and there is no single point