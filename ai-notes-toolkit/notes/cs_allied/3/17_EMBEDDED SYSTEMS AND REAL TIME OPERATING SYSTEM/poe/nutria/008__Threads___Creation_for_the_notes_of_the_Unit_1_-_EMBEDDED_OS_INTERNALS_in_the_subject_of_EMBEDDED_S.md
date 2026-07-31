
### Threads - Creation

- A thread is a lightweight process that is used to execute a single task. 
- Threads are created within a process and share the same address space, allowing them to access the same resources.
- Threads can be created using the `pthread_create()` function, which requires the specification of a thread routine and a set of attributes. 
- The attributes of a thread can be specified using the `pthread_attr_t` structure, which includes the scheduling policy, stack size, and priority. 
- Threads can be scheduled using one of the following policies: FIFO, Round Robin, or other. 
- Threads can be synchronized using mutexes, semaphores, or other synchronization primitives. 
- Threads can be terminated using the `pthread_exit()` function or by returning from the thread routine. 
- Threads can be suspended and resumed using the `pthread_suspend()` and `pthread_resume()` functions.