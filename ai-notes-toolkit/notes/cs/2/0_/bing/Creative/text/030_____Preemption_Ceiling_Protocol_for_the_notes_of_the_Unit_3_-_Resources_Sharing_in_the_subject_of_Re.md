### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its current priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower priority task, and that the blocking time is bounded by the worst-case execution time of the critical section of the lower priority task.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
  - Static preemption ceiling protocol assigns a fixed ceiling priority to each resource based on the system design, and does not change it at run time.
  - Dynamic preemption ceiling protocol assigns a ceiling priority to each resource based on the current priority of the task that locks it, and updates it whenever the resource is locked or released.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed priority scheduling technique that allows a task to specify a preemption threshold, below which it cannot be preempted.
  - PTS can improve the schedulability, reduce the context switches, and decrease the memory requirements of real-time systems.
  - PTS can also enable a scalable real-time system design, especially for object-oriented systems that require synchronization considerations to maintain consistent object states.
  - PTS can be combined with preemption ceiling protocol to avoid long priority inversion and deadlock, while preserving the benefits of PTS.