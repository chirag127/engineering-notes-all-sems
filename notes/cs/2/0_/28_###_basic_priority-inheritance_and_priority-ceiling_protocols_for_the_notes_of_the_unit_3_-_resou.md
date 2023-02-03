### Basic Priority-Inheritance and Priority-Ceiling Protocols for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

Priority-Inheritance Protocol (PIP):
- A synchronization protocol that ensures that a task holding a lock on a shared resource has the highest priority among all tasks waiting for that resource.
- Prevents priority inversion, where a low-priority task holds a resource needed by a high-priority task, causing the high-priority task to wait.
- When a task requests a resource, it inherits the priority of the highest-priority task waiting for that resource.
- The priority of the task is restored to its original value when it releases the resource.

Priority-Ceiling Protocol (PCP):
- A synchronization protocol that assigns a priority ceiling to each shared resource, which is the highest priority a task can have while holding that resource.
- Prevents priority inversion by ensuring that no task with a lower priority than the priority ceiling of a resource can access that resource.
- The priority ceiling of a resource is set to the priority of the highest-priority task that may need to access the resource.

Both protocols help ensure that high-priority tasks are not blocked by low-priority tasks, improving the real-time behavior of the system.
