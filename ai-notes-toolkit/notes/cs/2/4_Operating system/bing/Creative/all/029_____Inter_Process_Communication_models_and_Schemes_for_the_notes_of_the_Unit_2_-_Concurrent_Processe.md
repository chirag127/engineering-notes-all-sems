# Inter Process Communication Models and Schemes

Inter process communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions. The communication between these processes can be seen as a method of co-operation between them.

There are two primary models of inter process communication: shared memory and message passing .

## Shared Memory Model

Shared memory is the memory that can be simultaneously accessed by multiple processes. This is done so that the processes can communicate with each other. All POSIX systems, as well as Windows operating systems use shared memory.

Advantages of Shared Memory Model:

- It is fast and efficient, as no kernel involvement is required for the communication.
- It allows complex data structures to be shared easily.

Disadvantages of Shared Memory Model:

- It requires synchronization mechanisms to avoid race conditions and data inconsistency.
- It is not scalable, as the number of processes increases the size of the shared memory region also increases.
- It is not portable, as different operating systems have different implementations of shared memory.

## Message Passing Model

Message passing is a mechanism where processes exchange data and information by sending and receiving messages. The messages can be sent either directly or indirectly through a common mailbox or a message queue.

Advantages of Message Passing Model:

- It is easier to implement and use, as the processes do not need to share any memory space.
- It is scalable, as the number of processes does not affect the communication performance.
- It is portable, as the message passing interface is standardized and supported by most operating systems.

Disadvantages of Message Passing Model:

- It is slower and less efficient, as the messages need to be copied and transferred through the kernel.
- It requires more memory space and CPU time, as each message has a header and a body.
- It is difficult to handle complex data structures, as the messages need to be serialized and deserialized.