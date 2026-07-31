# Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions  .
- Processes can communicate with each other through both shared memory and message passing.
- Semaphores are counters which allow multiple threads or processes to synchronize by allocating or releasing resources .
- Semaphores can be used for both intra-process and inter-process communication.
- Semaphores can be implemented in two ways: binary semaphores and counting semaphores.
- Binary semaphores can have only two values: 0 or 1, and are used to implement mutual exclusion or critical sections.
- Counting semaphores can have any non-negative integer value, and are used to implement resource allocation or producer-consumer problems.
- To perform synchronization using semaphores, following are the steps:
  - Step 1: Create a semaphore or connect to an already existing semaphore (semget())
  - Step 2: Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
  - Step 3: Perform control operations on the semaphore i.e., set or get attributes or remove the semaphore (semctl())
- Semaphores are useful for inter-process communication because they provide a simple and efficient way of coordinating multiple processes that share common resources or data  .