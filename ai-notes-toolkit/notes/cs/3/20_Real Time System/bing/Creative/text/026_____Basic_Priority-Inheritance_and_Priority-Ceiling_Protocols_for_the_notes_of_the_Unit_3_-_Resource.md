### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- Both protocols aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources, and to prevent priority inversion and deadlock situations.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the execution of the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed.

#### Priority-Inheritance Protocol (PIP)

- PIP works by temporarily raising the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it or that may block it in the future.
- This way, the low-priority task can finish using the resource and release it to the high-priority task, thus avoiding priority inversion and reducing blocking time.
- PIP requires minimum support from the operating system, and can be implemented using semaphores or mutexes.
- PIP cannot prevent deadlock, as it is possible that a circular chain of tasks holding and waiting for resources may form, and none of them can inherit a higher priority to break the cycle.
- PIP is a greedy protocol, as it allows a task to acquire a resource whenever it is free, regardless of the priorities of other tasks that may need it later.

#### Priority-Ceiling Protocol (PCP)

- PCP works by assigning a static priority ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can acquire a resource only if its priority is higher than the priority ceilings of all the resources currently held by other tasks, otherwise it is blocked.
- This way, PCP prevents deadlock, as it avoids circular waiting by enforcing a strict order of resource acquisition based on priority ceilings.
- PCP also prevents priority inversion, as it ensures that a high-priority task can always access a resource if it is free, and that a low-priority task holding a resource will run at the priority ceiling of that resource until it releases it.
- PCP requires maximum support from the operating system, and can be implemented using semaphores with priority ceiling attributes.
- PCP is a non-greedy protocol, as it may deny a task to acquire a resource even if it is free, if the task's priority is lower than the priority ceilings of other resources. This may lead to unnecessary blocking, but also to better resource utilization.