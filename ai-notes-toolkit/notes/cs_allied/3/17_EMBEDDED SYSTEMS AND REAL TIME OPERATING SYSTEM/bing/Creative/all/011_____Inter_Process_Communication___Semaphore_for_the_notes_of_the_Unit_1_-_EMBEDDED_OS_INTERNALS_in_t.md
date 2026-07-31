# Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions.
- Processes can communicate with each other through both shared memory and message passing.
- Semaphores are counters which allow multiple threads or processes to synchronize by allocating or releasing resources .
- Semaphores can be either binary (0 or 1) or counting (any non-negative integer).
- Semaphores can be implemented in two ways: synchronization semaphores and process semaphores.
- Synchronization semaphores are used to coordinate the access of shared resources among threads within a single process.
- Process semaphores or system V semaphores are used to coordinate the access of shared resources among processes.
- Process semaphores are created and managed by the operating system.
- To perform synchronization using process semaphores, the following steps are required:
  - Create a semaphore or connect to an already existing semaphore using `semget()` system call.
  - Perform operations on the semaphore such as allocate, release, or wait for the resources using `semop()` system call.
  - Perform control operations on the semaphore such as set or get its value, permissions, or status using `semctl()` system call.
- Process semaphores can be used to implement mutual exclusion, producer-consumer, and reader-writer problems.