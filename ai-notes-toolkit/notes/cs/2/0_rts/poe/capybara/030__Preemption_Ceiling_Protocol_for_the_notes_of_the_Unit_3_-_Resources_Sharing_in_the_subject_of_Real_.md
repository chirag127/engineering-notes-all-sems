### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

The Preemption Ceiling Protocol is used in real-time systems to prevent deadlocks and priority inversion. Here are some important points to understand this protocol:

- The Preemption Ceiling Protocol is a mutual exclusion protocol that allows a task to execute without interruption by a lower priority task.

- The protocol determines a ceiling priority level for each resource. A task can only access a resource if its priority level is higher than the ceiling level of the resource.

- The ceiling priority level of a resource is the highest priority level of any task that may need to access it.

- When a task acquires a resource, it is elevated to the ceiling priority level of the resource. This ensures that no lower priority task can pre-empt the task that holds the resource.

- If a task tries to access a resource that is held by a higher priority task, it will be blocked until the resource becomes available.

- The Preemption Ceiling Protocol is effective in preventing priority inversion. Priority inversion occurs when a low priority task holds a resource that is required by a high priority task. The high priority task cannot execute until the low priority task releases the resource.

- The protocol guarantees that a task will not be blocked indefinitely due to a resource held by a lower priority task.

- The Preemption Ceiling Protocol requires that the priority of each task be fixed at the time of creation. This ensures that the ceiling priority level of a resource can be determined before any task tries to access it.

- The protocol can be implemented using hardware, software, or a combination of both.

- The Preemption Ceiling Protocol is widely used in real-time systems, especially in systems with a large number of tasks and resources.

- The protocol is an important tool for ensuring the timely and predictable execution of real-time systems. It helps to prevent deadlocks, priority inversion, and other problems that can occur when multiple tasks share resources.