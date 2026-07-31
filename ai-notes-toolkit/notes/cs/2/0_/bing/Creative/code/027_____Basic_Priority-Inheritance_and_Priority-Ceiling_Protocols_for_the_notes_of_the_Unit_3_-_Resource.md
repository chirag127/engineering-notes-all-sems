### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- Both protocols aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent priority inversion and deadlock situations.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the execution of the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed.

#### Priority-Inheritance Protocol (PIP)

- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it or that may block it in the future.
- This way, the low-priority task can finish using the resource and release it to the high-priority task, thus avoiding priority inversion and reducing blocking time.
- PIP has the following rules :
  - A task can lock a resource only if it is not locked by another task, or if it is locked by a task with lower or equal priority.
  - A task that locks a resource inherits the highest priority of any task that is blocked by it or that may block it in the future, until it releases the resource.
  - A task that releases a resource reverts to its original priority.
- PIP has the following advantages :
  - It overcomes the limitations of traditional priority-based scheduling, such as unbounded priority inversion and deadlock.
  - It requires minimum support from the operating system, such as priority manipulation and resource status tracking.
  - It preserves the optimality of fixed-priority scheduling, such as the rate-monotonic algorithm.
- PIP has the following disadvantages :
  - It can still cause long blocking times, especially for tasks with intermediate priorities, as they may be blocked by multiple lower-priority tasks.
  - It can cause chained blocking, where a high-priority task is blocked by a low-priority task that is blocked by another low-priority task, and so on.
  - It can not prevent deadlock, as two or more tasks may lock different resources and wait for each other to release them.

#### Priority-Ceiling Protocol (PCP)

- PCP works by assigning a priority ceiling to each shared resource, which is the highest priority of any task that can lock that resource, and by preventing a task from locking a resource if its priority is lower than the priority ceiling of any locked resource.
- This way, PCP ensures that a high-priority task can always access a resource if it is free, and that a low-priority task can not lock a resource if it may block a high-priority task, thus avoiding priority inversion and deadlock.
- PCP has the following rules  :
  - A task can lock a resource only if it is not locked by another task, or if it is locked by a task with lower or equal priority, and if its priority is higher than the priority ceiling of any locked resource.
  - A task that locks a resource inherits the priority ceiling of that resource, until it releases the resource.
  - A task that releases a resource reverts to its original priority.
- PCP has the following advantages  :
  - It overcomes the limitations of PIP and traditional priority-based scheduling, such as unbounded priority inversion, chained blocking, and deadlock.
  - It reduces the blocking time of high-priority tasks to at most one critical section of the lowest-priority task that can lock the same resource.
  - It prevents tasks from going into an unbounded wait state, as they can always access a resource if it is free and they have higher priority than any locked resource.
- PCP has the following disadvantages  :
  - It requires maximum support from the operating system, such as priority ceiling assignment, resource status tracking, and priority ceiling checking.
  - It may deny a task from locking a resource even if it is free, if its priority is lower than the priority ceiling of any locked resource, thus causing unnecessary blocking.
  - It may cause priority inversion, if a