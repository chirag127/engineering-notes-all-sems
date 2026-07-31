### Process and Thread

#### Process
- A process is an instance of a program in execution.
- It is a unit of execution that consists of instructions, data, and system resources.
- A process has its own address space, file descriptors, and security attributes.
- Processes can communicate with each other through inter-process communication mechanisms such as pipes, sockets, and shared memory.

#### Thread
- A thread is a unit of execution within a process.
- It shares the same address space, file descriptors, and security attributes as the process it belongs to.
- Multiple threads can exist within a single process, and they can execute concurrently.
- Threads can communicate with each other through shared variables and synchronization mechanisms such as mutexes and semaphores.

#### Relationship between Process and Thread
- A process can have multiple threads, but a thread can only belong to one process.
- Threads within the same process can share resources and data, while processes are isolated from each other.
- Creating a new thread is faster and requires fewer resources than creating a new process.
- The operating system schedules threads for execution, not processes. A process is considered to be executing if any of its threads are executing.

#### Usage in Object Oriented System Design
- In object-oriented system design, processes and threads can be used to implement concurrency and parallelism.
- Objects can be designed to be thread-safe, meaning that they can be accessed and modified by multiple threads concurrently without causing data corruption or race conditions.
- Processes and threads can also be used to implement distributed systems, where multiple processes running on different machines communicate with each other to achieve a common goal.