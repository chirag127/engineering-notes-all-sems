# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access the resource .
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks .
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of the resource, and it cannot be preempted by any other task until it releases the resource .
- Preemption ceiling protocol guarantees that a task can be blocked by at most one lower-priority task, and that deadlock is impossible .
- Preemption ceiling protocol can be applied to both static-priority and dynamic-priority systems, such as rate-monotonic and earliest-deadline-first scheduling .
- Preemption ceiling protocol can be implemented in two ways: original ceiling protocol (OCP) and immediate ceiling protocol (ICP).
  - OCP raises the priority of a task only when it is blocked by a lower-priority task that holds a resource.
  - ICP raises the priority of a task as soon as it locks a resource, regardless of whether it is blocked or not.
  - ICP has better performance than OCP in terms of response time, blocking time, and context switches.
- Preemption ceiling protocol can be extended to support nested resources, multiple resources, and inheritance relations among resources .
- Preemption ceiling protocol can also be combined with other techniques, such as preemption threshold scheduling (PTS), to achieve better scalability and flexibility for real-time systems .
  - PTS allows a task to specify a preemption threshold, which is the lowest priority level at which it can be preempted.
  - PTS reduces the number of preemptions and context switches, and improves the schedulability of fixed-priority systems.
  - PTS can be integrated with preemption ceiling protocol to handle synchronization issues among tasks that share resources .
  - PTS can also be adapted to dynamic-priority systems, such as deadline-driven systems, by using fixed preemption levels.