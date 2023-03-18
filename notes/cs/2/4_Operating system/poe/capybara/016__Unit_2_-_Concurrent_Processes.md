## Unit 2 - Concurrent Processes

Concurrent processes are a crucial concept in computer science. They allow multiple tasks to be executed simultaneously, improving the efficiency of the system. Here are some important points to keep in mind when studying concurrent processes:

- **What is a concurrent process?** A concurrent process is a process that executes multiple tasks simultaneously. These tasks can be independent, or they may need to communicate with each other.

- **What is a thread?** A thread is a lightweight process that shares memory and other resources with its parent process. Multiple threads can be executed within a single process, allowing for even greater concurrency.

- **What is a race condition?** A race condition occurs when two or more processes or threads access a shared resource in an unpredictable order, leading to unexpected results. Proper synchronization techniques must be used to prevent race conditions.

- **What is a deadlock?** A deadlock occurs when two or more processes or threads are waiting for each other to release a resource, and none of them can proceed. Deadlocks can be prevented by careful design of the system and the use of appropriate synchronization techniques.

- **What is a semaphore?** A semaphore is a synchronization object that can be used to control access to a shared resource. It provides a way for processes or threads to signal each other and avoid race conditions.

- **What is a mutex?** A mutex is a type of semaphore that is used to provide exclusive access to a shared resource. Only one process or thread can hold a mutex at a time, preventing race conditions.

- **What is a monitor?** A monitor is a synchronization construct that allows multiple processes or threads to access a shared resource in a controlled manner. Monitors are typically implemented using a mutex and a condition variable.

- **What is a condition variable?** A condition variable is a synchronization object that allows processes or threads to wait for a specific condition to be met before proceeding. It is typically used in conjunction with a mutex to provide safe access to a shared resource.

In conclusion, understanding concurrent processes is essential for developing efficient and reliable software systems. By studying the concepts outlined above, you will be well on your way to mastering this important topic.