# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- There are two variants of preemption ceiling protocol: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Preemption ceiling protocol has several advantages over priority inheritance protocol, such as:
  - It prevents deadlock and chain blocking by enforcing a partial order on resource locking.
  - It reduces the number of context switches and memory requirements by limiting preemption.
  - It simplifies the analysis of schedulability and response time by bounding the blocking time of each task.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS) and deadline-driven scheduling (DDS).
- Preemption threshold scheduling assigns a preemption threshold to each task, which is the lowest priority level at which the task can be preempted.
- Deadline-driven scheduling assigns the priority of each task based on its deadline, which can be fixed or dynamic.
- Preemption ceiling protocol can be combined with these schemes to provide better synchronization and performance for real-time systems .