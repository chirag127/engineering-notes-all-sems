### Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS.
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- IPC can be implemented using different techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls.
- Shared memory is a technique where processes access a common memory region to exchange data.
- Pipes are unidirectional or bidirectional channels that allow processes to send and receive data in a stream.
- Queues are data structures that store data in a FIFO (first-in, first-out) order and allow processes to send and receive messages .
- Mailboxes are similar to queues, but they store only one message at a time and overwrite the previous message if a new one arrives.
- Signals are events that notify processes about the occurrence of a condition or a change in the system state.
- Remote procedure calls are a technique where processes invoke functions or procedures in another process and receive the results.

- Different open source RTOSes provide different IPC APIs and features. For example, FreeRTOS supports queues, binary semaphores, counting semaphores, recursive semaphores, mutexes, event groups, and software timers .
- IPC APIs can have different parameters, return values, and error codes depending on the RTOS implementation .
- IPC APIs can also have different performance, reliability, and security characteristics depending on the RTOS design .
- IPC APIs should be used carefully and correctly to avoid common problems, such as deadlock, starvation, priority inversion, buffer overflow, and data corruption .