### Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions  .
- IPC can be achieved through both shared memory and message passing methods.
- A semaphore is a common method of IPC that uses a variable or abstract data type to control access to a common resource by multiple processes  .
- A semaphore can be initialized to a non-negative integer value that represents the number of available resources or units of the resource.
- A semaphore supports two atomic operations: wait and signal.
- The wait operation decrements the semaphore value by one, if it is positive, or blocks the process until the semaphore value becomes positive.
- The signal operation increments the semaphore value by one, and wakes up a blocked process if any.
- A semaphore can be used to implement mutual exclusion, synchronization, and deadlock prevention among processes.
- To perform synchronization using semaphores, the following steps are required:
  - Create a semaphore or connect to an already existing semaphore (semget())
  - Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
  - Perform control operations on the semaphore (semctl())
- A semaphore can be either binary or counting, depending on whether it can take only two values (0 and 1) or any non-negative integer value.
- A binary semaphore can be used to implement a lock or a mutex, while a counting semaphore can be used to implement a bounded buffer or a producer-consumer problem.