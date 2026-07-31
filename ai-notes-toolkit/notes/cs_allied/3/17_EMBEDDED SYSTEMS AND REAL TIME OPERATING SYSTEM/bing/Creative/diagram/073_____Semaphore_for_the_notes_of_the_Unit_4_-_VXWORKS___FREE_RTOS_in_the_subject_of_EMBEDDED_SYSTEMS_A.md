### Semaphore

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have a value of 0 or 1, indicating whether the resource is available or not.
- A semaphore can be used to implement mutual exclusion, synchronization, or signaling between threads or processes.
- A semaphore can be created, taken, and given using the FreeRTOS API functions.
- A semaphore can be given from an interrupt service routine using the xSemaphoreGiveFromISR() function.
- A semaphore can be either binary or counting, depending on the maximum value it can hold.
- A binary semaphore can only have a value of 0 or 1, and can be used to implement a lock or a signal.
- A counting semaphore can have a value from 0 to a specified maximum, and can be used to implement a resource pool or a barrier.
- A mutex is a special type of binary semaphore that supports priority inheritance and recursive locking.
- A mutex can be used to protect a critical section of code or data from concurrent access by multiple threads or processes.
- A mutex can be created, taken, and given using the FreeRTOS API functions.
- A mutex can be taken and given recursively by the same thread or process using the xSemaphoreTakeRecursive() and xSemaphoreGiveRecursive() functions.
- A mutex can be given from an interrupt service routine using the xSemaphoreGiveFromISR() function.
- FreeRTOS+POSIX provides a compatibility layer for using POSIX semaphore and mutex functions with FreeRTOS semaphores and mutexes.
- FreeRTOS+POSIX supports the following POSIX semaphore and mutex functions: sem_init(), sem_destroy(), sem_wait(), sem_trywait(), sem_post(), sem_getvalue(), pthread_mutex_init(), pthread_mutex_destroy(), pthread_mutex_lock(), pthread_mutex_trylock(), pthread_mutex_unlock(), pthread_mutex_getprioceiling(), pthread_mutex_setprioceiling(), pthread_mutexattr_init(), pthread_mutexattr_destroy(), pthread_mutexattr_getprioceiling(), pthread_mutexattr_setprioceiling(), pthread_mutexattr_getprotocol(), pthread_mutexattr_setprotocol(), pthread_mutexattr_gettype(), pthread_mutexattr_settype().
- FreeRTOS+POSIX does not support the following POSIX semaphore and mutex functions: sem_open(), sem_close(), sem_unlink(), sem_timedwait(), pthread_mutex_timedlock().