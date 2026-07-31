 Here is the content in Markdown format without any emojis or external links:

### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

1. Preemption Ceiling Protocol (PCP) is a priority inheritance protocol used for resource sharing in real-time systems.
2. In PCP, each resource is assigned a ceiling priority. A task can preempt a lower priority task only if its priority is higher than the ceiling priority of all resources currently held by the lower priority task.
3. When a task acquires a resource, its priority is raised to the ceiling priority of that resource if its original priority is lower. When the task releases the resource, its priority is reset to the original value.
4. This protocol ensures that a task will never be preempted by another task while it holds a resource. Thus, it prevents priority inversion and ensures that critical sections are executed without delay or interruption.
5. However, PCP may introduce unbounded priority inversion and may result in significant blocking times for tasks waiting to acquire resources. It is suitable for systems with a small number of resources and tasks.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.