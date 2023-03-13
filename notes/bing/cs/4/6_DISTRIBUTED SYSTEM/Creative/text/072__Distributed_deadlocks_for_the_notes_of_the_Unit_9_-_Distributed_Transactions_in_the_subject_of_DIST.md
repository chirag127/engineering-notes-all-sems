### Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release some resources, and none of them can proceed  .
- Distributed deadlocks can occur in distributed systems when **distributed transactions** or **concurrency control** is being used.
- Distributed deadlocks are more difficult to avoid, prevent, or even detect than deadlocks in centralized systems, because all relevant information is distributed over multiple machines .
- Several strategies can be used to handle distributed deadlocks:
  - **Deadlock prevention**: avoid one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) by using appropriate protocols or algorithms.
  - **Deadlock avoidance**: use some information about resource requirements and availability to allocate resources in a safe manner that avoids deadlock states.
  - **Deadlock detection**: periodically check for the existence of deadlocks using some methods such as global wait-for graphs or distributed algorithms, and then resolve them by aborting or restarting some processes.
  - **Deadlock ignorance**: ignore the possibility of deadlocks and assume that they will not occur or will be rare, and rely on timeouts or user intervention to handle them if they do occur.
- There are three main approaches to detect distributed deadlocks:
  - **Centralized approach**: designate a single node as the deadlock detector, and have all nodes send their local wait-for graphs to it periodically. The deadlock detector then constructs a global wait-for graph and checks for cycles using some algorithm such as depth-first search or topological sorting.
  - **Hierarchical approach**: organize the nodes into a hierarchy of clusters, and have each cluster elect a coordinator node as the deadlock detector for that cluster. The coordinator nodes then exchange their local wait-for graphs with each other periodically, and check for cycles using some algorithm such as depth-first search or topological sorting.
  - **Distributed approach**: use a distributed algorithm that does not require a central or hierarchical coordinator, and instead relies on message passing and local computations to detect cycles. One such algorithm is **edge chasing**, which involves sending probe messages along the edges of the wait-for graph, and detecting cycles when a probe message returns to its originator.