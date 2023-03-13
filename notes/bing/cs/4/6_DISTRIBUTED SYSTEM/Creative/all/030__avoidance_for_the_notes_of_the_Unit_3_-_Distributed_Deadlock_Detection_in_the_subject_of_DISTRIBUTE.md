### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a strategy that tries to ensure that the system will always remain in a safe state, where no deadlock can occur.
- Deadlock avoidance requires some knowledge of the future resource requests and releases of the processes, which may not be available or accurate in a distributed system.
- Deadlock avoidance can be implemented using one of the following methods:
  - Resource allocation graph (RAG): A directed graph that represents the allocation and request of resources by processes. A cycle in the graph indicates a deadlock. RAG can only be used when each resource type has a single instance.
  - Banker's algorithm: A generalization of RAG that can handle multiple instances of each resource type. It simulates the allocation and request of resources by processes and checks if the system is in a safe state after each operation. A safe state is one where there exists a sequence of processes that can finish their execution without causing a deadlock.
  - Timestamp ordering: A method that assigns a timestamp to each resource request and release by processes. It ensures that the requests are granted in a consistent order across the system, avoiding circular waits. Timestamp ordering can be based on logical clocks or physical clocks.
- Deadlock avoidance has some advantages and disadvantages:
  - Advantages:
    - It can prevent deadlocks from occurring without imposing any restrictions on the processes.
    - It can allow more concurrency and flexibility than deadlock prevention.
  - Disadvantages:
    - It can be costly and complex to implement in a distributed system, especially when the resource information is dynamic and uncertain.
    - It can be conservative and inefficient, as it may deny some requests that are not actually leading to a deadlock.