# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for a RTOS, correct timing is the key feature.
- UNIX is not a RTOS by default, but it can be modified or extended to support some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one when an event occurs.
  - Priority inheritance: the mechanism to avoid priority inversion, which occurs when a low priority process holds a resource needed by a high priority process.
  - Real-time signals: the signals that are delivered to a process immediately, without being queued or blocked.
  - Memory locking: the function to prevent the memory pages of a process from being swapped out to disk, which would cause delays.
  - High-resolution timers: the timers that can measure time intervals with nanosecond precision.
- Some examples of UNIX variants or extensions that support real-time features are:
  - RTLinux: a hard real-time extension to the Linux kernel that runs Linux as a low priority thread on a small real-time core.
  - Xenomai: a dual kernel approach that provides a hard real-time co-kernel to Linux, which can preempt the Linux kernel at any time.
  - PREEMPT_RT: a patch set that transforms the Linux kernel into a fully preemptible kernel, with improved latency and determinism.
  - QNX: a commercial UNIX-like RTOS that uses a microkernel architecture and a message passing model.
  - Solaris: a commercial UNIX-like OS that supports real-time scheduling, memory locking, and high-resolution timers.