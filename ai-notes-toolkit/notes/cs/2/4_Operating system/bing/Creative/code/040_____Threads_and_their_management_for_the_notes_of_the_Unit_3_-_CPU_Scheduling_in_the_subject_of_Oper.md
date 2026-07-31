### Threads and their management

- A thread is a single sequential flow of execution of tasks of a process .
- A thread is also known as a lightweight process that the operating system can schedule and run concurrently with other threads.
- The operating system creates and manages threads, and they share the same memory and resources as the program that created them.
- This enables multiple threads to collaborate and work efficiently within a single program.
- The life cycle of a thread in an operating system involves the creation, scheduling, execution, blocking, and termination.
- The operating system plays a critical role in managing the life cycle of threads, ensuring that they run efficiently and effectively.
- Creation: A thread is created by a process or by another thread within the same process.
- Scheduling: The operating system is responsible for assigning CPU time to the threads and processes based on various scheduling algorithms.
- Execution: A thread executes the tasks assigned to it by the program or the operating system.
- Blocking: A thread may be blocked by the operating system due to various reasons, such as waiting for an I/O operation, synchronization, or termination of another thread.
- Termination: A thread may be terminated by the operating system when it completes its tasks, or by the program or another thread that created it.
- Types of threads: There are two types of threads in operating systems: user-level threads and kernel-level threads.
- User-level threads: These are threads that are created and managed by the user-level libraries, such as POSIX threads or Java threads.
- User-level threads are not visible to the operating system, and they run on top of a single kernel-level thread.
- User-level threads have the advantage of being fast and flexible, but they have the disadvantage of being dependent on the underlying kernel-level thread and not being able to utilize multiprocessor systems.
- Kernel-level threads: These are threads that are created and managed by the operating system, such as Windows threads or Linux threads.
- Kernel-level threads are visible to the operating system, and they can run on different processors or cores.
- Kernel-level threads have the advantage of being able to utilize multiprocessor systems and being supported by the operating system, but they have the disadvantage of being slow and costly due to the context switching and system calls.