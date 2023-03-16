### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks can access shared resources without being blocked by lower priority tasks.

Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can lock a resource only if its priority is higher than the current preemption ceiling of the system.
3. The system preemption ceiling is the maximum of the preemption ceilings of all resources currently locked by tasks.
4. When a task locks a resource, it raises the system preemption ceiling to the preemption ceiling of the resource.
5. When a task releases a resource, it lowers the system preemption ceiling to the maximum of the preemption ceilings of all resources still locked by tasks.
6. A task can be preempted only by tasks with priorities higher than the current system preemption ceiling.

This protocol ensures that high priority tasks can access shared resources without being blocked by lower priority tasks, and it prevents priority inversion by ensuring that lower priority tasks cannot lock resources needed by higher priority tasks. It also ensures that tasks are scheduled in priority order, with the highest priority task always running, except when it is blocked waiting for a shared resource. This makes the protocol suitable for use in real-time systems, where predictable and timely access to shared resources is essential.