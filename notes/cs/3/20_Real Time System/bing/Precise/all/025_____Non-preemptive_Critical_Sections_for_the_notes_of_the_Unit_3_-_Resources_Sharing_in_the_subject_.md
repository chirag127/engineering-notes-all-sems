### Non-preemptive Critical Sections

- Non-preemptive critical sections refer to sections of code that cannot be interrupted by the scheduler.
- These sections are used to protect shared resources from being accessed by multiple threads or processes simultaneously.
- Non-preemptive critical sections are implemented using synchronization mechanisms such as semaphores, mutexes, or monitors.
- These mechanisms ensure that only one thread or process can enter the critical section at a time.
- Once a thread or process enters the critical section, it cannot be preempted until it exits the critical section.
- This ensures that the shared resource is accessed in a mutually exclusive manner, preventing race conditions and other synchronization issues.
- Non-preemptive critical sections are commonly used in real-time systems to ensure predictable and deterministic behavior.
- However, care must be taken to avoid priority inversion, where a high-priority thread is blocked by a lower-priority thread holding a critical section.
- Priority inheritance or priority ceiling protocols can be used to mitigate this issue.
