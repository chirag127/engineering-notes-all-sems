# Inter Process Communication Models and Schemes

Inter process communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions. The communication between these processes can be seen as a method of co-operation between them. Processes can communicate with each other through different models and schemes, which have different advantages and disadvantages.

## Shared Memory Model

- Shared memory is the memory that can be simultaneously accessed by multiple processes. This is done so that the processes can communicate with each other by reading and writing data to the shared region.
- Shared memory can be implemented in two ways: system-wide shared memory and memory-mapped files.
- System-wide shared memory is a region of memory that is created by the operating system and can be accessed by any process that knows its identifier. The operating system provides functions to create, attach, detach, and remove shared memory segments.
- Memory-mapped files are files that are mapped into the address space of a process. The process can then access the file as if it were a part of its memory. The operating system ensures that the changes made to the file by one process are visible to other processes that have mapped the same file.
- The advantage of shared memory is that it is fast and efficient, as it does not involve copying data between processes or kernel intervention.
- The disadvantage of shared memory is that it requires synchronization mechanisms, such as semaphores or mutexes, to avoid race conditions and data inconsistency. It also poses security and reliability risks, as one process can corrupt or overwrite the data of another process.

## Message Passing Model

- Message passing is a method of communication where processes exchange messages with each other. A message is a unit of data that can contain any information that the sender and receiver agree upon.
- Message passing can be implemented in two ways: direct communication and indirect communication.
- Direct communication is a method where processes communicate with each other by explicitly specifying the identity of the sender and receiver. The operating system provides functions to send and receive messages between processes. The advantage of direct communication is that it is simple and straightforward. The disadvantage of direct communication is that it requires prior knowledge of the identity of the processes and it does not support dynamic and flexible communication patterns.
- Indirect communication is a method where processes communicate with each other through an intermediary entity, such as a mailbox or a message queue. The operating system provides functions to create, delete, send, and receive messages from mailboxes or message queues. The advantage of indirect communication is that it supports dynamic and flexible communication patterns, such as one-to-many, many-to-one, or many-to-many. The disadvantage of indirect communication is that it introduces additional overhead and complexity, as it involves an intermediary entity and kernel intervention.