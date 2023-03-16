### Unit 3 - Distributed Deadlock Detection: Deadlock Prevention

Deadlock prevention is a technique used in distributed systems to ensure that deadlocks do not occur. Here are some methods for deadlock prevention:

1. **Resource allocation**: One way to prevent deadlocks is to ensure that resources are allocated in a way that prevents circular waiting. This can be done by imposing a total ordering on the resources and ensuring that processes request resources in increasing order.

2. **Hold and wait**: Another way to prevent deadlocks is to ensure that processes do not hold resources while waiting for other resources. This can be done by requiring processes to release all their resources before requesting new ones.

3. **Preemption**: Preemption is another technique that can be used to prevent deadlocks. This involves taking resources away from a process if it is determined that the process is involved in a potential deadlock.

4. **No Mutual Exclusion**: Deadlocks can also be prevented by ensuring that there is no mutual exclusion on resources. This can be done by allowing multiple processes to access the same resource simultaneously.

These are some of the methods that can be used to prevent deadlocks in distributed systems. It is important to note that these methods may not always be practical or effective, and other techniques may be needed to ensure that deadlocks do not occur.