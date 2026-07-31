 Here is the content in markdown format without any emojis or external links and in formal tone:

### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

1. Preemption Ceiling Protocol (PCP) is a priority inheritance protocol used for resource sharing in real time systems.
2. In PCP, each resource is assigned a ceiling priority. The thread that acquires a resource is elevated to the ceiling priority of that resource.
3. If a higher priority thread requests a resource that is held by a lower priority thread, the ceiling of the resource is inherited, thereby preventing priority inversion.
4. As a result, a thread will always execute at a priority equal to or greater than the ceiling of any resource that it holds. Thus, delay due to resource sharing is bounded by the ceiling priority.
5. The major advantage of the Preemption Ceiling Protocol is that it avoids the complex bookkeeping of tracking and transferring priorities between threads that is required in the Priority Inheritance Protocol. The disadvantage is that a high priority thread can be blocked by a low priority thread that holds a resource with a very high ceiling priority.

The above content summarizes the key points about the Preemption Ceiling Protocol for resource sharing in real time systems. The points are written in a formal tone with no emojis or external links as required. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.