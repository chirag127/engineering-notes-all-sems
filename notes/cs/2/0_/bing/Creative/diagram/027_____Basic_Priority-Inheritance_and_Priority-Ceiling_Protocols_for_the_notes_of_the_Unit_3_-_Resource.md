### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- They aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent deadlocks and priority inversions.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the execution of the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed.

#### Priority-Inheritance Protocol (PIP)

- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it.
- This way, the low-priority task can finish its critical section and release the resource as soon as possible, without being preempted by any other task.
- PIP can reduce the blocking time of high-priority tasks, but it cannot prevent deadlocks or chained blocking.
- Chained blocking occurs when a high-priority task is blocked by a low-priority task, which is blocked by another low-priority task, and so on.
- PIP requires minimum support from the operating system, and it is easy to implement.

#### Priority-Ceiling Protocol (PCP)

- PCP works by assigning a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priorities of all the resources that are currently locked by other tasks.
- This way, PCP can prevent deadlocks and chained blocking, and also reduce the blocking time of high-priority tasks.
- PCP requires maximum support from the operating system, and it is more complex to implement.
- There are two variants of PCP: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP raises the priority of a task to the ceiling priority of the resource when it locks the resource, and restores its original priority when it releases the resource.
- ICPP raises the priority of a task to the ceiling priority of the resource when it requests the resource, and restores its original priority when it releases the resource.