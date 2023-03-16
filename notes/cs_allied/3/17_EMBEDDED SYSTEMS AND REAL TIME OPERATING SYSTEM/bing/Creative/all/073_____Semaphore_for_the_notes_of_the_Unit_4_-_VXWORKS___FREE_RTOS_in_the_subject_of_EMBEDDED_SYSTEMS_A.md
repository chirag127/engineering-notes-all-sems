# Semaphore for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have two states: available or unavailable. A thread or process can acquire a semaphore if it is available, and release it when it is done with the shared resource.
- A semaphore can be binary or counting. A binary semaphore can only have two values: 0 or 1. A counting semaphore can have any non-negative value, and it represents the number of available resources.
- In FreeRTOS, semaphores are built on queues. A queue is a data structure that stores items in a first-in, first-out (FIFO) order. A queue can be used to pass messages or data between tasks, or to synchronize tasks.
- A semaphore is implemented as a queue with a length of one. The queue item is either empty or full, corresponding to the semaphore state. A task can acquire a semaphore by receiving an item from the queue, and release a semaphore by sending an item to the queue.
- FreeRTOS provides several API functions to create and manipulate semaphores. Some of the most common ones are:

  - `xSemaphoreCreateBinary()` creates a binary semaphore and returns a handle to it.
  - `xSemaphoreTake()` tries to acquire a semaphore by receiving an item from the queue. It can block the calling task until the semaphore is available or a timeout expires.
  - `xSemaphoreGive()` releases a semaphore by sending an item to the queue. It can unblock a task that is waiting for the semaphore.
  - `xSemaphoreGiveFromISR()` is a special version of `xSemaphoreGive()` that can be called from an interrupt service routine (ISR). It can also trigger a context switch if a higher priority task is unblocked by the semaphore.

- A mutex is a special type of binary semaphore that can be used to implement mutual exclusion. Mutual exclusion means that only one task can access a shared resource at a time, and other tasks have to wait until the resource is released.
- A mutex has two additional features compared to a binary semaphore:

  - A mutex has a priority inheritance mechanism that can prevent priority inversion. Priority inversion occurs when a higher priority task is blocked by a lower priority task that holds a mutex. The priority inheritance mechanism temporarily boosts the priority of the lower priority task to match the highest priority task that is waiting for the mutex.
  - A mutex can be recursive, meaning that the same task can acquire the same mutex multiple times without blocking itself. The task has to release the mutex the same number of times it acquired it before the mutex is available to other tasks.

- FreeRTOS provides several API functions to create and manipulate mutexes. Some of the most common ones are:

  - `xSemaphoreCreateMutex()` creates a mutex and returns a handle to it.
  - `xSemaphoreCreateRecursiveMutex()` creates a recursive mutex and returns a handle to it.
  - `xSemaphoreTakeRecursive()` tries to acquire a recursive mutex by receiving an item from the queue. It can block the calling task until the mutex is available or a timeout expires.
  - `xSemaphoreGiveRecursive()` releases a recursive mutex by sending an item to the queue. It can unblock a task that is waiting for the mutex.

- In VXWorks, semaphores are also used to synchronize and protect access to shared resources. VXWorks provides several types of semaphores, such as binary, counting, mutual exclusion, and reader-writer semaphores.
- VXWorks also provides several API functions to create and manipulate semaphores. Some of the most common ones are:

  - `semBCreate()` creates a binary semaphore and returns an ID to it.
  - `semCCreate()` creates a counting semaphore and returns an ID to it.
  - `semMCreate()` creates a mutual exclusion semaphore and returns an ID to it.
  - `semTake()` tries to acquire a semaphore by decrementing its value. It can block the calling task until the semaphore is positive or a timeout expires.
  - `semGive()` releases a semaphore by incrementing its value. It can unblock a task that