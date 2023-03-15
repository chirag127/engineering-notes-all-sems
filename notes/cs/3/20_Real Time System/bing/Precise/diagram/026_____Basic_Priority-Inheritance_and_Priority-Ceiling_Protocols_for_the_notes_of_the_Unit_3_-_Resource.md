### Basic Priority-Inheritance and Priority-Ceiling Protocols

#### Unit 3 - Resources Sharing in Real Time System

1. **Priority-Inheritance Protocol**: This protocol is used to solve the problem of priority inversion in real-time systems. When a high-priority task is blocked by a lower-priority task that is holding a shared resource, the priority of the lower-priority task is temporarily raised to that of the high-priority task. This allows the lower-priority task to complete its use of the shared resource and release it, allowing the high-priority task to continue.

2. **Priority-Ceiling Protocol**: This protocol is an extension of the priority-inheritance protocol. It assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. When a task acquires a shared resource, its priority is raised to the priority ceiling of the resource. This prevents lower-priority tasks from accessing the resource and causing priority inversion.

3. **Comparison**: The priority-ceiling protocol has the advantage of preventing deadlocks, while the priority-inheritance protocol does not. However, the priority-ceiling protocol can result in longer blocking times for lower-priority tasks.

4. **Usage**: Both protocols are commonly used in real-time systems to manage access to shared resources and prevent priority inversion. The choice of protocol depends on the specific requirements of the system and the trade-offs between preventing deadlocks and minimizing blocking times.