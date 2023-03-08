 Here is the content in markdown format for the topic -

### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority Ceiling Protocol (PCP) is used in dynamic priority systems to avoid priority inversion.
- In dynamic priority systems, the priority of a task can increase or decrease based on its state. This can lead to priority inversion where a higher priority task waits for a lower priority task to complete.
- PCP assigns a priority ceiling to each resource. The priority ceiling of a resource is the highest priority of all tasks that may use the resource.
- When a task acquires a resource, its priority is raised to the ceiling priority of that resource. This prevents any lower priority task from interrupting the resource-holding task.
- When the task releases the resource, its priority is restored to its original value.
- This way, PCP prevents lower priority tasks from delaying the high priority tasks and avoids priority inversion.
- However, a major disadvantage is that the priorities of tasks can fluctuate frequently leading to a complex system with timing unpredictability. Also, a global knowledge of all tasks and resources is required to assign correct priority ceilings.

**Advantages:**
- Prevents priority inversion and delays to high priority tasks.
- Simple to implement.

**Disadvantages:**
- Priorities fluctuate frequently leading to complex and unpredictable systems.
- Requires global knowledge of all tasks and resources.

**Applications:** Real-time systems, especially embedded systems with multiple tasks and shared resources like I/O devices, communication channels, etc.

[Detailed diagrams and examples can be added here to aid understanding]