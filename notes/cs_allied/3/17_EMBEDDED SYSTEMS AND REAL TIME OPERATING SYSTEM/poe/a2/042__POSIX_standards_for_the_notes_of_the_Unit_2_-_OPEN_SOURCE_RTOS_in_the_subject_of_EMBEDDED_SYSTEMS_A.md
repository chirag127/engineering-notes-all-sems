 Here are the notes on POSIX standards for Unit 2 - OPEN SOURCE RTOS in EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

### POSIX standards

- POSIX stands for Portable Operating System Interface. It is a family of standards specified by the IEEE for maintaining compatibility between operating systems.
- POSIX defines the application programming interfaces (API), along with command line shells and utility interfaces, for software compatibility with variants of Unix and other operating systems.
- The POSIX standards aim to enable software portability across POSIX-compliant operating systems. This is particularly important for embedded systems to enable the reuse of software components.
- Some key POSIX standards relevant to real-time operating systems are:

POSIX.1 - Core Services: This includes definitions for threads, mutexes, condition variables, semaphores, message passing, timers, and real-time signals.
POSIX.1b - Realtime Extensions: This adds real-time features to the POSIX.1 standard, including priority inheritance mutexes, priority ceiling mutexes, and scheduling policies.
POSIX.1c - Thread Execution Scheduling: This specifies thread scheduling interfaces and policies such as the SCHED_FIFO and SCHED_RR policies suitable for hard real-time systems.

- Many open source real-time operating systems such as FreeRTOS, μC/OS-II, and VxWorks implement these POSIX standards to varying degrees. This enables greater portability of applications across these RTOS options.
- Following the POSIX standards helps to enable software reuse and reduces the learning curve for developers when switching between different RTOS and processor options for embedded systems.