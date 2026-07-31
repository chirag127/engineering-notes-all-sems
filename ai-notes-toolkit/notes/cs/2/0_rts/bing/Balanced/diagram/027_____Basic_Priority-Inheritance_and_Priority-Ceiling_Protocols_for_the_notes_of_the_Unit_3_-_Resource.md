### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance protocol (PIP) and priority-ceiling protocol (PCP) are two methods for resolving priority inversion problem in real-time systems.
- Priority inversion occurs when a higher-priority task is blocked by a lower-priority task that holds a shared resource, and the lower-priority task is preempted by a medium-priority task that does not need the resource.
- PIP and PCP aim to reduce the blocking time of higher-priority tasks and prevent deadlock situations.

#### Priority-Inheritance Protocol

- PIP works by temporarily boosting the priority of the lower-priority task that holds the resource to the priority of the highest-priority task that requests the resource.
- This way, the lower-priority task can finish its critical section and release the resource, allowing the higher-priority task to resume execution.
- PIP can be applied to nested resources, where a task may hold more than one resource at a time. In this case, the priority of the task is boosted to the highest priority of any task that requests any of the resources it holds.
- PIP has the following properties:
  - It eliminates unbounded priority inversion, as the blocking time of a higher-priority task is limited by the duration of the critical sections of the lower-priority tasks that hold the resources it needs.
  - It is greedy, as it allows a task to access a resource whenever it is free, regardless of the priorities of other tasks that may request the same resource in the future.
  - It may cause chained blocking, where a task is blocked by another task that is blocked by another task, and so on, resulting in a long chain of blocked tasks.
  - It may cause deadlock, if there is a circular dependency among the tasks and the resources they need.

#### Priority-Ceiling Protocol

- PCP works by assigning a static priority ceiling to each resource, which is the highest priority of any task that may access the resource.
- A task can access a resource only if its priority is higher than the priority ceilings of all the resources currently held by other tasks.
- This way, the priority ceiling of a resource acts as a barrier that prevents lower-priority tasks from accessing the resource and blocking higher-priority tasks.
- PCP can be applied to nested resources, where a task may hold more than one resource at a time. In this case, the priority of the task is raised to the highest priority ceiling of any resource it holds.
- PCP has two variants: original ceiling priority protocol (OCPP) and immediate ceiling priority protocol (ICPP).
  - OCPP raises the priority of a task only when it accesses a resource, and lowers it when it releases the resource.
  - ICPP raises the priority of a task as soon as it becomes ready to run, and lowers it when it finishes execution.
- PCP has the following properties:
  - It eliminates unbounded priority inversion, as the blocking time of a higher-priority task is limited by the duration of a single critical section of a lower-priority task.
  - It is not greedy, as it may withhold access to a free resource, causing a task to be blocked by a lower-priority task that does not hold the requested resource. This is called avoidance blocking.
  - It prevents chained blocking, as a task can be blocked by at most one lower-priority task at a time.
  - It prevents deadlock, as it ensures that a task can access a resource only if it has a higher priority than any other task that may need the same resource.