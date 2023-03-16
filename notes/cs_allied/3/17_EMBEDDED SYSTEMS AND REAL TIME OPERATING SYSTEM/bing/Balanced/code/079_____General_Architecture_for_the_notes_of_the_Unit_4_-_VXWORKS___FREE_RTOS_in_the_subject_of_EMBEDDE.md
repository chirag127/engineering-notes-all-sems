# General Architecture for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that are used for embedded systems and real-time applications.
- RTOS are designed to meet the performance requirements and timing constraints of time-sensitive systems, such as industrial control, robotics, aerospace, and defense.
- RTOS differ from general purpose operating systems (GPOS) in terms of scheduling, kernel, and priority inversion handling.
- The general architecture of VXWORKS and FREE RTOS can be compared as follows:

## Scheduling
- Scheduling is the process of allocating CPU time to tasks based on their priority and deadlines.
- VXWORKS supports preemptive priority-based scheduling, which means that a higher priority task can interrupt a lower priority task at any time.
- VXWORKS also supports round-robin scheduling, which means that tasks with the same priority are executed in a circular order for a fixed time slice.
- FREE RTOS supports preemptive priority-based scheduling as well, but it also allows the user to configure the scheduler as cooperative, which means that tasks can voluntarily yield the CPU to other tasks.
- FREE RTOS does not support round-robin scheduling, but it provides a mechanism called time slicing, which allows tasks with the same priority to share the CPU time equally.

## Kernel
- Kernel is the core component of an operating system that manages the system resources, such as memory, devices, and interrupts.
- VXWORKS has a monolithic kernel, which means that all the kernel functions are executed in the same address space and memory protection domain.
- VXWORKS kernel is modular, which means that the user can select the components and features that are needed for the application and exclude the rest.
- VXWORKS kernel is also scalable, which means that it can run on different hardware platforms and architectures, such as x86, ARM, PowerPC, and MIPS.
- FREE RTOS has a microkernel, which means that the kernel functions are executed in separate address spaces and memory protection domains.
- FREE RTOS kernel is minimal, which means that it only provides the basic functionality of task management, synchronization, and communication.
- FREE RTOS kernel is also portable, which means that it can run on various microcontrollers and processors, such as AVR, PIC, MSP430, and Cortex-M.

## Priority Inversion
- Priority inversion is a situation where a lower priority task holds a resource that is needed by a higher priority task, causing the higher priority task to be blocked and the lower priority task to be executed instead.
- VXWORKS handles priority inversion by using a mechanism called priority inheritance, which means that the lower priority task inherits the priority of the highest priority task that is waiting for the resource, and releases the resource as soon as possible.
- VXWORKS also provides an option to use priority ceiling, which means that the priority of the task that acquires the resource is raised to the highest priority level of any task that may use the resource, and lowered to its original level when the resource is released.
- FREE RTOS handles priority inversion by using a mechanism called priority inheritance as well, but it also allows the user to disable this feature if it is not needed or desired.
- FREE RTOS does not support priority ceiling, but it provides a mechanism called mutexes, which are mutual exclusion locks that can be used to protect critical sections of code from concurrent access by multiple tasks.