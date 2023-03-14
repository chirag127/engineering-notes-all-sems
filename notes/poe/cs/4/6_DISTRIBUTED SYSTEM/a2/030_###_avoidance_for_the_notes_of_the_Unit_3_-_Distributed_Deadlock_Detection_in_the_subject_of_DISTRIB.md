 Here is the content in markdown format for the topic ### avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM:

### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock detection algorithms detect the occurrence of a deadlock. Deadlock avoidance algorithms try to prevent deadlocks from occurring.
- In distributed systems, deadlocks can occur due to resource allocation across multiple nodes. To avoid deadlocks, we can use following methods:
- Safety algorithm: Ensure that requests for resources are granted only if they do not violate safety constraints that guarantee freedom from deadlock. E.g. Resource allocation graph (RAG) must remain acyclic.
- Resource ordering: Impose a total ordering on resource types and require that resources be requested in the non-decreasing order of this ordering. This ensures that circular wait conditions cannot occur.
- Limiting resource demands: Require that processes request resources in bounded quantities, thereby limiting resource demands and making the state space finite. This enables the use of deadlock avoidance techniques like the Banker's algorithm that work for finite state systems.
- Advantage: Deadlocks can be prevented if the avoidance algorithm is correctly implemented.
- Disadvantage: There can be decreased system utilization as the algorithm may unnecessarily restrict allocation. It can be complex to implement for distributed systems with multiple resource types and processes.

[Detailed diagrams and examples can be included here if required to understand the concepts better.]

Hope this helps!