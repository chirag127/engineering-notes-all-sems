### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks are similar to deadlocks in centralized systems, but they are harder to detect, avoid, and prevent, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are different types of distributed deadlocks, depending on the nature of the resources or messages involved. Some examples are:
  - Communication deadlocks: occur when processes are waiting for messages from each other that will never arrive.
  - Distributed mutual exclusion deadlocks: occur when processes are competing for exclusive access to shared resources in a distributed system.
  - Distributed transaction deadlocks: occur when transactions are waiting for locks on data items that are held by other transactions in a distributed database system.
- There are different approaches to handle distributed deadlocks, such as :
  - Prevention: use a protocol that ensures that deadlocks cannot occur, such as ordering the resources or messages, or using timeouts or timestamps.
  - Avoidance: use a protocol that avoids unsafe resource allocation or message passing, such as the banker's algorithm or the wound-wait scheme.
  - Detection: use a technique that detects the existence of deadlocks in the system, and then resolve them by aborting or restarting some processes or transactions.
  - Ignorance: ignore the possibility of deadlocks, and assume that they are rare or negligible, and rely on the user or the application to handle them.
- The techniques of deadlock detection in distributed systems require the following properties:
  - Progress: the technique should be able to detect all the deadlocks in the system.
  - Safety: the technique should not detect false or phantom deadlocks, which are not actually present in the system.
- There are two main categories of deadlock detection techniques in distributed systems :
  - Centralized: use a single node or a coordinator to collect information from all the nodes in the system, and construct a global wait-for graph (WFG) to identify cycles that indicate deadlocks.
  - Distributed: use multiple nodes or agents to cooperate and exchange information with each other, and use a distributed algorithm to identify cycles that indicate deadlocks, such as edge chasing or probe propagation.