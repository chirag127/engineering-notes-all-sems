# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Both protocols aim to prevent unbounded priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource.
- Both protocols also aim to prevent deadlock, which is a situation where two or more tasks are waiting for each other to release a resource.

## Priority-Inheritance Protocol

- The basic idea of priority-inheritance protocol is that when a high-priority task is blocked by a low-priority task that holds a resource, the low-priority task inherits the priority of the high-priority task until it releases the resource.
- This way, the low-priority task can finish its critical section faster and unblock the high-priority task sooner.
- The priority-inheritance protocol has the following properties:
  - It is greedy, meaning that a task can access a resource whenever it is free, regardless of the priorities of other tasks that may request the same resource later.
  - It is transitive, meaning that if a task inherits the priority of another task, it also inherits the priority of any other task that the latter task inherits from.
  - It is dynamic, meaning that the priority of a task can change during its execution depending on the blocking situation.
  - It guarantees that the blocking time of a task is bounded by the duration of the longest critical section of any lower-priority task that shares a resource with it .

## Priority-Ceiling Protocol

- The basic idea of priority-ceiling protocol is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource.
- A task can access a resource only if its priority is higher than the priority ceiling of all the resources currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from being blocked by a lower-priority task that does not hold the requested resource, which is called avoidance blocking.
- The priority-ceiling protocol has the following properties:
  - It is not greedy, meaning that a task may be denied access to a free resource if its priority is lower than the priority ceiling of another resource held by another task.
  - It is not transitive, meaning that a task does not inherit the priority of any other task that holds a resource.
  - It is static, meaning that the priority of a task does not change during its execution.
  - It guarantees that the blocking time of a task is bounded by the duration of a single (outermost) critical section of any lower-priority task that shares a resource with it .

## Comparison

- The priority-ceiling protocol is better than the priority-inheritance protocol in terms of reducing the blocking time, preventing deadlock, and simplifying the analysis of schedulability  .
- However, the priority-ceiling protocol requires a priori knowledge of the resource usage and priority assignment of all the tasks, which may not be available or feasible in some situations .
- The priority-inheritance protocol is more flexible and adaptable to dynamic changes in the system, but it may incur more overhead and complexity in the implementation .