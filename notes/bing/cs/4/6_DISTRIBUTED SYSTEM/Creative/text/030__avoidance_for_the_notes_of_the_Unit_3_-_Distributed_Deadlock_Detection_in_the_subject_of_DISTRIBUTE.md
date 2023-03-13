### Avoidance

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by avoiding unsafe states.
- Avoidance requires some knowledge of the resource requirements and the current allocation of each process in the system.
- Avoidance can be implemented using either static or dynamic methods.

#### Static Avoidance

- Static avoidance is based on the assumption that each process declares its maximum resource needs before it starts execution.
- Static avoidance uses a global state graph (GSG) to represent the resource allocation and requests of all processes in the system.
- A GSG is a directed graph where nodes are processes or resources, and edges are either requests or allocations.
- A request edge goes from a process to a resource, indicating that the process is waiting for the resource.
- An allocation edge goes from a resource to a process, indicating that the resource is allocated to the process.
- A GSG is safe if there is a path from each process node to a resource node that satisfies its request.
- A GSG is unsafe if there is no such path for some process node.
- A safe GSG guarantees that there is no deadlock in the system, while an unsafe GSG may lead to a deadlock.
- Static avoidance works by checking the safety of the GSG before granting any resource request.
- If the request leads to a safe GSG, it is granted; otherwise, it is denied or delayed until a safe GSG can be reached.
- Static avoidance has the advantage of being simple and easy to implement, but it has the disadvantages of being conservative and requiring a priori knowledge of the resource needs.

#### Dynamic Avoidance

- Dynamic avoidance is based on the assumption that each process declares its resource needs as it executes, rather than before it starts.
- Dynamic avoidance uses a wait-for graph (WFG) to represent the resource allocation and requests of all processes in the system.
- A WFG is a directed graph where nodes are processes, and edges are wait-for relations.
- A wait-for edge goes from a process to another process, indicating that the former is waiting for the latter to release some resource.
- A WFG is cyclic if there is a cycle of wait-for edges in the graph.
- A cyclic WFG indicates that there is a deadlock in the system, while an acyclic WFG indicates that there is no deadlock.
- Dynamic avoidance works by checking the cyclicity of the WFG before granting any resource request.
- If the request leads to an acyclic WFG, it is granted; otherwise, it is denied or delayed until an acyclic WFG can be reached.
- Dynamic avoidance has the advantage of being less conservative and not requiring a priori knowledge of the resource needs, but it has the disadvantages of being more complex and requiring more communication and synchronization.