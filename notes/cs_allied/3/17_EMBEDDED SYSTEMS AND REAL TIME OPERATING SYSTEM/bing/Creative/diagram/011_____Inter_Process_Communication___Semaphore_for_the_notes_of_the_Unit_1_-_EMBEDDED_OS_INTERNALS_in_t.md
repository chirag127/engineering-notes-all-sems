### Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions .
- IPC can be done through shared memory or message passing.
- A semaphore is a common method of IPC that uses a variable or abstract data type to control access to a common resource by multiple processes .
- A semaphore can be initialized to a non-negative integer value that represents the number of available resources or units of the resource.
- A semaphore supports two atomic operations: wait and signal.
- The wait operation decrements the semaphore value by one, if it is positive, or blocks the process until the semaphore value becomes positive.
- The signal operation increments the semaphore value by one, and wakes up any blocked process waiting on the semaphore.
- A semaphore can be used to implement mutual exclusion, where only one process can access a critical section at a time, or synchronization, where a process has to wait for another process to finish a task before proceeding.
- To perform synchronization using semaphores, the following are the steps:
  - Step 1: Create a semaphore or connect to an already existing semaphore (semget())
  - Step 2: Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
  - Step 3: Perform control operations on the semaphore (semctl())
- A semaphore can be binary (0 or 1) or counting (any non-negative integer).
- A binary semaphore can be used to implement a lock or a mutex, where only one process can enter a critical section at a time.
- A counting semaphore can be used to implement a bounded buffer or a producer-consumer problem, where a producer process can produce items and put them in a buffer, and a consumer process can consume items from the buffer, as long as the buffer is not full or empty.