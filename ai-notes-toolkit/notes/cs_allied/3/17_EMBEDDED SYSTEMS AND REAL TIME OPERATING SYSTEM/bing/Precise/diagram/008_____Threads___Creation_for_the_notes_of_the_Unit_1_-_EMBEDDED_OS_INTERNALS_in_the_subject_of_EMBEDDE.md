### Threads – Creation

- A thread is a lightweight unit of execution within a process.
- Threads share the same address space and resources of the process they belong to.
- Multiple threads can run concurrently within a process, allowing for parallel execution of tasks.
- Thread creation is faster and requires fewer resources than process creation.
- In most operating systems, threads can be created using system calls or library functions.
- The specific method for creating threads varies depending on the operating system and programming language being used.
- When a thread is created, it is assigned a unique thread identifier and a set of registers to store its execution state.
- The new thread can then begin executing a specified function or code block.
- The parent thread can continue executing concurrently with the new thread, or it can wait for the new thread to complete before resuming execution.
- Thread creation can improve the performance and responsiveness of an application by allowing multiple tasks to be performed simultaneously.
