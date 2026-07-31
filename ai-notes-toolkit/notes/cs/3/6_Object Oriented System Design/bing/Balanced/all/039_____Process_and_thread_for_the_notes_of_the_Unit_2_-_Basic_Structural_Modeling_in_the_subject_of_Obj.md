# Process and Thread

- A **process** is an independent sequence of execution that runs in its own memory space . A process can have one or more threads, which are units of execution within a process .
- A **thread** is a segment of a process that can execute concurrently with other threads of the same process or different processes . A thread shares the memory and resources of its parent process, but has its own stack, program counter, and registers.
- In object-oriented system design, there are two types of objects: **active** and **inactive**. Active objects have their own threads of control and can communicate and synchronize with other active or inactive objects. Inactive objects do not have their own threads of control and can only respond to requests from active objects.
- An example of an active object is a timer that periodically sends signals to other objects. An example of an inactive object is a bank account that can only perform operations when requested by a customer or a teller object.
- The advantages of using threads in object-oriented system design are:
  - Threads can improve the performance and responsiveness of a system by utilizing the parallelism of multicore processors .
  - Threads can simplify the design and implementation of concurrent and distributed systems by allowing objects to interact asynchronously and independently .
  - Threads can reduce the overhead of creating and destroying processes, as well as the context switching time between processes .
- The challenges of using threads in object-oriented system design are:
  - Threads can introduce complexity and errors in the system due to synchronization, deadlock, race condition, and memory consistency issues .
  - Threads can increase the testing and debugging difficulty of the system due to the nondeterministic and unpredictable behavior of concurrent threads .
  - Threads can require more careful and rigorous design and coding practices to ensure the correctness, reliability, and maintainability of the system .