### Distributed Deadlocks

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector.

In distributed systems, there are two main categories of deadlocks: Resource Deadlock and Communication Deadlock. Resource deadlock refers to the deadlock state when the resource required by the first process is locked by the second one and the resource required by the second process is locked by the first process.

Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection. In the distributed approach, different nodes work together to detect deadlocks. No single point failure (that is the whole system is dependent on one node if that node fails the whole system crashes) as the workload is equally divided among all nodes.