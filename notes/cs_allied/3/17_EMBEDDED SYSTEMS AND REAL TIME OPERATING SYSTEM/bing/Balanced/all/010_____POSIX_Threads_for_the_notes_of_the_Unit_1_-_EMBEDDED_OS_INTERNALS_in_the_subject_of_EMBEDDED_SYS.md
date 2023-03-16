# POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same address space, file descriptors, stack, and other attributes, but have their own **thread ID**, **registers**, **stack pointer**, **priority**, **signal mask**, and **errno** variable.
- Threads can communicate with each other using **shared memory**, **mutexes**, **condition variables**, and **semaphores**.
- Threads can be created, joined, detached, canceled, and synchronized using the functions defined in the **pthread.h** header file.
- POSIX also defines a standard threading library API which is supported by most modern operating systems.