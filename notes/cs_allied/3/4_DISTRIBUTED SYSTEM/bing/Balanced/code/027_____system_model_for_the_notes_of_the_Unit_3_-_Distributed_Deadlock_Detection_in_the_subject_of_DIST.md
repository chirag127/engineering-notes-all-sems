### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process may request a resource, use it, and release it. A process may hold multiple resources at the same time.
- A process may block if it requests a resource that is not available. A process may also block if it waits for a message from another process.
- A deadlock occurs when a set of processes are blocked and none of them can make progress. A deadlock can be caused by circular waiting for resources or messages among the processes.
- A system model for distributed deadlock detection defines the following components:
  - The representation of the process-resource and process-message interactions, such as wait-for graphs or dependency matrices.
  - The algorithm for collecting and analyzing the global state of the system, such as edge chasing or global wait-for graph construction.
  - The strategy for resolving the deadlock, such as aborting or preempting some processes or resources.