### POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same address space, file descriptors, stack, and other attributes, but have their own **thread ID**, **registers**, **stack pointer**, **errno**, and **signal mask**.
- Threads can communicate with each other using **shared memory**, **message passing**, or **synchronization primitives**.
- The POSIX thread libraries are a standards based thread API for **C/C++**.
- The POSIX thread libraries provide functions for creating, joining, detaching, canceling, and synchronizing threads.
- The POSIX thread libraries also provide functions for managing thread attributes, such as **priority**, **scheduling policy**, **stack size**, and **detach state**.
- The POSIX thread libraries use the prefix **pthread_** for all functions, types, and constants.
- The POSIX thread libraries are implemented as a **library** that can be linked with the application program.
- The POSIX thread libraries are most effective on **multi-processor** or **multi-core** systems where the threads can be scheduled to run on different processors or cores, thus gaining speed through parallel or distributed processing.