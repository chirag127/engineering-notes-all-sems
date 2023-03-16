### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks. Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the preemption ceiling is raised to the ceiling of the locked resource.
4. When a task releases a resource, the preemption ceiling is lowered to the highest ceiling of all resources still locked by the task.
5. A task can be preempted only by tasks with priorities higher than the current preemption ceiling.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and that priority inversion is avoided. It is an effective way to manage resource sharing in real-time systems.