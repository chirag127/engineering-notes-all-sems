### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling to each resource based on the worst-case scenario, and does not change the ceiling during runtime.
- Dynamic preemption ceiling protocol assigns a variable ceiling to each resource based on the current situation, and updates the ceiling whenever a resource is locked or released.
- Dynamic preemption ceiling protocol has less overhead than static preemption ceiling protocol, but it requires more information about the system and the tasks.