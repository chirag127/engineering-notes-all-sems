### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding a shared resource.

The key points of the Preemption Ceiling Protocol are:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system.
3. The preemption ceiling of the system is the maximum of the preemption ceilings of all resources currently locked by tasks.
4. A task can be preempted by a higher priority task only if the priority of the preempting task is higher than the preemption ceiling of the system.

This protocol ensures that a high priority task is never blocked by a lower priority task holding a shared resource. It also ensures that a task holding a shared resource is not preempted by a lower priority task, preventing priority inversion.