# Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS .
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- IPC can be implemented using various techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls.
- Different open source RTOSes may offer different IPC APIs and features, depending on their design and architecture .
- One of the most popular open source RTOSes is FreeRTOS, which provides a rich set of IPC APIs, such as:
  - Binary and counting semaphores, which are used to synchronize tasks and share resources.
  - Mutexes, which are a special type of semaphore that provide priority inheritance and recursive locking.
  - Event groups, which are used to notify tasks of the occurrence of multiple events.
  - Message buffers, which are used to send and receive variable length messages between tasks or interrupts.
  - Stream buffers, which are used to send and receive streams of data between tasks or interrupts.
  - Notifications, which are used to send a single 32-bit value to a task or an interrupt.
  - Queues, which are used to send and receive fixed length messages between tasks or interrupts.
  - Queue sets, which are used to monitor multiple queues and semaphores for events.