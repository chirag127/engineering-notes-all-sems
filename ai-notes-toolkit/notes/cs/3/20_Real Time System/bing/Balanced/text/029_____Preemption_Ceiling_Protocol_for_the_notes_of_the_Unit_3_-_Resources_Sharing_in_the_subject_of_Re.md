### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by other tasks in a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has less blocking time than static preemption ceiling protocol, but it requires more storage and computation overhead.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- Preemption threshold scheduling can reduce the number of context switches and increase the schedulability of real-time systems, but it may also cause long priority inversion.
- Preemption ceiling protocol can avoid long priority inversion by ensuring that a task can lock a resource only if its priority is higher than the preemption threshold of any task that can access that resource.
- Preemption ceiling protocol can also be applied to object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Preemption ceiling protocol can ensure that a task can invoke a method of an object only if its priority is higher than the ceiling priority of the object, which is the highest priority of any task that can invoke any method of the object.