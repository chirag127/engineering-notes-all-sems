### Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and deadlines to tasks that run on a real-time operating system (RTOS).
- An RTOS is a software platform that provides deterministic and predictable behavior for embedded systems and real-time applications.
- An RTOS typically consists of a kernel, which manages the tasks, interrupts, timers, and other system resources, and optional components, such as a network stack, a file system, a command console, and device drivers.
- An RTOS must meet the timing constraints of the tasks, which are usually specified by their worst-case execution time (WCET), deadline, and period.
- An RTOS must also handle the problem of priority inversion, which occurs when a high-priority task is blocked by a low-priority task that holds a shared resource.
- There are different types of realtime scheduling algorithms, such as fixed-priority, dynamic-priority, earliest deadline first, rate-monotonic, and deadline-monotonic.
- VXWORKS and FREE RTOS are two popular RTOS platforms that support realtime scheduling for embedded systems and real-time applications.
- VXWORKS is a commercial RTOS developed by Wind River Systems, which offers a rich set of features, such as a POSIX-compliant API, a graphical user interface, a network stack, a file system, and device drivers.
- VXWORKS supports preemptive, fixed-priority scheduling, with 256 priority levels and a priority inheritance protocol to avoid priority inversion.
- VXWORKS also supports optional components, such as a time-partitioned scheduler, a memory protection unit, and a hypervisor, to enhance the performance, security, and reliability of the system.
- FREE RTOS is an open-source RTOS developed by Richard Barry, which offers a minimal and lightweight core, consisting of a kernel, a queue, a semaphore, and a software timer.
- FREE RTOS supports preemptive, fixed-priority scheduling, with a configurable number of priority levels and a priority inheritance protocol to avoid priority inversion.
- FREE RTOS also supports optional components, such as a command console interface, a network stack, and a file system, which can be included as add-ons.
- FREE RTOS is designed to be portable, scalable, and easy to use, and it supports a wide range of microcontrollers and development tools.