## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized.
- Deadlock detection is one of the strategies to deal with deadlocks, where the system periodically checks for the existence of deadlocks and resolves them by aborting one or more processes.
- Deadlock detection in distributed systems entails two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Detection of existing deadlocks requires examining the status of process-resource interactions for the presence of cyclic wait.
- Resolution of detected deadlocks requires choosing a suitable victim process to abort and recover the resources.
- Deadlock detection in distributed systems can be performed using either a centralized or a distributed approach.
- In the centralized approach, a designated node (called the deadlock detector) collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect cycles.
- In the distributed approach, a distributed algorithm (such as edge chasing) is used to propagate probe messages along the wait-for edges and detect cycles.
- The advantages of the centralized approach are simplicity and efficiency, while the disadvantages are single point of failure and communication overhead.
- The advantages of the distributed approach are fault tolerance and scalability, while the disadvantages are complexity and message overhead.