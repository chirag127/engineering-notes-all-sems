### Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS .
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- Some of the common IPC methods are  :
  - Shared memory: a region of memory that can be accessed by multiple processes.
  - Pipes: a unidirectional or bidirectional channel that can transfer data between processes.
  - Queues: a data structure that can store and retrieve data in a first-in first-out (FIFO) order.
  - Mailbox: a message buffer that can send and receive fixed-size messages between processes.
  - Signals: a notification mechanism that can interrupt a process and invoke a handler function.
  - Remote procedure calls: a method that can invoke a function in another process and return the result.
- Different open source RTOSes may have different implementations and APIs for IPC methods .
- For example, FreeRTOS supports queues, mailboxes, signals, and software timers as IPC methods.
- IPC methods may have different advantages and disadvantages in terms of performance, reliability, scalability, and complexity  .
- For example, shared memory is fast and simple, but it requires synchronization and protection mechanisms to avoid data corruption and race conditions.
- Pipes are easy to use and can handle large amounts of data, but they are limited by the buffer size and may cause blocking and deadlock.
- Queues are flexible and can handle variable-length messages, but they may consume more memory and CPU time than mailboxes.
- Mailboxes are efficient and can handle high-priority messages, but they may cause message loss or overwrite if the buffer is full.
- Signals are lightweight and can handle urgent events, but they may be unreliable and hard to debug.
- Remote procedure calls are powerful and can handle complex operations, but they may introduce network latency and security risks.