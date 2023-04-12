### Semaphore

- A semaphore is a synchronization object that can be used to control access to a shared resource by multiple tasks or processes.
- A semaphore has an internal variable that represents the state of the resource, such as available or busy.
- A semaphore can be binary or counting, depending on the number of resources it can manage.
- A binary semaphore can only manage one resource, and its state can be either 0 (taken) or 1 (free).
- A counting semaphore can manage multiple resources, and its state can be any non-negative integer value.
- A task or process can acquire a semaphore by calling a function that decrements the semaphore value, and release a semaphore by calling a function that increments the semaphore value.
- If a task or process tries to acquire a semaphore that is already taken, it will be blocked until the semaphore is released by another task or process.
- If a task or process tries to release a semaphore that is already free, it will cause an error or have no effect, depending on the implementation.

#### Semaphore in VxWorks

- VxWorks provides a semaphore API that supports binary, counting, and mutual exclusion (mutex) semaphores.
- A mutex semaphore is a special type of binary semaphore that can be used to protect a critical section of code from concurrent access by multiple tasks.
- A mutex semaphore has a priority inheritance mechanism that prevents priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a mutex.
- A semaphore in VxWorks is created by calling a function that specifies the type, the initial value, and the queueing order of the semaphore.
- For example, to create a counting semaphore with an initial value of 5 and a FIFO queueing order, the following code can be used:

```c
SEM_ID semShovels; // declare a semaphore ID
semShovels = semCCreate(SEM_Q_FIFO, 5); // create a counting semaphore
if (semShovels == NULL) {
  perror("semCCreate"); // handle error
}
```

- A semaphore in VxWorks is acquired by calling the `semTake` function, which takes the semaphore ID and a timeout value as arguments.
- The timeout value can be `WAIT_FOREVER` to block indefinitely, `NO_WAIT` to return immediately, or a positive number of ticks to wait for a specified time.
- For example, to acquire a semaphore with a timeout of 10 ticks, the following code can be used:

```c
STATUS status; // declare a status variable
status = semTake(semShovels, 10); // take a semaphore
if (status == OK) {
  // do something with the resource
} else {
  // handle error or timeout
}
```

- A semaphore in VxWorks is released by calling the `semGive` function, which takes the semaphore ID as an argument.
- For example, to release a semaphore, the following code can be used:

```c
STATUS status; // declare a status variable
status = semGive(semShovels); // give a semaphore
if (status == OK) {
  // do something else
} else {
  // handle error
}
```

- A semaphore in VxWorks is deleted by calling the `semDelete` function, which takes the semaphore ID as an argument.
- A semaphore should not be deleted if there are tasks blocked on it, as this may cause undefined behavior.
- For example, to delete a semaphore, the following code can be used:

```c
STATUS status; // declare a status variable
status = semDelete(semShovels); // delete a semaphore
if (status == OK) {
  // do something else
} else {
  // handle error
}
```

#### Semaphore in FreeRTOS

- FreeRTOS provides a semaphore API that supports binary, counting, and recursive semaphores.
- A recursive semaphore is a special type of mutex semaphore that can be acquired multiple times by the same task, as long as it is released the same number of times.
- A semaphore in FreeRTOS is built on top of a queue, which is a data structure that can store and transfer messages between tasks.
- A semaphore in FreeRTOS is created by calling a function that allocates memory for the semaphore and returns a handle to it.
- For example, to create a binary semaphore, the following code can be used:

```c
SemaphoreHandle_t xSemaphore = NULL; // declare a semaphore handle
xSemaphore = xSemaphoreCreateBinary(); // create a binary semaphore
if (

```
