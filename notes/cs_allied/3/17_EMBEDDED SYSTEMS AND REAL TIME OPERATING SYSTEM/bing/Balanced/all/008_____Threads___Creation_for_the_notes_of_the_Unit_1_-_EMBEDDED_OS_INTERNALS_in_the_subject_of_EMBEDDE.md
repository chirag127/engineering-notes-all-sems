# Threads - Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread is also known as a lightweight process that shares the same memory and resources as the program that created it.
- Threads can improve the performance and responsiveness of a program by dividing the workload among multiple execution units.
- Threads can also enable a program to take advantage of multiprocessor or multicore systems by running different threads on different cores or processors.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the program itself (user-level threads).
- The operating system provides system calls or APIs to create, terminate, suspend, resume, join, and synchronize threads.
- The program can also use libraries or frameworks that provide thread abstraction and management, such as POSIX threads (pthreads), Java threads, or Qt threads.
- The thread creation process involves allocating memory and resources for the thread, initializing the thread attributes and state, assigning a unique identifier and a priority to the thread, and adding the thread to the ready queue or the scheduler.
- The thread creation process may vary depending on the operating system, the programming language, and the thread library or framework used.
- The thread creation process may also involve specifying the function or the code segment that the thread will execute, the arguments or parameters that the thread will receive, and the options or flags that the thread will follow.
- The thread creation process may have some overhead or cost in terms of memory, CPU time, and system calls, which may affect the performance and scalability of the program.
- The thread creation process may also have some challenges or limitations in terms of security, portability, compatibility, and error handling, which may affect the reliability and robustness of the program.