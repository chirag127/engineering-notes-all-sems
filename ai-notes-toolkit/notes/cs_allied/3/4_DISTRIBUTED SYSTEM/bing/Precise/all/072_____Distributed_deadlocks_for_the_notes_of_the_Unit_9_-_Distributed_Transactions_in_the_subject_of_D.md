# Distributed Deadlocks

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector.

In distributed systems, there are two main categories of deadlocks: Resource Deadlock and Communication Deadlock.

- **Resource Deadlock**: Resource deadlock refers to the deadlock state when the resource required by the first process is locked by the second one and the resource required by the second process is locked by the first process.

- **Communication Deadlock**: Communication deadlock refers to the deadlock state when two or more processes are blocked and waiting for messages from each other.

Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.

- **Deadlock Prevention**: Deadlock prevention is a strategy that ensures that at least one of the necessary conditions for deadlock does not hold. This can be achieved by imposing constraints on resource allocation.

- **Deadlock Avoidance**: Deadlock avoidance is a strategy that ensures that the system never enters a deadlock state. This can be achieved by careful resource allocation and by maintaining information about the current allocation of resources and the future requests of processes.

- **Deadlock Detection**: Deadlock detection is a strategy that allows the system to enter a deadlock state, detects the deadlock, and then takes action to recover from the deadlock.

In the distributed approach, different nodes work together to detect deadlocks. There is no single point of failure as the workload is equally divided among all nodes.