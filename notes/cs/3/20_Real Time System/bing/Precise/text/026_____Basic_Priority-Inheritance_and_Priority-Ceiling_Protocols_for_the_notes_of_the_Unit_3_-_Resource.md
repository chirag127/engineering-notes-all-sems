### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage resource sharing and prevent priority inversion.

1. **Priority-Inheritance Protocol**: This protocol is used to temporarily raise the priority of a low-priority task that is holding a shared resource needed by a higher-priority task. The low-priority task inherits the priority of the highest-priority task that is blocked, allowing it to complete its use of the shared resource and release it for the higher-priority task.

2. **Priority-Ceiling Protocol**: This protocol assigns a priority ceiling to each shared resource, which is the highest priority of any task that may access the resource. A task can only access a shared resource if its priority is higher than the current priority ceiling of all resources it currently holds or will hold in the future. This prevents lower-priority tasks from accessing resources needed by higher-priority tasks and prevents priority inversion.

These protocols are important for ensuring that high-priority tasks can access shared resources in a timely manner and that the system can meet its real-time requirements. They are commonly used in real-time operating systems and other systems where resource sharing and priority management are critical.