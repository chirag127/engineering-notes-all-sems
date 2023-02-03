### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

Non-preemptive Critical Sections in Real Time Systems:

In Real Time Systems, critical sections are portions of code that access shared resources and must be executed atomically, without interruption. Non-preemptive critical sections are critical sections that cannot be interrupted by other tasks or processes once they have started executing.

Non-preemptive critical sections are typically implemented using semaphores, which are synchronization mechanisms that control access to shared resources. A semaphore is a variable that is used to indicate the availability of a shared resource. When a task enters a critical section, it acquires the semaphore associated with the shared resource, and releases the semaphore when it has finished accessing the resource.

One advantage of non-preemptive critical sections is that they can be simpler to implement than preemptive critical sections, as they do not require the use of interrupt disabling or other advanced synchronization techniques. However, non-preemptive critical sections can also lead to priority inversion, where a lower-priority task holds a semaphore that is needed by a higher-priority task, leading to the higher-priority task being blocked.

In conclusion, non-preemptive critical sections are critical sections in Real Time Systems that cannot be interrupted by other tasks or processes once they have started executing. Non-preemptive critical sections are typically implemented using semaphores, which are synchronization mechanisms that control access to shared resources. The use of non-preemptive critical sections can lead to priority inversion, where a lower-priority task holds a semaphore that is needed by a higher-priority task.
