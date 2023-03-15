# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for an RTOS, correct timing is the key feature.
- UNIX is not designed as an RTOS, but it can be modified to support some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one.
  - Priority inheritance: the mechanism to avoid priority inversion, where a low priority process blocks a high priority one.
  - Real-time signals: the signals that are delivered immediately and have a fixed number of predefined handlers.
  - POSIX real-time extensions: the set of standards that define interfaces and behavior for real-time applications on UNIX-like systems.
- However, UNIX still has some limitations that prevent it from being a fully-fledged RTOS, such as:
  - Non-deterministic system calls: the system calls that may take an unpredictable amount of time to complete, such as memory allocation, file I/O, or network communication.
  - Non-real-time kernel: the kernel that may perform some operations that are not time-critical, such as garbage collection, swapping, or device drivers.
  - Non-real-time hardware: the hardware that may introduce delays or interruptions, such as caches, interrupts, or buses.
- Therefore, UNIX is not suitable for hard real-time applications, where missing a deadline may cause catastrophic consequences, such as in aerospace, medical, or nuclear systems.
- UNIX may be used for soft real-time applications, where missing a deadline may degrade the performance or quality of service, but not cause failure, such as in multimedia, gaming, or web servers.
- Some examples of UNIX-like systems that have been modified to support real-time features are:
  - Linux: a popular open-source operating system that can be configured with various patches, such as PREEMPT_RT, Xenomai, or RTAI, to achieve real-time performance .
  - QNX: a commercial operating system that uses a microkernel architecture and a message-passing model to provide real-time performance and reliability.
  - Solaris: a proprietary operating system that offers real-time extensions, such as RT scheduling class, RT signals, and RT semaphores.