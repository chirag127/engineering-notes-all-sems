### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can enter the critical section at a time.
- If another task attempts to enter the critical section while it is already occupied, it will be blocked until the occupying task exits the critical section.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and spinlocks.
- It is important to use non-preemptive critical sections carefully, as they can introduce priority inversion and negatively impact the real-time performance of the system.
- Priority inversion occurs when a high-priority task is blocked by a lower-priority task that is executing in a non-preemptive critical section.
- To avoid priority inversion, it is important to keep the length of non-preemptive critical sections as short as possible and to use priority inheritance or priority ceiling protocols.