### Unit 3 - Distributed Deadlock Detection
#### Deadlock Prevention

Deadlock prevention is a technique used in distributed systems to ensure that deadlocks do not occur. Here are some methods for deadlock prevention:

1. **Resource ordering**: Resources are assigned a unique number and processes can only request resources in increasing order of their assigned numbers. This prevents circular wait, one of the necessary conditions for deadlock.

2. **Resource allocation denial**: A process is denied its resource request if granting the request could potentially lead to a deadlock. This requires the system to have knowledge of the current resource allocation state and the future requests of processes.

3. **Preemption**: Resources are forcibly taken away from a process if it is determined that a deadlock could occur. The process is then restarted with its resource requests.

4. **Concurrency control**: The number of processes that can access a resource at the same time is limited. This can prevent deadlocks by ensuring that resources are not over-allocated.

These are some of the methods used for deadlock prevention in distributed systems. It is important to note that these methods may not always be effective and may have their own drawbacks, such as reduced system performance or increased complexity. Therefore, it is important to carefully evaluate the trade-offs when implementing deadlock prevention techniques.