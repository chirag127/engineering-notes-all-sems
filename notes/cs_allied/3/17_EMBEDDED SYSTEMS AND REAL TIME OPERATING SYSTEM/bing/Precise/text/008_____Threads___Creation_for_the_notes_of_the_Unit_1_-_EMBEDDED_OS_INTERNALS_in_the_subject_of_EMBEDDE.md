### Threads – Creation

1. A thread is a basic unit of CPU utilization, consisting of a program counter, a stack, and a set of registers.
2. Threads are created by the operating system to execute tasks concurrently within a process.
3. The process of creating a new thread involves allocating memory for the thread's stack and initializing the thread's context, including its program counter and registers.
4. The operating system then adds the new thread to the scheduler's queue of runnable threads.
5. The new thread becomes eligible for execution once it is in the scheduler's queue.
6. The operating system may provide system calls or library functions for creating new threads, such as `pthread_create` in the POSIX threads library.
7. When a thread is created, it shares the address space and resources of the process that created it.
8. This allows threads to communicate and share data with each other more easily than if they were separate processes.
