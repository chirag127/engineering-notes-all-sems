### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage the sharing of resources among tasks. These protocols are designed to prevent priority inversion, which occurs when a high-priority task is blocked by a lower-priority task that is holding a shared resource.

1. **Priority-Inheritance Protocol**: This protocol allows a lower-priority task that is holding a shared resource to temporarily inherit the priority of the highest-priority task that is blocked and waiting for the resource. This allows the lower-priority task to complete its use of the resource and release it, allowing the higher-priority task to proceed.

2. **Priority-Ceiling Protocol**: This protocol assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only access a shared resource if its priority is higher than the current priority ceiling of all resources it currently holds or will hold during its execution. This prevents lower-priority tasks from blocking higher-priority tasks and ensures that a task can only be blocked by tasks with a higher priority.

These protocols are used to ensure that high-priority tasks can access shared resources in a timely manner, preventing priority inversion and improving the predictability and performance of real-time systems. They are commonly used in systems with fixed-priority scheduling, where tasks are assigned priorities based on their importance and deadlines.