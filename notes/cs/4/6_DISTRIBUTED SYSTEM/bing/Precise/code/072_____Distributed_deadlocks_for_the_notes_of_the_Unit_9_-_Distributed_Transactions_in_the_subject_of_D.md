### Distributed Deadlocks

- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector .
- In the distributed approach, different nodes work together to detect deadlocks. There is no single point failure as the workload is equally divided among all nodes .
- In distributed systems, there are two main categories of deadlocks: Resource Deadlock and Communication Deadlock .
- Resource deadlock refers to the deadlock state when the resource required by the first process is locked by the second one and the resource required by the second process is locked by the first process .
- A deadlock can be defined as a condition where a set of processes request resources that are held by other processes in the set .
- Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection .
