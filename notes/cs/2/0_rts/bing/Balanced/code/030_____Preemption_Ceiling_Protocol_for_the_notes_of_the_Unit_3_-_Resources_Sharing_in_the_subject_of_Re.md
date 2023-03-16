### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems.
- It aims to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- It assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- There are two variants of preemption ceiling protocol: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Preemption ceiling protocol has some advantages over priority inheritance protocol, such as:
  - It prevents transitive blocking, where a low-priority task blocks a medium-priority task, which in turn blocks a high-priority task.
  - It prevents deadlock due to circular waiting, where two or more tasks wait for each other to release the resources they hold.
  - It reduces the number of context switches, since a task can lock multiple resources without being preempted.
  - It simplifies the analysis of the worst-case response time of tasks, since the blocking time is bounded by the ceiling priority of the resources.