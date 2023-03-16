### Threads – Creation

1. A thread is a basic unit of CPU utilization, consisting of a program counter, a stack, and a set of registers.
2. Threads are created by the operating system to execute tasks concurrently within a process.
3. The process of creating a new thread involves allocating memory for the thread's stack and initializing the thread's context, including its program counter and registers.
4. The operating system then adds the new thread to the scheduler's queue of runnable threads.
5. The new thread begins executing when it is scheduled by the operating system.
6. The specific steps and system calls involved in creating a new thread vary depending on the operating system and programming language being used.
7. In some systems, threads can be created explicitly by the programmer using system calls or library functions, while in other systems, threads are created automatically by the operating system to improve performance.
8. Once a thread has been created, it can be managed using various thread management functions, such as setting its priority or suspending its execution.
