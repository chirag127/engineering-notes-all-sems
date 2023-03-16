### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that at least one of the necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) is never satisfied. For example, by using timeouts, ordering resources, or aborting transactions.
  - Avoidance: This approach tries to ensure that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that will not lead to deadlock. For example, by using the banker's algorithm or timestamps.
  - Detection: This approach tries to identify the existence of deadlocks after they occur, and then resolve them by breaking the circular wait. For example, by constructing a global wait-for graph or using edge chasing algorithms.
- The techniques of deadlock detection in distributed systems require the following properties:
  - Progress: The method should be able to detect all the deadlocks in the system.
  - Safety: The method should not detect false or phantom deadlocks.
- There are two main types of distributed deadlocks:
  - Communication deadlocks: These occur when processes are waiting for messages from each other, and no message can be delivered. For example, by using synchronous message passing or circular buffer queues.
  - Resource deadlocks: These occur when processes are waiting for resources held by other processes, and no resource can be released. For example, by using distributed mutual exclusion or distributed locking.