# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems that involve shared resources and preemptive scheduling.
- The goal of these protocols is to prevent or minimize unbounded priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a resource needed by the high-priority task.
- Priority inversion can cause deadline misses, reduced system utilization, and increased response times.

## Priority-Inheritance Protocol

- The basic idea of the priority-inheritance protocol is that when a high-priority task is blocked by a low-priority task that holds a resource, the low-priority task inherits the priority of the high-priority task until it releases the resource.
- This way, the low-priority task can finish its critical section faster and unblock the high-priority task, reducing the blocking time.
- The priority-inheritance protocol can be implemented using a priority queue for each resource, where the highest-priority task that requests the resource is at the head of the queue.
- When a task requests a resource, it checks the queue and if it is empty, it acquires the resource and becomes the owner of the queue. If the queue is not empty, it appends itself to the queue and blocks until the resource is available.
- When a task releases a resource, it removes itself from the queue and restores its original priority. If the queue is not empty, it transfers the ownership of the queue and the resource to the next task in the queue, and boosts its priority to the highest priority of any task in the queue.
- The priority-inheritance protocol guarantees that the blocking time of a task is bounded by the duration of the longest critical section of any lower-priority task that shares a resource with it.
- However, the priority-inheritance protocol has some drawbacks, such as:
  - It can cause chained blocking, where a medium-priority task is blocked by a low-priority task that inherits the priority of a high-priority task, and the high-priority task is blocked by another task that holds a different resource.
  - It can cause multiple priority inversions, where a high-priority task is blocked by a low-priority task that holds a resource, and then the low-priority task is preempted by another high-priority task that does not need the resource.
  - It can cause unnecessary priority boosting, where a low-priority task inherits the priority of a high-priority task that requests a resource, but the high-priority task is blocked by another task that holds a different resource.

## Priority-Ceiling Protocol

- The basic idea of the priority-ceiling protocol is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access the resource.
- A task can acquire a resource only if its priority is higher than the priority ceiling of all the resources currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from blocking a higher-priority task that needs a different resource, and avoids chained blocking and multiple priority inversions.
- The priority-ceiling protocol can be implemented using a system ceiling, which is the highest priority ceiling of all the resources currently held by any task, and a local ceiling, which is the highest priority ceiling of all the resources that a task can access.
- When a task requests a resource, it checks the system ceiling and if it is lower than its priority, it acquires the resource and raises the system ceiling to the priority ceiling of the resource. If the system ceiling is higher than its priority, it blocks until the system ceiling is lower than its priority.
- When a task releases a resource, it lowers the system ceiling to the highest priority ceiling of all the resources still held by any task. If the system ceiling is lower than the local ceiling of the task, it restores its original priority. If the system ceiling is higher than the local ceiling of the task, it boosts its priority to the system ceiling.
- The priority-ceiling protocol guarantees that the blocking time of a task is bounded by the duration of the shortest critical section of any lower-priority task that shares a resource with it.
- However, the priority-ceiling protocol has some drawbacks, such as:
  - It can cause avoidance blocking, where a task is denied access to a free resource because the system ceiling is higher than its priority, and the resource is held by a lower-priority task that does not need it.
  - It can cause unnecessary priority boosting, where a task inherits the system ceiling even