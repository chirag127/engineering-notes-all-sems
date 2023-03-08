### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

The Preemption Ceiling Protocol is a synchronization protocol that is used in real-time systems to ensure that a task cannot be preempted by another task while it is in a critical section. This protocol is designed to prevent priority inversion, which occurs when a low-priority task holds a resource that a high-priority task needs, causing the high-priority task to be blocked.

The following are the key points to understand about the Preemption Ceiling Protocol:

- The protocol assigns a priority ceiling to each resource in the system, which is the highest priority of any task that may need to access the resource. For example, if a resource is needed by a high-priority task, then the priority ceiling of the resource is set to the priority of the high-priority task.
- When a task attempts to acquire a resource, its priority is temporarily raised to the priority ceiling of the resource. This ensures that no other task can preempt it while it holds the resource.
- If a task attempts to acquire a resource that is already held by another task, then the protocol checks if the priority of the current task is higher than the priority ceiling of the resource. If the current task's priority is lower than the priority ceiling, then it is blocked until the resource is released.

Advantages of the Preemption Ceiling Protocol:

- It prevents priority inversion, which can be a major problem in real-time systems.
- It is simple to implement and can be used with many different scheduling algorithms.
- It guarantees that a task will not be preempted while it holds a resource, which can be important for certain real-time applications.

Disadvantages of the Preemption Ceiling Protocol:

- It requires assigning priority ceilings to resources, which can be difficult to do in complex systems.
- It can lead to priority inversion if the priority ceilings are not set correctly.

Example:

Consider a system with two tasks: Task 1 has a priority of 3 and needs to access Resource A, which has a priority ceiling of 2. Task 2 has a priority of 2 and needs to access Resource B, which has a priority ceiling of 1. If Task 1 attempts to acquire Resource A while it is held by Task 2, then Task 1's priority will be raised to 2, which is higher than the priority ceiling of Resource B. Therefore, Task 2 will be blocked until Task 1 releases Resource A.

Applications:

The Preemption Ceiling Protocol is commonly used in real-time systems, particularly those that use priority-based scheduling algorithms. It is also used in embedded systems and safety-critical systems where reliability is important.