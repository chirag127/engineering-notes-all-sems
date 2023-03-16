### Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS .
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and dynamically.
- IPC can be implemented using different techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls .
- Shared memory is a technique where processes can access a common memory region to exchange data.
- Pipes are unidirectional or bidirectional channels that allow processes to send and receive data in a FIFO (first-in, first-out) manner.
- Queues are similar to pipes, but they can store multiple messages of different sizes and priorities .
- Mailboxes are special types of queues that can store only one message at a time.
- Signals are simple messages that notify processes about the occurrence of an event or a condition .
- Remote procedure calls are a technique where processes can invoke functions or methods on other processes, either locally or remotely.
- Different open source RTOSes, such as Bern RTOS, FreeRTOS, Zephyr, and NuttX, provide various IPC APIs and mechanisms to support different application scenarios and requirements   .
- IPC APIs and mechanisms may vary in terms of performance, reliability, scalability, and complexity depending on the RTOS design and implementation .
- IPC is a key component of RTOS that enables inter-process synchronization, coordination, and communication   .