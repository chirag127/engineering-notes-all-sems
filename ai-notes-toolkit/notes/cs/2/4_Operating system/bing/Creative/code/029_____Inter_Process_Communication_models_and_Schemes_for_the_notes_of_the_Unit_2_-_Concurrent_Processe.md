# Inter Process Communication models and Schemes

Inter process communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions without sharing the same address space. IPC can be classified into two models: shared memory and message passing.

## Shared Memory Model

Shared memory is the memory that can be simultaneously accessed by multiple processes. This is done so that the processes can communicate with each other by reading and writing data to the shared region. The operating system provides mechanisms to create, manage and protect the shared memory segments. The advantages of shared memory are:

- It is fast and efficient, as no data copying is required.
- It allows complex data structures to be shared easily.

The disadvantages of shared memory are:

- It requires synchronization and mutual exclusion mechanisms to avoid race conditions and data inconsistency.
- It is not scalable, as the number of processes and the size of shared memory increase.

## Message Passing Model

Message passing provides a mechanism to allow processes to communicate and to synchronize their actions by exchanging messages. The messages can be either fixed-sized or variable-sized, and can be sent either synchronously or asynchronously. The operating system provides mechanisms to create, send, receive and delete messages. The advantages of message passing are:

- It is simple and easy to implement, as no shared data structures are required.
- It is scalable, as the number of processes and the size of messages can vary.

The disadvantages of message passing are:

- It is slow and inefficient, as data copying and context switching are required.
- It is difficult to handle complex data structures and large messages.

## IPC Schemes

There are various IPC schemes that are based on either shared memory or message passing models, or a combination of both. Some of the common IPC schemes are:

- Pipes: Pipes are a form of message passing that allow one-way or two-way communication between processes using a special file. Pipes can be either named or unnamed, and can be either blocking or non-blocking.
- Sockets: Sockets are a form of message passing that allow bidirectional communication between processes using network protocols. Sockets can be either stream-oriented or datagram-oriented, and can be either connection-oriented or connectionless.
- Semaphores: Semaphores are a form of shared memory that allow processes to synchronize their actions by using integer variables. Semaphores can be either binary or counting, and can be either local or global.
- Shared memory: Shared memory is a form of shared memory that allows processes to access a common memory region directly. Shared memory can be either anonymous or mapped, and can be either read-only or read-write.
- Message queues: Message queues are a form of message passing that allow processes to exchange messages using a queue data structure. Message queues can be either persistent or transient, and can be either blocking or non-blocking.
- Signals: Signals are a form of message passing that allow processes to send notifications or requests to other processes using predefined integers. Signals can be either standard or real-time, and can be either ignored, handled or blocked.