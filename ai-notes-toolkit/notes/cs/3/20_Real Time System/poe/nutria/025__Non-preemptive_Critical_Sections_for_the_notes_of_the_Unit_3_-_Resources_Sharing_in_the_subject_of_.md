
### Non-preemptive Critical Sections

1. Non-preemptive critical sections are sections of code that must execute uninterrupted, without interruption from other processes.
2. This is necessary in order to ensure that shared resources are not corrupted when multiple processes are using them.
3. Non-preemptive critical sections are used in real-time systems, which require processes to finish within a certain amount of time.
4. In a non-preemptive critical section, the process that is currently executing the code will be allowed to finish before any other processes can access the shared resource.
5. This is in contrast to preemptive critical sections, which allow processes to interrupt each other while accessing the shared resource.
6. Non-preemptive critical sections are often implemented using semaphores or monitors.
7. Semaphores are used to control access to shared resources, while monitors provide synchronization between processes.
8. Non-preemptive critical sections are used to ensure that processes that require access to a shared resource do not interfere with each other and corrupt the data.