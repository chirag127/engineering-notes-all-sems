### Process and Thread

- A **process** is an instance of a program that is being executed. It contains the program code and its current activity.
- A process is made up of multiple threads of execution that execute instructions concurrently.
- A **thread** is the smallest unit of processing that can be scheduled by an operating system.
- Threads exist within a process and share the same resources, such as memory and open files, as other threads within the same process.
- Each thread has its own program counter, stack, and set of registers.
- Threads can communicate with each other through shared memory or by using message passing.
- The use of threads can improve the performance of a program by allowing multiple tasks to be performed concurrently.
- Multithreading can be implemented at the user level or the kernel level.
- User-level threads are managed by a user-level library and the kernel is not aware of their existence.
- Kernel-level threads are managed by the operating system and are scheduled by the kernel.
- The use of threads can also improve the responsiveness of a program by allowing long-running tasks to be performed in the background while the user interface remains responsive.
