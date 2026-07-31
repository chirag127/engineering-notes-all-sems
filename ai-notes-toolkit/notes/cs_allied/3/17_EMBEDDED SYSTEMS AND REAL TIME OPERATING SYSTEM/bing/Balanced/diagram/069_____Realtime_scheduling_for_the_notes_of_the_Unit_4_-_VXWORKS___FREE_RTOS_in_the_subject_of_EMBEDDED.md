### Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and execution times to tasks in a real-time system, such that the system can meet its timing constraints and performance goals.
- A real-time operating system (RTOS) is a software platform that provides the core functionality for a real-time system, such as task management, inter-task communication, timing and synchronization, interrupt handling, memory management, and device drivers.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.
- VXWORKS is a commercial RTOS developed by Wind River Systems, which supports multiple architectures, such as x86, ARM, PowerPC, and MIPS. It offers a rich set of features, such as preemptive priority-based scheduling, round-robin scheduling, rate-monotonic scheduling, POSIX compliance, networking, file system, security, and graphical user interface.
- FREE RTOS is an open source RTOS developed by Richard Barry, which supports more than 40 architectures, such as AVR, PIC, MSP430, and Cortex-M. It offers a minimal set of features, such as preemptive priority-based scheduling, cooperative scheduling, inter-task communication, timing and synchronization primitives. It is designed to be a real-time kernel, rather than a full operating system, and additional features can be added as modules or libraries.
- The main differences between VXWORKS and FREE RTOS are:

  - VXWORKS is a proprietary RTOS, while FREE RTOS is a free and open source RTOS.
  - VXWORKS has a larger footprint and requires more resources, while FREE RTOS has a smaller footprint and requires less resources.
  - VXWORKS supports more advanced scheduling algorithms, such as rate-monotonic scheduling, while FREE RTOS only supports priority-based scheduling.
  - VXWORKS provides more built-in features and services, such as networking, file system, security, and graphical user interface, while FREE RTOS provides only the core functionality and relies on external modules or libraries for additional features.
  - VXWORKS has a higher level of certification and validation, such as DO-178B and IEC 61508, while FREE RTOS has a lower level of certification and validation, such as MISRA C compliance and SAFERTOS certification.

- The main similarities between VXWORKS and FREE RTOS are:

  - Both are RTOS that support embedded systems and real-time applications.
  - Both use preemptive priority-based scheduling as the default scheduling algorithm, which allows the highest priority task to run at any time and preempts lower priority tasks.
  - Both provide inter-task communication mechanisms, such as message queues, semaphores, and mutexes, which allow tasks to exchange data and synchronize their execution.
  - Both provide timing and synchronization primitives, such as timers, delays, and event flags, which allow tasks to perform time-sensitive operations and coordinate their activities.
  - Both support multiple architectures and platforms, and can be customized and configured according to the application requirements.