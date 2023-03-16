### Non-preemptive Critical Sections

Non-preemptive critical sections refer to sections of code that are executed without interruption. This means that once a task enters a non-preemptive critical section, it cannot be preempted until it exits the critical section. This is achieved by disabling interrupts or by using a scheduling policy that does not allow preemption.

Here are some key points to remember about non-preemptive critical sections:

1. Non-preemptive critical sections are used to protect shared resources from concurrent access.
2. They ensure that only one task can access the shared resource at a time.
3. Non-preemptive critical sections can be implemented using various synchronization mechanisms such as semaphores, mutexes, and monitors.
4. The use of non-preemptive critical sections can lead to priority inversion, where a high priority task is blocked by a lower priority task that is executing a critical section.
5. To avoid priority inversion, priority inheritance or priority ceiling protocols can be used.
