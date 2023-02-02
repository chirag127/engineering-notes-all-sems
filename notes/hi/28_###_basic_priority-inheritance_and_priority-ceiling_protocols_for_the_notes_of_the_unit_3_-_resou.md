### Basic Priority-Inheritance and Priority-Ceiling Protocols for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System
Priority-Inheritance Protocol:
- A synchronization protocol that ensures a task with a higher priority will not be blocked by a lower priority task.
- When a lower priority task acquires a resource, it temporarily inherits the priority of the highest priority task waiting for that resource.
- This ensures that the higher priority task will be able to execute as soon as the resource becomes available.
- The lower priority task returns to its original priority once it releases the resource.

Priority-Ceiling Protocol:
- A synchronization protocol that assigns a ceiling priority to each resource.
- When a task acquires a resource, it temporarily inherits the ceiling priority of that resource.
- This ensures that the task with the highest priority waiting for the resource will be able to execute as soon as the resource becomes available.
- The task returns to its original priority once it releases the resource.
