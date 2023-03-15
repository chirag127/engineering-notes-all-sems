# Preemption Ceiling Protocol

Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion and ensure that high priority tasks are not blocked by low priority tasks holding shared resources.

Here are some key points to note about the Preemption Ceiling Protocol:

1. Each shared resource is assigned a preemption ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the current preemption ceiling of the system, which is the maximum of the preemption ceilings of all resources currently locked by other tasks.
3. When a task locks a resource, the system's preemption ceiling is raised to the preemption ceiling of the resource.
4. A task can be preempted only by tasks with a priority higher than the current preemption ceiling of the system.
5. When a task releases a resource, the system's preemption ceiling is lowered to the maximum of the preemption ceilings of all resources still locked by other tasks.

This protocol ensures that high priority tasks are not blocked by low priority tasks holding shared resources, and also prevents unbounded priority inversion. It is commonly used in real-time systems to ensure timely execution of high priority tasks.