Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of basic priority-inheritance and priority-ceiling protocols for resource sharing in real-time systems.

### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Resource sharing in real-time systems can cause priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a shared resource.
- Priority inversion can lead to missed deadlines, reduced performance, and even deadlock.
- To avoid priority inversion, two protocols are commonly used: the basic priority-inheritance protocol and the priority-ceiling protocol.
- The basic priority-inheritance protocol works as follows:
  - Each resource has a priority equal to the highest priority of any task that can access it.
  - When a task requests a resource, it inherits the priority of the resource if it is higher than its own priority.
  - When a task releases a resource, it reverts to its original priority.
  - This way, a higher-priority task can preempt a lower-priority task that holds a resource, and the lower-priority task can resume its execution when the resource is released.
- The basic priority-inheritance protocol can reduce the blocking time of a higher-priority task to at most the duration of a single critical section of a lower-priority task.
- However, the basic priority-inheritance protocol has some drawbacks:
  - It can cause chained blocking, which is a situation where a task is blocked by another task that is blocked by another task, and so on.
  - It can cause multiple inheritance, which is a situation where a task inherits the priority of multiple resources, and may end up with a higher priority than necessary.
  - It can cause unnecessary preemptions, which can increase the overhead and reduce the schedulability of the system.
- The priority-ceiling protocol improves the basic priority-inheritance protocol by minimizing the blocking time and preventing deadlock.
- The priority-ceiling protocol works as follows:
  - Each resource has a priority ceiling equal to the highest priority of any task that can access it.
  - A task can access a resource only if its priority is higher than the priority ceiling of all the resources currently held by other tasks.
  - When a task requests a resource, it inherits the priority ceiling of the resource if it is higher than its own priority.
  - When a task releases a resource, it reverts to its original priority.
  - This way, a higher-priority task can access a resource without being blocked by a lower-priority task, and a lower-priority task can avoid blocking a higher-priority task by deferring its request until the resource is free.
- The priority-ceiling protocol can reduce the blocking time of a higher-priority task to at most the duration of a single critical section of a lower-priority task, and can prevent deadlock by avoiding circular waits.
- However, the priority-ceiling protocol has some drawbacks:
  - It can cause avoidance blocking, which is a situation where a task is denied access to a free resource because of the priority ceiling of another resource held by a lower-priority task.
  - It can cause unnecessary blocking, which is a situation where a task is blocked by a lower-priority task that does not hold the requested resource, but has a higher priority ceiling.
  - It can cause priority inversion, which is a situation where a lower-priority task holds a resource with a higher priority ceiling than the priority of a higher-priority task that does not request the resource.

: Difference between Priority Inheritance and Priority Ceiling Protocols. https://benchpartner.com/difference-between-priority-inheritance-and-priority-ceiling-protocols
: The Priority Ceiling Protocol: A Method for Minimizing the Blocking of High Priority Processes. https://apps.dtic.mil/sti/pdfs/ADA206572.pdf
: Resource Access Control in Real-time Systems. https://csperkins.org/teaching/2011-2012/adv-os/lecture08.pdf