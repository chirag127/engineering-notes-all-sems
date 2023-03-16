### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol is a resource sharing protocol used in real-time systems.
- It is used to prevent priority inversion, which occurs when a high priority task is blocked by a lower priority task that is holding a shared resource.
- In this protocol, each shared resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource.
- A task can only lock a resource if its priority is higher than the priority ceiling of all resources currently locked by other tasks.
- When a task locks a resource, its priority is temporarily raised to the priority ceiling of the resource.
- This ensures that a high priority task will not be blocked by a lower priority task holding a shared resource, as the lower priority task's priority will be raised to prevent it from blocking the higher priority task.
- When the task releases the resource, its priority is restored to its original value.
- This protocol can prevent deadlocks and ensure that high priority tasks are not blocked by lower priority tasks holding shared resources.