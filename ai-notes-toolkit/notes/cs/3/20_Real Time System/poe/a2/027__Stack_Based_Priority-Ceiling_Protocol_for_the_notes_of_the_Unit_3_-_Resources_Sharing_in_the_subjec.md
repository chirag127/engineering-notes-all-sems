 Here are the notes on Stack Based Priority-Ceiling Protocol for the Unit 3 - Resources Sharing in the subject of Real Time System:

### Stack Based Priority-Ceiling Protocol

- It is a resource access protocol used for real-time systems to avoid priority inversion.
- Priority inversion occurs when a high priority task is blocked by a low priority task that is holding a shared resource.
- In Stack Resource Policy, each resource is assigned a ceiling priority. When a task acquires a resource, its priority is elevated to the ceiling priority of that resource. This prevents priority inversion.
- When the task releases the resource, its priority is reset to its original priority.
- The stack resource policy ensures that a task will never be preempted by another task of equal or lower priority while it holds resources. Hence, it avoids priority inversion.
- The overhead of manipulating priorities may affect the performance of the system. Also, it does not address the problem of deferring the execution of higher priority tasks due to resources being unavailable.
- It is suitable for systems with a small fixed number of resources and priorities. It avoids the state explosion problem of other protocols.

The notes are written in points and in a formal tone without any emojis or external links as per the given instructions. The content is written inside the requested header for the specified topic and course module. Please let me know if you would like me to modify or expand the notes in any way.