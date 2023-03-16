### Threads – Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread shares the same memory and resources as the program that created it, which enables multiple threads to collaborate and work efficiently within a single program.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the user-level program (user-level threads).
- Kernel-supported threads are supported by the operating system, which stores multiple thread control blocks (TCBs) per process and is involved in dispatching and switching between threads (even between threads in the same process).
- User-level threads are created and managed by the user-level program, which uses its own data structures and libraries to implement threads without involving the kernel.
- Some operating systems, such as Windows, MacOS X, Linux, and some embedded operating systems, provide a hybrid approach that combines kernel-supported and user-level threads, such as the POSIX threads (pthreads) library.
- To create a thread, the program needs to specify the function or code segment that the thread will execute, as well as any parameters or arguments that the thread needs.
- The operating system or the user-level library will then allocate a stack and a TCB for the new thread, and add it to the ready list of threads that are waiting to run.
- The operating system or the user-level library will also assign a unique identifier to the new thread, which can be used to refer to the thread later.
- The operating system or the user-level library will then schedule the new thread to run on an available processor or core, or preempt an existing thread to make room for the new thread.
- The thread will start executing the specified function or code segment, and will terminate when the function returns or when the thread explicitly calls a termination function.