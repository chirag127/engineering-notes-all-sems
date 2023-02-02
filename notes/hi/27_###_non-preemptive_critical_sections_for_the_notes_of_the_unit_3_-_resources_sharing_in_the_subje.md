### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System
Non-Preemptive Critical Section:
- A critical section is a piece of code that accesses a shared resource.
- Non-preemptive critical section means that once a process enters the critical section, it cannot be preempted until it leaves the critical section.
- This helps ensure that the shared resource is not accessed by multiple processes at the same time, which could cause problems such as data corruption.
- Non-preemptive critical sections can be implemented using semaphores or locks.
- The disadvantage of non-preemptive critical sections is that a process can block other processes from accessing the shared resource if it takes too long to complete its critical section.
