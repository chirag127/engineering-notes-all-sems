# Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access the resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of the resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the worst-case scenario, and does not change it during execution.
- Dynamic preemption ceiling protocol assigns a variable ceiling priority to each resource based on the current situation, and updates it whenever a resource is locked or released.
- Dynamic preemption ceiling protocol has less blocking time and higher schedulability than static preemption ceiling protocol, but it requires more storage and computation overhead.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed-priority scheduling technique that allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can improve the performance of real-time systems by reducing context switches, memory requirements, and response times.
- However, PTS may cause long priority inversion if not combined with a synchronization protocol, since a low-priority task holding a resource may not be preempted by a high-priority task that needs the resource.
- Preemption ceiling protocol can solve this problem by raising the priority of the low-priority task to the ceiling priority of the resource, and allowing the high-priority task to preempt it.
- Preemption ceiling protocol can also prevent deadlock in PTS systems, since a task cannot lock a resource if its priority is lower than the ceiling priority of any resource locked by another task.
- Preemption ceiling protocol and PTS can work together to provide a scalable and efficient real-time system design.