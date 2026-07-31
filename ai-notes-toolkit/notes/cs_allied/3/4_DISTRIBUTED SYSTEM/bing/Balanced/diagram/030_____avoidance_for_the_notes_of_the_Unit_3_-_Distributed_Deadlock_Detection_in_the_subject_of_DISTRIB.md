### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that tries to prevent a deadlock from occurring by ensuring that the system is always in a safe state.
- A safe state is one where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Deadlock avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- However, deadlock avoidance is impractical in distributed systems for several reasons, such as:
  - The system may not have complete or accurate information about the global state of resources and processes.
  - The system may not be able to predict the future resource requests and releases of each process, especially if they are dynamic or unpredictable.
  - The system may incur a high overhead of communication and synchronization to maintain and update the global state information.
  - The system may have to deny some resource requests even if they do not cause a deadlock, which may reduce the system performance and utilization.
- Therefore, deadlock detection is often preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that tries to discover a deadlock after it has occurred by examining the status of the process-resource interactions for the presence of a cyclic wait.
- Deadlock detection requires the system to collect and analyze the global wait-for graph, which is a variant of the resource allocation graph that shows which processes are waiting for which resources.
- Deadlock detection algorithms can be classified into four categories, based on how the global wait-for graph is constructed and analyzed:
  - Path-pushing algorithms: Each process maintains a set of paths in the wait-for graph that start from itself and end at some other process. The processes exchange these paths periodically to detect cycles.
  - Edge-chasing algorithms: Each process sends a probe message along the edges of the wait-for graph to detect cycles. The probe messages are forwarded or discarded by the processes based on some rules.
  - Diffusion computation algorithms: Each process initiates a computation to detect cycles in the wait-for graph. The computation involves sending and receiving messages among the processes until a termination condition is met.
  - Global state detection algorithms: Each process periodically records its local state and sends it to a coordinator process. The coordinator process constructs and analyzes the global wait-for graph based on the collected local states.