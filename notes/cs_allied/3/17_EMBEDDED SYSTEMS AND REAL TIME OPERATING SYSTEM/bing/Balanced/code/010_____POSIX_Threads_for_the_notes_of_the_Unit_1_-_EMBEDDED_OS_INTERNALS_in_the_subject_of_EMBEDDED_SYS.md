### POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995) .
- A single process can contain multiple threads, all of which are executing the same program. Each thread has its own **stack**, **registers**, **thread ID**, **priority**, **signal mask**, and **errno** variable.
- Threads share the same **address space**, **heap**, **global variables**, **file descriptors**, and **signal handlers** as the process that created them.
- Threads can communicate with each other using **shared memory**, **message passing**, or **synchronization primitives** such as **mutexes**, **condition variables**, **semaphores**, and **barriers**.
- The pthreads API provides functions for creating, joining, detaching, canceling, and synchronizing threads, as well as setting and getting thread attributes .
- The pthreads API is implemented by various **libraries** for different operating systems, such as **libpthread** for Linux, **libc** for BSD, and **pthreadVC2** for Windows.