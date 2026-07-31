# Basic Priority-Inheritance and Priority-Ceiling Protocols

## Unit 3 - Resources Sharing in Real Time System

- **Priority-Inheritance Protocol**: This protocol is used to solve the problem of priority inversion. When a high-priority task is blocked by a lower-priority task, the lower-priority task inherits the priority of the higher-priority task. This allows the lower-priority task to complete its critical section and release the shared resource, allowing the higher-priority task to continue.

- **Priority-Ceiling Protocol**: This protocol is an extension of the priority-inheritance protocol. Each shared resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource. When a task accesses a shared resource, its priority is raised to the priority ceiling of the resource. This prevents lower-priority tasks from accessing the resource and causing priority inversion.

- Both protocols are used to prevent priority inversion and ensure that high-priority tasks are not blocked by lower-priority tasks for an extended period of time.

- These protocols are commonly used in real-time systems where tasks have strict timing constraints and shared resources must be accessed in a timely manner.

- Priority-inheritance and priority-ceiling protocols can help improve the predictability and performance of real-time systems by reducing the impact of priority inversion. However, they can also increase the complexity of the system and may require additional overhead to implement. It is important to carefully evaluate the trade-offs when deciding whether to use these protocols in a real-time system.