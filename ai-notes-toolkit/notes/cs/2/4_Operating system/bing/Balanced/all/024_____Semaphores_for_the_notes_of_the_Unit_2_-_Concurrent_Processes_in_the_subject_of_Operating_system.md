# Semaphores

- A semaphore is a variable or abstract data type used to control access to a common resource by multiple threads and avoid critical section problems in a concurrent system such as a multitasking operating system.
- A semaphore can be seen as a non-negative integer that is used to solve the critical section problem by acting as a signal.
- A semaphore has two fields: a value S.V and a queue of processes S.L.
- A semaphore supports two atomic operations: wait and signal.
  - Wait (S) or P: If the semaphore value is greater than 0, decrement the value. Otherwise, wait until the value is positive and then decrement it.
  - Signal (S) or V: Increment the value of semaphore and wake up a process from the queue if it is not empty.
- There are two main types of semaphores: counting semaphores and binary semaphores.
  - Counting semaphores can have any non-negative value and are used to represent the number of available resources or slots.
  - Binary semaphores can have only two values: 0 or 1 and are used to implement mutual exclusion or locks.
- Advantages of semaphores:
  - Semaphores allow only one process into the critical section and follow the mutual exclusion principle.
  - Semaphores can be used to synchronize the actions of multiple tasks or threads.
  - Semaphores are simple and easy to implement.
- Disadvantages of semaphores:
  - Semaphores can cause deadlock if the processes do not release the resources or signal the semaphore.
  - Semaphores can cause priority inversion if a high-priority process is blocked by a low-priority process holding the semaphore.
  - Semaphores can cause busy waiting if the processes keep checking the semaphore value in a loop.