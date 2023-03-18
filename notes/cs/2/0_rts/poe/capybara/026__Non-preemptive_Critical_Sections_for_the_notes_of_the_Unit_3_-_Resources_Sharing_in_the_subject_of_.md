### Non-preemptive Critical Sections

In a real-time system, multiple tasks may need to access shared resources simultaneously. To ensure proper resource sharing, non-preemptive critical sections are used. These critical sections are also known as mutual exclusion sections or mutex.

Here are some key points to remember about non-preemptive critical sections:

- Non-preemptive critical sections are used to ensure that only one task can access a shared resource at a time. This prevents race conditions and data corruption.
- A task that needs to access a shared resource must enter the critical section before accessing the resource. Once a task enters the critical section, no other task can enter until the first task exits.
- Non-preemptive critical sections are implemented using semaphores. A semaphore is a synchronization object that can be used to block access to a shared resource.
- A semaphore has two states: locked and unlocked. When a task enters a critical section, it locks the semaphore. When the task exits the critical section, it unlocks the semaphore.
- If a task attempts to enter a critical section that is already locked, it will block until the semaphore is unlocked.
- Non-preemptive critical sections are non-preemptive, which means that a task cannot be interrupted while it is in a critical section. This ensures that the task can complete its operation without interference from other tasks.

In summary, non-preemptive critical sections are an essential tool for ensuring proper resource sharing in a real-time system. By using semaphores to synchronize access to shared resources, non-preemptive critical sections prevent race conditions and data corruption.