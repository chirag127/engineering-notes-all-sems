### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks.

Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the preemption ceiling is raised to the ceiling of the locked resource.
4. When a task releases a resource, the preemption ceiling is lowered to the minimum of the ceilings of all resources locked by the task.
5. A task can be preempted only by a task with a priority higher than the current preemption ceiling.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and prevents priority inversion. It is commonly used in real-time systems to ensure that critical tasks are completed on time.