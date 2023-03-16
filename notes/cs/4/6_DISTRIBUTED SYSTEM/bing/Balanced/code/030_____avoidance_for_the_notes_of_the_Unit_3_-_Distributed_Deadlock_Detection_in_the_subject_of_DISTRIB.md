### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is one in which there exists a sequence of resource allocations that does not lead to a deadlock.
- Deadlock avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- However, deadlock avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among the nodes.
  - The uncertainty and unpredictability of resource requests and releases.
  - The possibility of communication failures and process crashes.
  - The high overhead and complexity of maintaining and checking the safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that identifies the existence of deadlocks after they have occurred and takes some actions to resolve them.
- Deadlock detection requires the system to collect and analyze the information about the process-resource interactions and look for cycles in the wait-for graph.
- Deadlock detection algorithms in distributed systems can be classified into four categories, based on the way they collect and propagate the information:
  - Path-pushing algorithms: Each node maintains a set of paths that represent the dependencies among the processes and resources. The paths are periodically exchanged among the nodes to detect cycles.
  - Edge-chasing algorithms: Each node sends a probe message along the edges of the wait-for graph to trace a cycle. If a probe returns to the sender, a deadlock is detected.
  - Diffusion computation algorithms: Each node initiates a computation to determine the local wait-for graph and propagates it to its neighbors. The computation terminates when the global wait-for graph is obtained and checked for cycles.
  - Global state detection algorithms: Each node periodically records its local state and sends it to a coordinator node. The coordinator node constructs a global state from the local states and checks it for consistency and cycles.