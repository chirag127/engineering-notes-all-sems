### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can enter the critical section at a time, while other tasks attempting to enter the critical section are blocked until the task currently in the critical section exits.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and spinlocks.
- It is important to carefully design the use of non-preemptive critical sections to avoid issues such as priority inversion and deadlock.
- Priority inversion occurs when a lower priority task holds a resource needed by a higher priority task, causing the higher priority task to be blocked.
- Deadlock occurs when two or more tasks are blocked waiting for resources held by each other, resulting in a circular wait.
- To avoid these issues, it is important to follow best practices such as using the priority ceiling protocol and avoiding nested critical sections.
