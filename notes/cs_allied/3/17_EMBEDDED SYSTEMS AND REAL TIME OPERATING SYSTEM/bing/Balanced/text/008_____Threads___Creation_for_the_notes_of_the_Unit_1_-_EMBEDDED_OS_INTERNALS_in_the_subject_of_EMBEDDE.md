### Threads – Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread shares the same memory and resources as the program that created it, which enables multiple threads to collaborate and work efficiently within a single program.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the user-level program (user-level threads).
- Kernel-supported threads are more expensive to create and switch, but they can take advantage of multiple processors and have better support for blocking system calls and signals.
- User-level threads are cheaper to create and switch, but they cannot run on multiple processors and may be blocked by a system call or a signal in another thread.
- Some operating systems provide a hybrid approach that combines kernel-supported and user-level threads (e.g., Solaris).
- To create a thread, the program needs to specify the function or code segment that the thread will execute, as well as any arguments or parameters for the function.
- The operating system or the user-level library will allocate a thread control block (TCB) for the new thread, which contains information such as the thread ID, the thread state, the thread priority, the thread context (registers, stack, etc.), and any other thread-specific data.
- The operating system or the user-level library will also add the new thread to the ready list or the run queue, which are data structures that keep track of the threads that are ready to run or running on the processors.
- The operating system or the user-level library will then schedule the new thread to run on a processor, either by preempting another thread or by waiting for a processor to become idle.
- The operating system or the user-level library will also provide mechanisms to synchronize, communicate, and terminate threads.