 Here are the notes in formal markdown format without any emojis or external links:

### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

1. Priority inversion: When a high priority task is blocked by a low priority task leading to delay in execution of high priority task. This is undesirable in real-time systems.
2. Priority Ceiling Protocol: It avoids priority inversion and works as follows:
- Each shared resource is assigned a priority ceiling which is the highest priority of any task that may use the resource.
- A task may execute only if its priority is higher than the ceiling of all resources it may access.
- While accessing a shared resource, a task is temporarily raised to the ceiling priority of that resource. This prevents lower priority tasks from interrupting the task and avoids priority inversion.
3. The Priority Ceiling Protocol ensures timely execution of high priority tasks and hence is suitable for real-time systems using dynamic priority scheduling. However, it may lead to reduced parallelism and resource utilization.

The above notes cover the key points around priority inversion, Priority Ceiling Protocol and how the latter avoids priority inversion to ensure predictable execution of high priority real-time tasks sharing resources using dynamic priority scheduling. The points are written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to elaborate on any part or modify the notes in any way.