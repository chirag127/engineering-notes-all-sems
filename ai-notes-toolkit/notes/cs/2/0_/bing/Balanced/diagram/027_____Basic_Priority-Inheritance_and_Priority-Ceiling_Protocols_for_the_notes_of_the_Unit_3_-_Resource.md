### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed priority scheduling.
- Both protocols aim to reduce the blocking time of high priority tasks due to lower priority tasks holding shared resources, and to prevent priority inversion and deadlock situations.
- Priority inversion occurs when a high priority task is blocked by a lower priority task, and the lower priority task is preempted by a medium priority task, thus delaying the execution of the high priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed.

#### Priority-Inheritance Protocol (PIP)

- PIP works by temporarily raising the priority of a lower priority task that holds a resource to the priority of the highest priority task that is blocked by it.
- This way, the lower priority task can finish its critical section and release the resource, allowing the higher priority task to resume.
- PIP has the following rules:

  1. A task can access a resource only if it is not held by another task with a higher priority.
  2. A task that holds a resource inherits the priority of the highest priority task that is blocked by it, and retains this priority until it releases the resource.
  3. A task that releases a resource resumes its original priority.

- PIP can reduce the blocking time of high priority tasks, but it cannot prevent deadlock or bound the number of priority inversions.

#### Priority-Ceiling Protocol (PCP)

- PCP works by assigning a ceiling priority to each resource, which is the highest priority of any task that can access the resource.
- A task can access a resource only if its priority is higher than the ceiling priorities of all the resources currently held by other tasks.
- This way, PCP prevents a lower priority task from blocking a higher priority task that needs a resource, and also prevents deadlock and multiple priority inversions.
- PCP has the following rules:

  1. A task can access a resource only if its priority is higher than the ceiling priorities of all the resources currently held by other tasks.
  2. A task that accesses a resource inherits the ceiling priority of the resource, and retains this priority until it releases the resource.
  3. A task that releases a resource resumes its original priority.

- PCP can prevent deadlock and bound the blocking time of high priority tasks, but it requires more support from the operating system and may deny a task from accessing a free resource if its priority is lower than the ceiling priority of the resource.