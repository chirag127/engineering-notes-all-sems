### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of **processors** that are connected by a **communication network**. The communication delay is finite but unpredictable.
- A processor can execute one or more **processes** that can request, use, and release **resources**. A resource can be local to a processor or shared by multiple processors.
- A process can request a resource in any order, which may not be known a priori, and can request a resource while holding others. If the allocation sequence of process resources is not controlled, **deadlocks** can occur.
- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed.
- Deadlocks can be dealt with using any one of the following three strategies: **deadlock prevention**, **deadlock avoidance**, and **deadlock detection** .
- Deadlock prevention is commonly achieved by either having a process acquire all the needed resources simultaneously before it begins execution or by pre-empting a process that holds the needed resource.
- Deadlock avoidance is the approach where a resource is granted to a process if the resulting global system is safe, that is, there is no possibility of a deadlock.
- Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition. To resolve the deadlock, we have to abort a deadlocked process.
- There are three approaches to detect deadlocks in distributed systems: **centralized approach**, **distributed approach**, and **hierarchical approach** .
- In the centralized approach, there is only one responsible node to detect deadlock. The advantage of this approach is that it is simple and easy to implement, while the drawbacks include excessive workload at one node, single-point failure, and less reliability.
- In the distributed approach, different nodes work together to detect deadlocks. The advantage of this approach is that it avoids single-point failure and increases the speed of deadlock detection, while the drawbacks include higher communication overhead and complexity.
- In the hierarchical approach, some selected nodes or clusters of nodes are responsible for deadlock detection and these selected nodes are controlled by a single node. The advantage of this approach is that it combines the benefits of both centralized and distributed approaches, while the drawback is that it requires a hierarchical structure of nodes .