# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a shared resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the actual priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better schedulability than static preemption ceiling protocol, but it requires more memory and synchronization primitives.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- PTS can reduce the number of context switches and improve the performance of real-time systems, but it may also cause long priority inversion and deadlock.
- Preemption ceiling protocol can solve these problems by enforcing the ceiling priority of the resources as the preemption threshold of the tasks that lock them.
- Preemption ceiling protocol is suitable for object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Preemption ceiling protocol can avoid the inheritance anomaly, which is a situation where a task inherits multiple priorities from different objects and causes unpredictable behavior.