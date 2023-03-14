### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- In distributed systems, a deadlock can occur when processes request resources in any order, which may not be known a priori, and a process can request a resource while holding others.
- Deadlocks can be handled using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention is achieved by either having a process acquire all the needed resources simultaneously before it begins execution or by pre-empting a process that holds the needed resource.
- Deadlock avoidance is achieved by granting a resource to a process if the resulting global system is safe.
- Deadlock detection is achieved by examining the status of the process–resources interaction for the presence of a deadlock condition.
- To resolve a deadlock, we have to abort a deadlocked process.
- Deadlock detection in distributed systems requires the following properties:
  - Progress: The method should be able to detect all the deadlocks in the system.
  - Safety: The method should not detect false or phantom deadlocks.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: There is only one responsible node to detect deadlock. The advantage of this approach is that it is simple and easy to implement, while the drawbacks include excessive workload at one node, single-point failure, and less reliability.
  - Distributed approach: Different nodes work together to detect deadlocks. The advantage of this approach is that there is no single point failure and the speed of deadlock detection increases, while the drawbacks include more complexity and communication overhead.
  - Hierarchical approach: This approach is a combination of both centralized and distributed approaches. Some selected nodes or clusters of nodes are responsible for deadlock detection and these selected nodes are controlled by a single node. The advantage of this approach is that it balances the workload and reliability, while the drawback is that it may introduce additional delays.