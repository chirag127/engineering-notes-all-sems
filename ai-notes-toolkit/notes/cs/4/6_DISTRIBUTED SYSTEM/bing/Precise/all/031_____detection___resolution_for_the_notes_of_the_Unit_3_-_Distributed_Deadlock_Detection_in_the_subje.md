# Detection & Resolution

In the context of distributed systems, deadlock detection and resolution are important concepts to understand. Here are some key points to consider:

1. **Distributed Deadlock Detection**: In a distributed system, a deadlock can occur when two or more processes are waiting for resources held by each other. Detecting deadlocks in a distributed system can be more challenging than in a centralized system, as there is no single point of control.

2. **Detection Algorithms**: There are several algorithms that can be used to detect deadlocks in a distributed system. These include the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.

3. **Resolution**: Once a deadlock has been detected, it must be resolved in order to allow the system to continue functioning. This can be done by aborting one or more of the processes involved in the deadlock, or by preempting resources from one process and allocating them to another.

4. **Prevention**: In addition to detecting and resolving deadlocks, it is also possible to prevent them from occurring in the first place. This can be done by using techniques such as resource ordering, or by implementing a timeout mechanism to prevent processes from waiting indefinitely for resources.

These are some of the key concepts to understand when studying distributed deadlock detection and resolution. It is important to have a thorough understanding of these concepts in order to effectively design and implement distributed systems.