### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems.
- It aims to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- It assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- This protocol ensures that a task can be blocked by at most one lower-priority task, and that a task can access a resource only if it is the highest-priority task in the system.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the system design.
- Dynamic preemption ceiling protocol assigns a variable ceiling priority to each resource based on the priority of the task that locks it.
- Static preemption ceiling protocol is simpler and faster, but dynamic preemption ceiling protocol is more flexible and can handle deadline-driven systems.