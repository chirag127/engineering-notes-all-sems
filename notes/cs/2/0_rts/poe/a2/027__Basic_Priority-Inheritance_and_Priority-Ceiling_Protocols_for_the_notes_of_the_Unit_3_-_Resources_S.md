 Here is the content in markdown format without any emojis or external links and in formal tone:

### Basic Priority-Inheritance and Priority-Ceiling Protocols

1. Priority Inheritance Protocol:
- When a higher priority task assigns a resource to a lower priority task, the priority of the lower priority task is temporarily increased to that of the higher priority task.
- This ensures that the lower priority task completes and releases the resource quickly.
- For example, if task T1 (priority 5) assigns a resource to task T2 (priority 3), the priority of T2 is increased from 3 to 5. This ensures T2 completes and releases the resource quickly, allowing T1 to also complete.

2. Priority Ceiling Protocol:
- Each shared resource is assigned a priority called the 'ceiling priority'.
- When a task acquires a resource, its priority is increased to the ceiling priority of that resource.
- This prevents other higher priority tasks from preempting the resource-holding task, and creating priority inversion.
- The ceiling priorities are chosen carefully to avoid priority conflicts with other high priority tasks in the system.
- For example, if resource R1 has a ceiling priority of 4, and task T2 (original priority 3) acquires R1, its priority is increased to 4. This prevents other priority 3 or lower priority tasks from preempting T2.

The above protocols can be used to ensure predictable execution patterns and avoid priority inversion in real-time embedded systems with shared resources. Proper protocol selection and ceiling priority assignment is important for optimal system performance.