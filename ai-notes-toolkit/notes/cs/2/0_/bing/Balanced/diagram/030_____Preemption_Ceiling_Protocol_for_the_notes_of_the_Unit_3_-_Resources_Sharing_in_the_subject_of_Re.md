### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems to avoid unbounded priority inversion and mutual deadlock.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better responsiveness than static preemption ceiling protocol, but it requires more memory and complex data structures.
- Preemption ceiling protocol can be combined with other scheduling techniques, such as preemption threshold scheduling, to achieve better performance and scalability.
- Preemption threshold scheduling assigns a threshold priority to each task, which is the lowest priority that can preempt the task.
- A task can be preempted only by another task whose priority is higher than both the current priority and the threshold priority of the preempted task.
- Preemption threshold scheduling reduces the number of context switches and the memory requirements, while preserving the schedulability of fixed-priority systems.
- Preemption threshold scheduling can be integrated with preemption ceiling protocol to handle synchronization of shared resources, by using the ceiling priority of the resource as the threshold priority of the task that locks the resource.
- This integration ensures that a task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks, and that it cannot be preempted by any other task until it releases the resource.
- This integration also avoids priority inversion and deadlock, and improves the response time and the schedulability of the system.