# Intertask Communication for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Intertask communication is the process of exchanging data or signals between tasks in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources, data or events.
- Intertask communication can also be used to implement concurrency, parallelism, synchronization and mutual exclusion in a multitasking system.
- VXWORKS and FREE RTOS are two popular RTOS that support various methods of intertask communication.

## VXWORKS Intertask Communication

- VXWORKS supports several different methods for intertask communication . They are:
  - Shared memory: Tasks can access a common memory region to read or write data. Shared memory is fast and simple, but requires explicit synchronization and mutual exclusion mechanisms to avoid data corruption or inconsistency.
  - Message queues: Tasks can send and receive messages of fixed or variable size through message queues. Message queues are thread-safe and can be used to communicate between user space and kernel space tasks. Message queues can also be used to implement priority inheritance and priority ceiling protocols to avoid priority inversion.
  - Pipes: Tasks can send and receive data streams through pipes. Pipes are similar to message queues, but they do not preserve message boundaries. Pipes are useful for transferring large amounts of data or binary data.
  - Signals: Tasks can send and receive signals to notify each other of events or conditions. Signals are asynchronous and can interrupt the execution of the receiving task. Signals can also be used to implement timers, alarms or exceptions.

## FREE RTOS Intertask Communication

- FREE RTOS can easily be extended to include other intertask communication mechanisms in the same manner. As all communication mechanisms are based on the same underlying queue concept, the API functions provided for each mechanism are in fact relatively interoperable. The intertask communication methods supported by FREE RTOS are:
  - Queues: Queues are the primary form of intertask communication in FREE RTOS. They can be used to send messages between tasks, and between interrupts and tasks. Queues are thread-safe and can be used to implement blocking or non-blocking communication. Queues can also be used to implement semaphores and mutexes.
  - Semaphores: Semaphores are a special type of queue that can be used to synchronize or coordinate the execution of tasks. Semaphores can be binary or counting, depending on the number of resources or events they represent. Semaphores can also be used to implement mutual exclusion or critical sections.
  - Mutexes: Mutexes are a special type of binary semaphore that can be used to protect shared resources or data from concurrent access by multiple tasks. Mutexes can also be used to implement priority inheritance and priority ceiling protocols to avoid priority inversion. Mutexes can also be recursive, allowing a task to take the same mutex multiple times.