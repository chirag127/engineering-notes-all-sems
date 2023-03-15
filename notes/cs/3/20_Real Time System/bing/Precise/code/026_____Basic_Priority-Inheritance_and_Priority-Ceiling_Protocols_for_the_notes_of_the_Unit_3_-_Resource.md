### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage the sharing of resources among tasks. These protocols are designed to prevent priority inversion, which occurs when a high-priority task is blocked by a lower-priority task that is holding a shared resource.

1. **Priority-Inheritance Protocol**: This protocol allows a lower-priority task that is holding a shared resource to temporarily inherit the priority of the highest-priority task that is blocked and waiting for the resource. This allows the lower-priority task to complete its use of the resource and release it, allowing the higher-priority task to proceed.

2. **Priority-Ceiling Protocol**: This protocol assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only access a shared resource if its priority is higher than the current priority ceiling of all resources it currently holds or will hold during its execution. This prevents lower-priority tasks from blocking higher-priority tasks by holding shared resources.

These protocols are used to ensure that high-priority tasks can access shared resources in a timely manner, and to prevent priority inversion in real-time systems. They are commonly used in systems where tasks have strict timing requirements and must complete their execution within a specified time frame.