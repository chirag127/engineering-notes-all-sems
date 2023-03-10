### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

Preemption Ceiling Protocol (PCP) is a synchronization protocol that is used to avoid priority inversion in real-time systems. Priority inversion is a situation where a low-priority task holds a resource that a high-priority task requires, which causes the high-priority task to be blocked until the low-priority task releases the resource. 

PCP is implemented in the following way:

1. Each resource is assigned a preemption ceiling priority (PCP). The PCP is the highest priority of any task that can potentially lock the resource.
2. When a task requests a resource, its priority is raised to the PCP of the requested resource.
3. If the task already has a priority higher than the PCP, then its priority is not changed.
4. The task can lock the resource only if its current priority is higher than the priority of any other task holding the resource.
5. When the task releases the resource, its priority is restored to its original priority.

Advantages of PCP:

1. PCP ensures that high-priority tasks are not blocked by low-priority tasks holding resources.
2. It is easy to implement and has low overhead.
3. It is a widely used protocol in real-time systems.

Disadvantages of PCP:

1. PCP requires that the preemption ceiling priority of each resource be determined in advance. This can be difficult to do in complex systems.
2. PCP does not prevent deadlock.

Example of PCP:

Consider a system with three tasks: T1, T2, and T3, and two resources: R1 and R2. The preemption ceiling priority of R1 is set to the priority of T1, and the preemption ceiling priority of R2 is set to the priority of T2. If T1 requests R2, its priority is raised to the preemption ceiling priority of R2, which is higher than the priority of T2. T1 can then lock R2 and execute without being blocked by T2.

Applications of PCP:

1. PCP is used in real-time operating systems to prevent priority inversion.
2. PCP is used in embedded systems, where resources are shared among different tasks.
3. PCP is used in aerospace and defense systems, where real-time performance is critical.

In conclusion, Preemption Ceiling Protocol is a synchronization protocol that ensures high-priority tasks are not blocked by low-priority tasks holding resources. It is easy to implement and widely used in real-time systems. However, it requires that the preemption ceiling priority of each resource be determined in advance, which can be difficult in complex systems.