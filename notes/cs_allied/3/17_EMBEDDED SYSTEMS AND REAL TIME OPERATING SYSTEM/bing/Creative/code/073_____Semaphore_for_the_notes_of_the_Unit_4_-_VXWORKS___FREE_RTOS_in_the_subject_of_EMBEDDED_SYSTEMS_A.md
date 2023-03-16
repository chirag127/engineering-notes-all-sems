### Semaphore

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have a value of 0 or 1, indicating whether the resource is available or not.
- A semaphore can be used to implement mutual exclusion, synchronization, or signaling between tasks.
- A semaphore can be created, taken, and given using the FreeRTOS API functions.
- A semaphore can be given from an interrupt service routine (ISR) using a special function.

#### Types of semaphores

- Binary semaphore: A binary semaphore can only have two states: 0 or 1. It can be used to signal the availability of a resource or an event. A binary semaphore can be created using the `xSemaphoreCreateBinary()` function.
- Counting semaphore: A counting semaphore can have a value between 0 and a specified maximum. It can be used to track the number of available resources or the number of tasks waiting for an event. A counting semaphore can be created using the `xSemaphoreCreateCounting()` function.
- Mutex: A mutex is a special type of binary semaphore that can be used to implement mutual exclusion. A mutex can only be taken by one task at a time, and the same task must give it back. A mutex can also inherit the priority of the highest-priority task waiting for it, to prevent priority inversion. A mutex can be created using the `xSemaphoreCreateMutex()` function.
- Recursive mutex: A recursive mutex is a special type of mutex that can be taken multiple times by the same task, as long as it is given back the same number of times. A recursive mutex can be used to protect a critical section that can be nested. A recursive mutex can be created using the `xSemaphoreCreateRecursiveMutex()` function.

#### Semaphore operations

- Take: A task can take a semaphore using the `xSemaphoreTake()` function. This function will decrement the semaphore value by one, if it is positive, and block the task until the semaphore is available, if it is zero. The function can also specify a timeout period, after which the task will unblock and return a failure status. A recursive mutex can be taken using the `xSemaphoreTakeRecursive()` function, which will not block the task if it already owns the mutex.
- Give: A task can give a semaphore using the `xSemaphoreGive()` function. This function will increment the semaphore value by one, if it is less than the maximum, and unblock a waiting task, if any. A recursive mutex can be given using the `xSemaphoreGiveRecursive()` function, which will only release the mutex if the task has given it back as many times as it has taken it.
- Give from ISR: A semaphore can be given from an ISR using the `xSemaphoreGiveFromISR()` function. This function will increment the semaphore value by one, if it is less than the maximum, and unblock a waiting task, if any. The function will also return a flag indicating whether a context switch is required, to resume the unblocked task.

#### Semaphore implementation

- FreeRTOS implements semaphores using queues. A queue is a data structure that can store a fixed number of items in a first-in first-out (FIFO) order. A queue can be used to pass data or messages between tasks or ISRs.
- A binary semaphore is implemented as a queue with one item. The item can be either present or absent, indicating the semaphore value. A task can take the item from the queue, blocking if it is absent, and put it back into the queue, unblocking a waiting task, if any.
- A counting semaphore is implemented as a queue with multiple items. The number of items in the queue indicates the semaphore value. A task can take an item from the queue, blocking if it is empty, and put an item back into the queue, unblocking a waiting task, if any.
- A mutex is implemented as a binary semaphore with additional features. A mutex can store the handle of the task that owns it, and check if the task that tries to take or give it is the same. A mutex can also store the priority of the highest-priority task waiting for it, and temporarily raise the priority of the owner task, to prevent priority inversion.
- A recursive mutex is implemented as a mutex with additional features. A recursive mutex can store the number of times the owner task has taken