### Inter Process Communication – Semaphore

Inter-process communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions. The communication between these processes can be seen as a method of co-operation between them. Processes can communicate with each other through both shared memory and message passing.

Semaphores are counters which allow multiple threads to synchronize. Apart from synchronization semaphores, there exists an alternate implementation of semaphores referred to as process semaphores or system V semaphores which aid in interprocess communication.

To perform synchronization using semaphores, the following steps are taken:
1. Create a semaphore or connect to an already existing semaphore (semget())
2. Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
3. Perform control operations on the message queue (semctl())

Semaphores, shared memory, and internal message queues are common methods of interprocess communication. IPC is a method for two or more separate programs or processes to communicate with each other. This avoids using real disk-based files and the associated I/O overhead to pass information.