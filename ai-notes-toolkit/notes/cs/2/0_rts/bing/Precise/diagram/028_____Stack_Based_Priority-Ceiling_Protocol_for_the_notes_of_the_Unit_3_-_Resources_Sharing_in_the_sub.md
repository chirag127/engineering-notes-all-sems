### Stack Based Priority-Ceiling Protocol

Stack Based Priority-Ceiling Protocol is a resource sharing protocol used in real-time systems. It is used to prevent priority inversion, which occurs when a high priority task is blocked by a lower priority task that is holding a shared resource.

Here are some key points to note about the Stack Based Priority-Ceiling Protocol:

1. Each shared resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource.
2. A task can only lock a resource if its priority is higher than the priority ceilings of all resources currently locked by other tasks.
3. When a task locks a resource, its priority is temporarily raised to the priority ceiling of the resource.
4. When a task releases a resource, its priority is restored to its original value.

This protocol ensures that a high priority task will not be blocked by a lower priority task holding a shared resource for an extended period of time. It also prevents deadlocks by ensuring that tasks can only lock resources in a specific order.
