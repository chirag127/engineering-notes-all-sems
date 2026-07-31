### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- When a task locks a resource, it raises its own priority to the ceiling priority of that resource, and it cannot be preempted by any other task with a lower priority.
- When a task unlocks a resource, it restores its own priority to its original value, and it may be preempted by any other task with a higher priority.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower priority task, and that deadlock is impossible because a task can lock a resource only if its priority is higher than the ceiling priority of any locked resource.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
  - Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the worst-case scenario, and it does not change during the execution.
  - Dynamic preemption ceiling protocol assigns a variable ceiling priority to each resource based on the current situation, and it changes during the execution.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling, to provide more benefits for real-time systems, such as increased schedulability, reduced context switches, and decreased memory requirements.