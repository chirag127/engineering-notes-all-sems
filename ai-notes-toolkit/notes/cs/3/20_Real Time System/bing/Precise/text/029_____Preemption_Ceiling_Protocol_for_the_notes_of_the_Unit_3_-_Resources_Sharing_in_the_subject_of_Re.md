### Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding shared resources.

Here are some key points to remember about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may lock the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system.
3. The preemption ceiling of the system is the maximum of the preemption ceilings of all resources currently locked by tasks.
4. When a task locks a resource, it raises the preemption ceiling of the system to the preemption ceiling of the resource.
5. When a task releases a resource, it lowers the preemption ceiling of the system to the maximum of the preemption ceilings of all resources still locked by tasks.
6. A task can be preempted only by tasks with priorities higher than the current preemption ceiling of the system.

This protocol ensures that high priority tasks are not blocked by low priority tasks holding shared resources, and it also prevents unbounded priority inversion. It is commonly used in real-time systems to ensure that high priority tasks can meet their deadlines.