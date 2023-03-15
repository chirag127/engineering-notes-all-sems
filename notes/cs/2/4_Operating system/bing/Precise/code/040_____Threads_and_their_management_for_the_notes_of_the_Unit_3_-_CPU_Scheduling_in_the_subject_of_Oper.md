### Threads and their management for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A thread is a basic unit of CPU utilization, consisting of a program counter, a stack, and a set of registers.
- Threads are sometimes referred to as lightweight processes and they do not require much memory overhead; they are cheaper than processes.
- A thread has or shares with other threads certain resources, including code section, data section, and other operating-system resources, such as open files and signals.
- A traditional or heavyweight process has a single thread of control. If a process has multiple threads of control, it can perform more than one task at a time.
- There are two main approaches to implementing threads in an operating system: user-level threads and kernel-level threads.
- User-level threads are managed by a user-level library and the kernel is not aware of the existence of these threads. The kernel continues to schedule the process as a single execution unit.
- Kernel-level threads are managed directly by the operating system. The kernel has full knowledge of all threads and schedules them accordingly.
- There are several benefits to using threads, including increased responsiveness, resource sharing, economy, and scalability.
- Thread management involves creating, scheduling, and synchronizing threads. The operating system is responsible for managing threads and ensuring that they are scheduled and executed efficiently.
- Thread scheduling can be done using various algorithms, including first-come, first-served, shortest job first, and priority scheduling.
- Thread synchronization is necessary to ensure that threads do not interfere with each other and that shared resources are accessed in a controlled manner. This can be achieved using various synchronization techniques, such as locks, semaphores, and monitors.