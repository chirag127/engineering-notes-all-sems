### Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main types of distributed deadlocks:
  - **Communication deadlocks**: occur when processes are waiting for messages from each other that will never arrive.
  - **Resource deadlocks**: occur when processes are holding some resources and requesting others that are held by other processes.
  - **Hybrid deadlocks**: occur when both communication and resource deadlocks are involved.
- There are three main approaches to handle distributed deadlocks :
  - **Deadlock prevention**: avoid creating cycles in the resource allocation graph by imposing some ordering or restrictions on resource requests and releases.
  - **Deadlock avoidance**: use some information about resource availability and process requirements to make safe decisions about resource allocation that will not lead to deadlocks.
  - **Deadlock detection**: allow deadlocks to occur, but detect them and resolve them by aborting or restarting some processes or releasing some resources.
- There are several techniques to detect distributed deadlocks, such as  :
  - **Global wait-for graph**: construct a global graph of resource dependencies from local graphs at each node, and check for cycles in the global graph.
  - **Edge chasing**: propagate probe messages along the edges of the local wait-for graphs, and detect cycles when a probe returns to its originator.
  - **Diffusing computation**: initiate a diffusing computation from each blocked process, and detect a deadlock when the computation terminates without finding a free resource.