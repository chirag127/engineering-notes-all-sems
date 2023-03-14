## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set .
- In distributed systems, a process may request resources in any order, which may not be known a priori, and a process can request a resource while holding others.
- If the allocation sequence of process resources is not controlled in such environments, deadlocks can occur .
- Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention is commonly achieved by either having a process acquire all the needed resources simultaneously before it begins execution or by pre-empting a process that holds the needed resource.
- Deadlock avoidance is the approach where a resource is granted to a process if the resulting global system is safe .
- Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition .
- To resolve the deadlock, we have to abort a deadlocked process.
- The techniques of deadlock detection in the distributed system require the following properties:
  - Progress – The method should be able to detect all the deadlocks in the system.
  - Safety – The method should not detect false or phantom deadlocks.
- There are three approaches to detect deadlocks in distributed systems . They are as follows:
  - Centralized approach – In the centralized approach, there is only one responsible resource to detect deadlock. The advantage of this approach is that it is simple and easy to implement, while the drawbacks include excessive workload at one node, single-point failure (that is the whole system is dependent on one node if that node fails the whole system crashes) which in turns makes the system less reliable.
  - Distributed approach – In the distributed approach different nodes work together to detect deadlocks. No single point failure (that is the whole system is dependent on one node if that node fails the whole system crashes) as the workload is equally divided among all nodes. The speed of deadlock detection also increases.
  - Hierarchical approach – This approach is the most advantageous. It is the combination of both centralized and distributed approaches of deadlock detection in a distributed system. In this approach, some selected nodes or clusters of nodes are responsible for deadlock detection and these selected nodes are controlled by a single node.