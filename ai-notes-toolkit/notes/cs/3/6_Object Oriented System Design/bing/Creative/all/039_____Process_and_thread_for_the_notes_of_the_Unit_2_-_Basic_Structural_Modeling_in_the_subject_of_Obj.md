# Process and Thread

- A **process** is an independent sequence of execution that runs in its own memory space . A process can have one or more threads, which are units of execution within a process .
- A **thread** is a segment of a process that can execute concurrently with other threads of the same process or different processes . A thread shares the memory and resources of its parent process, but has its own stack, program counter, and registers.
- In object-oriented system design, a process can be seen as a collection of objects that communicate with each other through messages. A thread can be seen as an active object that has its own state and behavior, and can initiate or respond to messages.
- Some of the advantages of using threads are:
  - They can improve the performance and responsiveness of a process by utilizing multiple cores or processors .
  - They can simplify the design and implementation of concurrent and distributed systems by providing a higher level of abstraction .
  - They can reduce the overhead of creating and destroying processes, as well as the context switching time between them .
- Some of the challenges of using threads are:
  - They can introduce complexity and errors in the synchronization and coordination of shared data and resources .
  - They can increase the risk of deadlock, livelock, race condition, and starvation problems .
  - They can be difficult to debug and test, as the behavior and outcome of a thread may depend on the timing and order of execution .

: Process vs Thread: What's the Difference? - javatpoint
: Process vs Thread – Difference Between Them - Guru99
: OOAD - Object Oriented Principles - tutorialspoint.com
: Difference between Process and Thread - GeeksforGeeks