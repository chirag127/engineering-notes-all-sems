### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for others in a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better schedulability than static preemption ceiling protocol, but it requires more storage space and dynamic priority systems.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed priority scheduling technique that allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can reduce the number of context switches, increase the schedulability, and decrease the memory requirements of real-time systems.
- PTS can also enable a scalable real-time system design, especially for object-oriented systems that require synchronization considerations to maintain consistent object states.
- PTS can be combined with preemption ceiling protocol by using the ceiling priority of a resource as the preemption threshold of the task that locks the resource.