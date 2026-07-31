 Here is the formatted content in Markdown format without any emojis or external links:

### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority Ceiling Protocol (PCP) is used in dynamic priority systems to avoid priority inversion.
- Priority inversion occurs when a high priority task is blocked by a low priority task that is holding a shared resource.
- PCP assigns a priority ceiling to each shared resource. The priority ceiling is the highest priority of any task that may use the resource.
- When a task acquires a shared resource, its priority is raised to the ceiling priority of that resource. This prevents lower priority tasks from interrupting the resource holder.
- Once the task releases the resource, its priority is restored to its original level.
- In this way, PCP prevents lower priority tasks from delaying high priority tasks and avoids priority inversion.
- PCP is easy to implement but may degrade system performance due to frequent changes in task priorities.
- The optimal choice of priority ceilings is crucial for efficiency and proper functioning of the system.

The above content is written in a formal tone with points in a straightforward manner like study notes without any emojis or external links as required. Please let me know if you would like me to modify or expand the answer.