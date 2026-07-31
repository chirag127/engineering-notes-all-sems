### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage shared resources and prevent priority inversion.

1. **Priority-Inheritance Protocol**: This protocol is used to temporarily raise the priority of a lower-priority task that is holding a shared resource, to the priority of the highest-priority task that is blocked and waiting for the resource. This prevents a medium-priority task from preempting the lower-priority task and causing priority inversion.

2. **Priority-Ceiling Protocol**: This protocol assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only lock a resource if its priority is higher than the priority ceiling of all resources currently locked by other tasks. This prevents priority inversion and also prevents deadlocks.

These protocols are important for ensuring the correct and timely execution of tasks in real-time systems that share resources. They help to prevent priority inversion, where a higher-priority task is blocked by a lower-priority task, and also prevent deadlocks, where two or more tasks are blocked waiting for each other to release resources.