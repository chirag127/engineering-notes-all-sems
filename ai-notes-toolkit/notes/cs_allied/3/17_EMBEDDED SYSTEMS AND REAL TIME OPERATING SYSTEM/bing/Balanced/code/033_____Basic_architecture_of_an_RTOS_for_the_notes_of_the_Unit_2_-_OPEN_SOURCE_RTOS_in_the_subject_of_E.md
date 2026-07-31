### Basic architecture of an RTOS

- An RTOS is a Real-Time Operating System that provides predictable and deterministic behavior for embedded and IoT applications.
- An RTOS typically consists of a kernel and various modules that provide additional functionality, such as networking, debugging, device I/O, etc.
- The kernel is the core component of the RTOS that manages the tasks, memory, timers, interrupts, and synchronization mechanisms.
- The tasks are the basic units of execution in an RTOS. They have a priority, a stack, a context, and a state. The state can be ready, running, blocked, or suspended.
- The scheduler is the part of the kernel that decides which task to run next based on the priority and the state of the tasks. The scheduler can be preemptive or cooperative, depending on the RTOS design.
- The memory management module is responsible for allocating and deallocating memory for the tasks and the kernel. It can use static or dynamic memory allocation, depending on the RTOS design.
- The timer module provides the ability to measure time and trigger events at specific intervals. It can use hardware or software timers, depending on the RTOS design.
- The interrupt module handles the external and internal interrupts that occur during the execution of the tasks. It can use interrupt service routines (ISRs) or deferred interrupt handlers, depending on the RTOS design.
- The synchronization module provides the mechanisms to coordinate the access to shared resources and data among the tasks. It can use semaphores, mutexes, queues, events, or message passing, depending on the RTOS design.
- The modules that provide additional functionality, such as networking, debugging, device I/O, etc., are usually implemented as libraries or drivers that interface with the kernel and the tasks. They can use standard or proprietary protocols, depending on the RTOS design.

The following diagram shows a general architecture of an RTOS:

```
+-----------------+
|   Application   |
+-----------------+
|   Networking    |
|   Debugging     |
|   Device I/O    |
+-----------------+
|      Kernel     |
+-----------------+
|  Task Manager   |
| Memory Manager  |
|  Timer Manager  |
| Interrupt Manager|
|Sync. Mechanisms |
+-----------------+
|     Hardware    |
+-----------------+
```

References:

: RTOS - Real Time Operating System - Engineers Garage
: What Is A Real-Time Operating Systems (RTOS) | Wind River
: RTOS Introduction - Real Time Operating System with Examples
: Understand Azure RTOS ThreadX | Microsoft Learn
: Real-time operating system - Wikipedia
: Architecture of RTOS - Part 1 - Robocraze