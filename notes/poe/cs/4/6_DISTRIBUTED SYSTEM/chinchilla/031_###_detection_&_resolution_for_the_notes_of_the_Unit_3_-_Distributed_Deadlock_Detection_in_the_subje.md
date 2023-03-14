### Detection & Resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Distributed deadlock detection is a mechanism that helps to identify and resolve deadlocks in distributed systems. Deadlocks occur when two or more processes are waiting for each other to release resources, resulting in a state of mutual waiting. This can lead to a system-wide deadlock, where no process can proceed until the deadlock is resolved. In this unit, we will discuss the detection and resolution of deadlocks in distributed systems.

#### Detection of Deadlocks

There are two approaches to detecting deadlocks in distributed systems:

1. **Centralized Approach**: In this approach, a single process is responsible for detecting and resolving deadlocks. This process maintains a global wait-for graph that represents the dependencies between processes and resources. The process periodically checks the wait-for graph for cycles, which indicate the presence of deadlocks. If a deadlock is detected, the process initiates a resolution algorithm to break the cycle and release the resources.

2. **Distributed Approach**: In this approach, each process maintains a local wait-for graph that represents the dependencies between itself and other processes. The processes periodically exchange messages to update their local wait-for graphs. If a process detects a cycle in its local wait-for graph, it sends a message to the processes involved in the cycle to initiate a resolution algorithm and release the resources.

#### Resolution of Deadlocks

There are several approaches to resolving deadlocks in distributed systems:

1. **Abort and Restart**: In this approach, one or more processes involved in the deadlock are aborted, and their resources are released. The aborted processes are then restarted, allowing them to acquire the resources they need to proceed.

2. **Resource Preemption**: In this approach, resources are preempted from one or more processes involved in the deadlock, allowing other processes to acquire them and proceed. The preempted processes are then restarted, allowing them to acquire the resources they need to proceed.

3. **Wait-for Graph modification**: In this approach, the wait-for graph is modified to break the cycle and release the resources. This can be achieved by adding additional edges or removing existing edges from the wait-for graph.

#### Mnemonics and Learning Tricks

1. Remember the two approaches to detecting deadlocks: Centralized and Distributed. Think of a "Centralized" approach as one where there is a single "center" responsible for detecting deadlocks, while a "Distributed" approach involves multiple processes working together to detect deadlocks.

2. Remember the three approaches to resolving deadlocks: Abort and Restart, Resource Preemption, and Wait-for Graph modification. Use the acronym "ARW" to help remember these approaches.

By understanding the detection and resolution techniques for distributed deadlocks, you can design more efficient and reliable distributed systems.