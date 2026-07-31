### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- This means that once a task enters a non-preemptive critical section, it will continue to execute until it exits the critical section, regardless of the priority of other tasks.
- Non-preemptive critical sections are used to protect shared resources from concurrent access by multiple tasks.
- This is achieved by ensuring that only one task can enter the critical section at a time.
- If another task attempts to enter the critical section while it is already occupied, it will be blocked until the occupying task exits the critical section.
- Non-preemptive critical sections can be implemented using various synchronization mechanisms, such as semaphores or mutexes.
- It is important to use non-preemptive critical sections carefully, as they can introduce the potential for priority inversion and deadlock if not used correctly.
- Priority inversion occurs when a lower priority task holds a resource needed by a higher priority task, causing the higher priority task to be blocked.
- Deadlock occurs when two or more tasks are blocked, waiting for resources held by each other, resulting in a circular wait.
- To avoid these issues, it is important to follow best practices for using non-preemptive critical sections, such as avoiding nested critical sections and ensuring that tasks do not hold resources for longer than necessary.