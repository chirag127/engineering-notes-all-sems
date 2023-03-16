# Intertask Communication

- Intertask communication is the process of exchanging data or signals between tasks or threads in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources, data or events.
- Intertask communication can also be used to implement task synchronization and mutual exclusion, which are mechanisms to ensure the correct and consistent execution of tasks in a concurrent system.
- Different RTOSs may provide different methods or primitives for intertask communication, such as shared memory, message queues, pipes, semaphores, mutexes, events, signals, etc.
- In this unit, we will focus on two popular RTOSs: VxWorks and FreeRTOS, and compare their intertask communication methods and performance.

## VxWorks Intertask Communication

- VxWorks is a commercial RTOS developed by Wind River Systems, widely used in embedded systems such as aerospace, defense, industrial and automotive applications.
- VxWorks supports several methods for intertask communication , such as:

  - **Shared memory**: A region of memory that can be accessed by multiple tasks. Shared memory is the fastest and simplest way of intertask communication, but it requires explicit synchronization and mutual exclusion mechanisms to avoid data corruption or inconsistency. VxWorks provides semaphores, mutexes and spin locks for this purpose.
  - **Message queues**: A data structure that stores messages in a FIFO (first-in, first-out) order. Message queues allow tasks to send and receive messages of fixed or variable size, with optional priority and timeout parameters. Message queues are thread-safe and can be used for both synchronous and asynchronous communication. VxWorks provides the msgQ API for creating and manipulating message queues.
  - **Pipes**: A special type of message queue that can be accessed by tasks using standard I/O functions, such as read and write. Pipes are useful for transferring streams of data between tasks, such as audio or video data. VxWorks provides the pipeDev API for creating and manipulating pipes.
  - **Events**: A mechanism that allows tasks to signal or wait for the occurrence of one or more events. Events are represented by bits in a 32-bit or 64-bit event flag. Tasks can set, clear, send, receive or test event flags using the eventLib API. Events can be used for both synchronous and asynchronous communication, and can also be triggered by interrupts or timers.
  - **Signals**: A mechanism that allows tasks to send or receive signals, which are predefined integers that represent various types of events or conditions. Signals are similar to events, but they are handled by the task's signal handler function, which can perform actions such as terminating the task, suspending the task, or ignoring the signal. VxWorks provides the sigLib API for creating and manipulating signals.

## FreeRTOS Intertask Communication

- FreeRTOS is a free and open source RTOS developed by Real Time Engineers Ltd, widely used in embedded systems such as microcontrollers, IoT devices, and low-power applications.
- FreeRTOS was designed to have a small ROM footprint and high portability. To this end, all intertask communication mechanisms are built around a single queue primitive , such as:

  - **Queues**: A data structure that stores items in a FIFO order. Queues allow tasks to send and receive items of fixed size, with optional priority and timeout parameters. Queues are thread-safe and can be used for both synchronous and asynchronous communication. FreeRTOS provides the xQueue API for creating and manipulating queues.
  - **Mutexes**: A special type of queue that can be used to implement mutual exclusion between tasks that share a resource. Mutexes are similar to binary semaphores, but they have additional features such as priority inheritance and recursive locking. FreeRTOS provides the xSemaphore API for creating and manipulating mutexes.
  - **Binary semaphores**: A special type of queue that can be used to implement synchronization between tasks or between tasks and interrupts. Binary semaphores have only two states: available or taken. Tasks can take or give binary semaphores using the xSemaphore API. Binary semaphores can also be used as binary flags or signals.
  - **Counting semaphores**: A special type of queue that can be used to implement synchronization between tasks or between tasks and interrupts. Counting semaphores have a positive integer value that represents the number of available resources or events. Tasks can take or give counting semaphores using the xSemaphore API. Counting semaphores can also be used as