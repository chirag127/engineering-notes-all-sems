### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access the resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of the resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that no circular waiting can occur among tasks.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the system design, and does not change it at run time.
- Dynamic preemption ceiling protocol assigns a ceiling priority to each resource based on the priority of the task that currently locks the resource, and updates it whenever the resource is locked or released.
- Dynamic preemption ceiling protocol has lower overhead than static preemption ceiling protocol, but it requires that the system is a fixed preemption-level system, which means that the priority of a task does not change during its execution.
- Preemption ceiling protocol can be integrated with other scheduling algorithms, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- Preemption threshold scheduling can improve the schedulability, reduce the context switches, and decrease the memory requirements of fixed priority systems, but it may also cause long priority inversion if not combined with a synchronization protocol.
- Preemption ceiling protocol can also be extended to handle multiple resources and nested critical sections, such as the dual ceiling protocol.