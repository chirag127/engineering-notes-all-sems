# Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and execution times to tasks in a real-time system, such that the system can meet its timing constraints and performance goals.
- A real-time operating system (RTOS) is a software platform that provides the core functionality for a real-time system, such as task management, inter-task communication, timing and synchronization, interrupt handling, memory management, and device drivers.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.

## VXWORKS

- VXWORKS is a commercial RTOS developed by Wind River Systems, Inc. It supports various architectures, such as x86, ARM, PowerPC, MIPS, and SPARC, and various platforms, such as aerospace, defense, industrial, medical, and automotive.
- VXWORKS provides a preemptive priority-based scheduler, which allows the user to assign up to 256 priority levels to tasks. The scheduler always runs the highest priority ready task, and preempts the current task if a higher priority task becomes ready.
- VXWORKS also supports various scheduling policies, such as round-robin, time-slicing, and deadline-based scheduling, which can be applied to tasks with the same priority level. The user can configure the scheduling policy and the time slice for each task.
- VXWORKS provides various kernel services and features, such as task creation, deletion, suspension, and resume, task stack overflow detection, task information query, task hook routines, inter-task communication mechanisms (such as message queues, semaphores, mutexes, and events), timers, interrupts, memory management, and device drivers.

## FREE RTOS

- FREE RTOS is an open source RTOS developed by Richard Barry and maintained by Amazon Web Services. It supports various architectures, such as x86, ARM, AVR, PIC, and MSP430, and various platforms, such as IoT, automotive, industrial, and medical.
- FREE RTOS provides a preemptive priority-based scheduler, which allows the user to assign up to 255 priority levels to tasks. The scheduler always runs the highest priority ready task, and preempts the current task if a higher priority task becomes ready.
- FREE RTOS also supports round-robin scheduling, which can be applied to tasks with the same priority level. The user can configure the time slice for each task.
- FREE RTOS provides the core real-time scheduling functionality, inter-task communication mechanisms (such as message queues, semaphores, mutexes, and events), timing and synchronization primitives (such as timers, delays, and tick hooks), and memory management. Additional features, such as a command console interface and network stack, can be included as add-ons.