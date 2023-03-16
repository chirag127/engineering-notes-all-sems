# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- Processing time requirements need to be fully understood and bound rather than just kept as a minimum.
- Unix is not a RTOS by default, but it can be modified or extended to provide some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one.
  - Real-time signals: the ability to deliver signals to processes without blocking or delaying them.
  - High-resolution timers: the ability to measure and control time with nanosecond precision.
  - Memory locking: the ability to prevent memory pages from being swapped out to disk.
  - Priority inheritance: the ability to avoid priority inversion, a situation where a low-priority process holds a resource needed by a high-priority process.
- Some examples of Unix variants or extensions that provide real-time features are:
  - RTLinux: a hard real-time extension for Linux that runs the Linux kernel as a low-priority process on top of a small real-time core.
  - Xenomai: a dual-kernel RTOS that coexists with the Linux kernel and provides a POSIX-compliant interface for real-time applications.
  - QNX: a microkernel-based RTOS that supports POSIX and Unix standards and provides a distributed architecture for embedded systems.
  - Solaris: a Unix-based OS that supports real-time scheduling, memory locking, and high-resolution timers.
  - VxWorks: a proprietary RTOS that supports POSIX and Unix standards and provides a modular and scalable architecture for embedded systems.