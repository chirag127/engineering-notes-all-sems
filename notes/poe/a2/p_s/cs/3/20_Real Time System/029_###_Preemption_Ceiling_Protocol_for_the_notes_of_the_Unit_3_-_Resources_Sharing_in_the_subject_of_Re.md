 Here is the content in markdown format for the topic ### Preemption Ceiling Protocol:

### Preemption Ceiling Protocol

- Preemption Ceiling Protocol (PCP) is a priority inheritance protocol used for resource sharing in real-time systems.
- It assigns a priority ceiling to each resource, which is the highest priority of all tasks that may access the resource.
- When a task acquires a resource, its priority is raised to the ceiling of that resource. This prevents lower-priority tasks from preempting the resource holder.
- When the task releases the resource, its priority is restored to its original value.
- This protocol avoids priority inversion and ensures that higher-priority tasks are not blocked by lower-priority tasks holding a shared resource.
- However, it may lead to priority boosting, where a task executes at a higher priority than required, which can affect the schedulability of the system.
- PCP is easier to implement than Stack Resource Policy but may suffer from more priority inversions. It is suitable for systems with a small number of resources and priority levels.

**Advantages:**
- Prevents priority inversion and ensures timely execution of higher-priority tasks.
- Simple to implement.

**Disadvantages:**
- May lead to priority boosting and affect schedulability.
- Not suitable for systems with many resources and priority levels.

**Examples:** Implementing a printer spooler service in a real-time system.

**Applications:** Used in real-time operating systems such as QNX for resource sharing.

[Detailed diagrams and codes can be added here to aid understanding]