### distributed dead lock detection for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM
Distributed Deadlock Detection involves detecting deadlocks in a distributed system, where multiple processes are executing on different nodes and communicating with each other. The following are the steps involved in detecting deadlocks in a distributed system:

1. Resource allocation graph: A resource allocation graph is constructed representing the resources and processes in the system.

2. Wait-for graph: A wait-for graph is constructed from the resource allocation graph, where each process is represented as a node and a directed edge from process P1 to process P2 represents that P1 is waiting for a resource held by P2.

3. Cycle detection: Cycles in the wait-for graph indicate a deadlock.

4. Global state information: A coordinator process collects information about the state of all processes in the system, including the resource allocation and wait-for graphs.

5. Deadlock detection: The coordinator process analyzes the information to detect deadlocks.

6. Deadlock resolution: If a deadlock is detected, the coordinator process selects a process to terminate, releasing its resources and allowing the other processes to continue execution.
