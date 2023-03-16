## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems, because they require global knowledge and coordination of all processes and resources.
- Deadlock detection is the best approach to handle deadlocks in distributed systems. It involves two steps: detecting the existence of deadlocks and resolving the detected deadlocks.
- Deadlock detection requires examining the status of process-resource interactions for the presence of cyclic wait. A cycle in the wait-for graph indicates a deadlock.
- Deadlock detection can be done by two methods: centralized and distributed.
- Centralized deadlock detection involves a designated node that collects the local wait-for graphs from all nodes and constructs a global wait-for graph to detect cycles. This method has the advantages of simplicity and efficiency, but also the disadvantages of single point of failure and communication overhead.
- Distributed deadlock detection involves a distributed algorithm that runs on all nodes and detects cycles in the wait-for graph without constructing a global wait-for graph. This method has the advantages of fault tolerance and scalability, but also the disadvantages of complexity and message overhead.
- Distributed deadlock detection can be further classified into two types: path-pushing and edge-chasing.
- Path-pushing algorithms propagate the dependency information along the wait-for graph and detect cycles when a node receives its own dependency information. Examples of path-pushing algorithms are the Chandy-Misra-Haas algorithm and the Ho-Ramamoorthy algorithm.
- Edge-chasing algorithms initiate probes along the wait-for graph and detect cycles when a probe returns to its initiator. Examples of edge-chasing algorithms are the Huang algorithm and the Menasce-Muntz algorithm.
- Deadlock resolution involves selecting and aborting some of the deadlocked processes to break the cycle and release the resources. The selection criteria can be based on factors such as priority, age, number of resources, etc.