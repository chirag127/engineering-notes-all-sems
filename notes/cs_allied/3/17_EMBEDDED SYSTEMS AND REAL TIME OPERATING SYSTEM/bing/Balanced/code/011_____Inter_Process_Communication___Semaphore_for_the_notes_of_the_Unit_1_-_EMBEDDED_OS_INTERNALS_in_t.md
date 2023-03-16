### Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions.
- IPC can be achieved through two methods: shared memory and message passing.
- Shared memory allows processes to access a common memory region for reading and writing data.
- Message passing allows processes to exchange messages through a communication channel such as a queue, a pipe, or a socket.
- A semaphore is a special type of IPC that uses a counter to control access to a shared resource by multiple processes.
- A semaphore can be initialized to a positive integer value that represents the number of available units of the resource.
- A process that wants to use the resource must perform a wait operation on the semaphore, which decrements the counter by one.
- If the counter is zero or negative, the process is blocked until another process releases the resource by performing a signal operation on the semaphore, which increments the counter by one.
- A semaphore can be used to implement mutual exclusion, synchronization, and deadlock prevention among processes.
- There are two types of semaphores: binary and counting.
- A binary semaphore can only have two values: 0 or 1, and is used to implement mutual exclusion.
- A counting semaphore can have any non-negative value, and is used to implement synchronization.
- Semaphores can be implemented in different ways, such as using atomic instructions, busy waiting, or blocking queues.
- Semaphores can also be classified as local or global, depending on whether they are shared by processes within the same address space or across different address spaces.
- Semaphores can be created, accessed, and manipulated using system calls such as semget, semop, and semctl.