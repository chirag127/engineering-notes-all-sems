### Semaphores

- A semaphore is a variable or abstract data type used to control access to a common resource by multiple threads and avoid critical section problems in a concurrent system such as a multitasking operating system.
- A semaphore can be seen as a non-negative integer that represents the number of available resources or the number of permits to enter a critical section .
- A semaphore can be initialized to any non-negative value, depending on the number of resources or the maximum number of concurrent processes allowed .
- A semaphore supports two atomic operations: wait and signal .
  - Wait (S) or P: If the semaphore value is greater than 0, decrement the value. Otherwise, wait until the value is positive and then decrement it. This operation is used to acquire a resource or enter a critical section.
  - Signal (S) or V: Increment the value of semaphore. This operation is used to release a resource or exit a critical section.
- There are two main types of semaphores: counting semaphores and binary semaphores.
  - Counting semaphores: These semaphores can have any non-negative value and are used to manage a pool of resources or a buffer of items.
  - Binary semaphores: These semaphores can have only two values: 0 or 1. They are used to implement mutual exclusion or locks.
- Semaphores have some advantages and disadvantages.
  - Advantages: Semaphores allow only one process into the critical section. They follow the mutual exclusion principle. They can be used to solve various synchronization problems such as producer-consumer, readers-writers, dining philosophers, etc.
  - Disadvantages: Semaphores are prone to errors such as deadlock, starvation, priority inversion, busy waiting, etc. They require careful programming and debugging. They are not easy to understand and use.

: https://www.linkedin.com/pulse/semaphore-operating-system-os-solutions-bridge-international
: https://www.scaler.com/topics/operating-system/semaphore-in-os/
: https://byjus.com/gate/semaphores-in-operating-system-notes/
: https://www.tutorialspoint.com/semaphores-in-operating-system
: https://en.wikipedia.org/wiki/Semaphore_(programming)
: https://www.geeksforgeeks.org/semaphores-solutions-in-operating-system/