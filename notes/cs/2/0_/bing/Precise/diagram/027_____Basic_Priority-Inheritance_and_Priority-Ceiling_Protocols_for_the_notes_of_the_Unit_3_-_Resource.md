### Basic Priority-Inheritance and Priority-Ceiling Protocols

#### Unit 3 - Resources Sharing in Real Time System

1. **Priority-Inheritance Protocol**: This protocol is used to solve the problem of priority inversion. When a high-priority task is blocked by a lower-priority task that holds a shared resource, the lower-priority task inherits the priority of the higher-priority task until it releases the resource. This ensures that the high-priority task can access the shared resource as soon as possible.

2. **Priority-Ceiling Protocol**: This protocol is an extension of the Priority-Inheritance Protocol. It assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. When a task acquires a shared resource, its priority is raised to the priority ceiling of the resource. This prevents lower-priority tasks from accessing the resource and causing priority inversion.

3. **Comparison**: The Priority-Ceiling Protocol is more effective in preventing priority inversion and reducing blocking time than the Priority-Inheritance Protocol. However, it requires more information about the system and the tasks, and may be more complex to implement.

4. **Implementation**: Both protocols can be implemented in the operating system or in the application code. The choice of implementation depends on the specific requirements of the system and the tasks.

5. **Applications**: These protocols are commonly used in real-time systems where tasks have strict timing constraints and shared resources must be accessed in a timely manner. They can help to improve the predictability and performance of the system.