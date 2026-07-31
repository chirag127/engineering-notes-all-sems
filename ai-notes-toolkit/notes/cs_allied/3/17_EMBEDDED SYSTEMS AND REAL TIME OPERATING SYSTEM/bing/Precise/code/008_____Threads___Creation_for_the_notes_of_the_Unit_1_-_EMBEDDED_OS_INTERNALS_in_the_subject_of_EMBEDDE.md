### Threads – Creation

- A thread is a lightweight, independent unit of execution within a process.
- Threads share the same address space and resources of the process they belong to, but have their own stack, program counter, and set of registers.
- Creating a new thread is faster and requires less memory than creating a new process.
- In most operating systems, threads can be created using a system call or library function.
- The function used to create a new thread typically takes a function pointer as an argument, which specifies the code that the new thread will execute.
- When a new thread is created, the operating system allocates the necessary resources and sets up the thread's context, including its stack and program counter.
- The new thread then begins executing the code specified by the function pointer passed to the thread creation function.
- Threads can be created in different states, such as running, ready, or blocked, depending on the requirements of the application.
- Once created, threads can be scheduled by the operating system to run concurrently with other threads within the same process or across different processes.