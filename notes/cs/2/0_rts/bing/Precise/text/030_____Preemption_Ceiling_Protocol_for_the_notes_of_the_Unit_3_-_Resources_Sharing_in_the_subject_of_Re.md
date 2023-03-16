### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by lower priority tasks. Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling.
3. When a task locks a resource, the system's preemption ceiling is set to the maximum of the current preemption ceiling and the resource's preemption ceiling.
4. A task can be preempted only by tasks with a priority higher than the current preemption ceiling.
5. When a task releases a resource, the system's preemption ceiling is reset to the maximum preemption ceiling of all resources currently locked by tasks.

This protocol ensures that high priority tasks are not blocked by lower priority tasks and prevents priority inversion. It is important to note that the preemption ceiling must be carefully assigned to each shared resource to ensure the correct functioning of the protocol.