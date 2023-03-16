### POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995) .
- A single process can contain multiple threads, all of which are executing the same program. Each thread has its own **stack**, **registers**, **thread ID**, **priority**, and **return value**.
- Threads share the same **address space**, **heap**, **file descriptors**, and **signal handlers** as the process that created them.
- Threads can communicate with each other using **shared variables**, **mutexes**, **condition variables**, and **semaphores**.
- Threads can be created, joined, detached, canceled, and synchronized using the functions defined in the **pthread.h** header file.
- Some of the common functions are:

  - `pthread_create`: creates a new thread and returns its ID.
  - `pthread_join`: waits for a thread to terminate and returns its exit status.
  - `pthread_detach`: marks a thread as detached, meaning that it will release its resources when it terminates without requiring a join.
  - `pthread_cancel`: requests the cancellation of a thread.
  - `pthread_exit`: terminates the calling thread and returns a value to the joiner.
  - `pthread_self`: returns the ID of the calling thread.
  - `pthread_mutex_init`: initializes a mutex object.
  - `pthread_mutex_lock`: locks a mutex object, blocking if it is already locked by another thread.
  - `pthread_mutex_unlock`: unlocks a mutex object.
  - `pthread_mutex_destroy`: destroys a mutex object.
  - `pthread_cond_init`: initializes a condition variable object.
  - `pthread_cond_wait`: blocks on a condition variable until it is signaled by another thread.
  - `pthread_cond_signal`: signals one thread waiting on a condition variable.
  - `pthread_cond_broadcast`: signals all threads waiting on a condition variable.
  - `pthread_cond_destroy`: destroys a condition variable object.
  - `pthread_sem_init`: initializes a semaphore object.
  - `pthread_sem_wait`: decrements a semaphore object, blocking if it is zero.
  - `pthread_sem_post`: increments a semaphore object, waking up a waiting thread if any.
  - `pthread_sem_destroy`: destroys a semaphore object.

- POSIX Threads is a portable and widely used standard for threaded programming in C/C++. It is supported by most operating systems, including Linux, Windows, macOS, and embedded systems .