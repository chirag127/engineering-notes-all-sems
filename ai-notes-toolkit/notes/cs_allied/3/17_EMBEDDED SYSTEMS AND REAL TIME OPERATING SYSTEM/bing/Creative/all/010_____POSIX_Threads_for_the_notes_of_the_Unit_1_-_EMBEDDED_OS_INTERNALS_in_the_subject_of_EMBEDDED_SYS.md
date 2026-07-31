# POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same address space, file descriptors, stack, and other attributes, but have their own **thread ID**, **registers**, **stack pointer**, **priority**, and **return value**.
- Threads can communicate with each other using **shared memory**, **mutexes**, **condition variables**, and **semaphores** .
- Threads can be created, joined, detached, canceled, and synchronized using the functions provided by the pthreads API .
- The pthreads API consists of **functions**, **header files**, and **data types**.
- The functions have names that start with **pthread_**, such as `pthread_create`, `pthread_join`, `pthread_mutex_lock`, etc .
- The header files include **pthread.h**, which defines the functions, constants, and types for pthreads, and **sched.h**, which defines the scheduling policies and parameters.
- The data types include **pthread_t**, which represents a thread ID, **pthread_attr_t**, which represents a thread attribute object, **pthread_mutex_t**, which represents a mutex, **pthread_cond_t**, which represents a condition variable, and **pthread_key_t**, which represents a thread-specific data key .
- The pthreads API supports various features, such as **thread attributes**, **thread cancellation**, **thread cleanup**, **thread local storage**, **thread scheduling**, **thread signals**, and **thread synchronization** .
- The pthreads API is widely supported by various operating systems, such as **Linux**, **macOS**, **Windows**, and **RTOS**  .