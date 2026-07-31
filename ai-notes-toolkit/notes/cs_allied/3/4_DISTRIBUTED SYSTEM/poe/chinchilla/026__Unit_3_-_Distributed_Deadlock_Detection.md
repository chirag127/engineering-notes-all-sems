## Unit 3 - Distributed Deadlock Detection

In a distributed system, deadlock detection is a crucial aspect of ensuring the overall system's stability and reliability. Deadlocks can occur in distributed systems when multiple processes or nodes compete for shared resources and end up blocking each other. In this unit, we will learn about distributed deadlock detection and the various algorithms used to detect deadlocks in a distributed system.

### 1. Introduction to Distributed Deadlock Detection

- Deadlocks in distributed systems occur when multiple nodes compete for shared resources and end up blocking each other.
- Distributed deadlock detection is the process of identifying deadlocks in a distributed system and taking appropriate actions to resolve them.
- It involves detecting cycles in the resource allocation graph, which represent potential deadlocks, and taking corrective actions to prevent actual deadlocks from occurring.

### 2. Resource Allocation Graph

- In a distributed system, a resource allocation graph is used to represent the allocation of resources to processes or nodes.
- Nodes in the graph represent processes, and edges represent resource requests and allocations.
- The resource allocation graph can be used to detect potential deadlocks by looking for cycles in the graph.

### 3. Distributed Deadlock Detection Algorithms

- There are two main approaches to distributed deadlock detection: centralized and distributed.
- Centralized deadlock detection involves a single node or process monitoring the entire system and detecting deadlocks centrally.
- Distributed deadlock detection involves each node or process monitoring its local state and exchanging information with other nodes to detect deadlocks collaboratively.

#### 3.1 Centralized Deadlock Detection

- In centralized deadlock detection, a single node or process is responsible for monitoring the entire system and detecting deadlocks centrally.
- The central node maintains a global resource allocation graph and periodically checks for cycles in the graph.
- If a cycle is detected, the central node takes appropriate actions to resolve the deadlock.

#### 3.2 Distributed Deadlock Detection

- In distributed deadlock detection, each node or process monitors its local state and exchanges information with other nodes to detect deadlocks collaboratively.
- Each node maintains a local resource allocation graph and periodically exchanges information with other nodes to build a global resource allocation graph.
- If a cycle is detected in the global resource allocation graph, the nodes involved in the cycle can work together to resolve the deadlock.

### 4. Conclusion

- Distributed deadlock detection is a crucial aspect of ensuring the stability and reliability of a distributed system.
- Resource allocation graphs can be used to detect potential deadlocks in a distributed system.
- Centralized and distributed deadlock detection are two main approaches used to detect deadlocks in a distributed system.