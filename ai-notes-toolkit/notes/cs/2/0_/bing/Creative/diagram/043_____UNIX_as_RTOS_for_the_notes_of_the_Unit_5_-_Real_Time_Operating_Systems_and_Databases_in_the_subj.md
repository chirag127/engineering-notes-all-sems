### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for an RTOS, correct timing is the key feature.
- UNIX is not designed as an RTOS, but it can be modified or extended to support some real-time features, such as:
  - Preemptive scheduling: the ability of the OS to interrupt a running process and switch to another one with higher priority.
  - Priority inheritance: the mechanism that prevents priority inversion, which occurs when a low-priority process holds a resource needed by a high-priority process.
  - Real-time signals: the signals that are delivered to a process immediately, without being queued or blocked.
  - POSIX real-time extensions: the set of standards that define interfaces and behavior for real-time applications on UNIX-like systems.
- Some examples of UNIX variants or derivatives that have real-time capabilities are:
  - Solaris: a proprietary UNIX OS developed by Sun Microsystems (now Oracle) that supports real-time scheduling, priority inheritance, and real-time signals.
  - QNX: a commercial UNIX-like RTOS that is widely used in embedded systems, such as automotive, medical, and industrial applications.
  - RTLinux: a hard real-time extension to the Linux kernel that runs Linux as a low-priority process on top of a small real-time core.
  - Xenomai: a dual-kernel RTOS that coexists with the Linux kernel and provides a POSIX-compliant real-time interface.
  - PREEMPT_RT: a patch set that transforms the Linux kernel into a fully preemptible kernel, with improved latency and determinism.