# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- There are two variants of preemption ceiling protocol: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that requests the resource.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed-priority scheduling scheme that allows a task to specify a preemption threshold, below which it cannot be preempted by higher-priority tasks.
- PTS can reduce the number of context switches, increase the schedulability, and decrease the memory requirements of real-time systems.
- However, PTS may lead to long priority inversion if not combined with a synchronization protocol, such as preemption ceiling protocol.
- Preemption ceiling protocol can also be extended to support object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Dual ceiling protocol is an example of such an extension, which assigns two ceiling priorities to each object: one for read operations and one for write operations.
