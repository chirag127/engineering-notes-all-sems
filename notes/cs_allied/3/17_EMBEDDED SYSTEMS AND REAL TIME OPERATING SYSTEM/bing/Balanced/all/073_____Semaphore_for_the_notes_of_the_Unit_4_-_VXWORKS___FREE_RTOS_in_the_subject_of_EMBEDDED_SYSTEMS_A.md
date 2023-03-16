# Semaphore for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A semaphore is a synchronization object that can be used to control access to a shared resource by multiple tasks or processes  .
- A semaphore has an internal variable that represents the state of the semaphore, such as available or taken .
- A semaphore can be binary or counting. A binary semaphore can only have two states: 0 or 1. A counting semaphore can have any non-negative integer value .
- A semaphore can be created, taken, given, and deleted using the FreeRTOS and VxWorks APIs   .
- A task can take a semaphore to gain access to a shared resource or to wait for a signal from another task. A task can give a semaphore to release the access to a shared resource or to send a signal to another task  .
- A task can block on a semaphore if the semaphore is not available when the task tries to take it. The task will be unblocked when the semaphore is given by another task  .
- A semaphore can have different queueing policies, such as FIFO or priority, to determine the order of unblocking the tasks that are waiting for the semaphore .
- A mutex is a special type of binary semaphore that can be used to implement mutual exclusion. A mutex can only be given by the task that took it. A mutex can also have a priority inheritance mechanism to prevent priority inversion  .
- A recursive mutex is a special type of mutex that can be taken multiple times by the same task. The task must give the mutex the same number of times as it took it before the mutex becomes available for other tasks.