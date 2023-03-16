### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage shared resources and prevent priority inversion.

1. **Priority-Inheritance Protocol**: This protocol is used to prevent priority inversion by temporarily raising the priority of a lower-priority task that holds a shared resource to the priority of the highest-priority task that is blocked and waiting for the resource. This ensures that the lower-priority task can complete its use of the shared resource and release it for the higher-priority task.

2. **Priority-Ceiling Protocol**: This protocol is used to prevent priority inversion, deadlocks, and unbounded priority inversion. It assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only lock a resource if its priority is higher than the current priority ceiling of all resources it currently holds or is attempting to lock.

These protocols are important for ensuring the correct and timely execution of tasks in real-time systems that share resources. They help to prevent situations where a higher-priority task is blocked by a lower-priority task, which can cause missed deadlines and other issues.