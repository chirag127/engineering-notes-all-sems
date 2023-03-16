# Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and deadlines to tasks that need to execute on a system with real-time constraints, such as timeliness, predictability and responsiveness.
- A real-time operating system (RTOS) is a software platform that provides the core functionality for managing the tasks, resources and events of a real-time system.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.

## VXWORKS

- VXWORKS is a commercial RTOS developed by Wind River Systems, Inc. It supports multiple architectures, such as x86, ARM, PowerPC and MIPS, and provides a rich set of features, such as networking, file system, security, graphics and device drivers.
- VXWORKS uses a preemptive priority-based scheduling algorithm, which means that the highest priority task that is ready to run will always preempt the lower priority tasks. The priority of a task can be static or dynamic, depending on the configuration.
- VXWORKS also supports various scheduling policies, such as round-robin, time-slice and deadline-based, which can be applied to tasks with the same priority level. These policies can help to balance the CPU utilization and the fairness among tasks.
- VXWORKS provides mechanisms to deal with priority inversion, which is a situation where a high priority task is blocked by a lower priority task that holds a shared resource. These mechanisms include priority inheritance, priority ceiling and mutexes.

## FREE RTOS

- FREE RTOS is an open source RTOS that is designed to be simple, portable and scalable. It supports many architectures, such as ARM, AVR, PIC and MSP430, and can run on bare metal or with a minimal hardware abstraction layer (HAL).
- FREE RTOS also uses a preemptive priority-based scheduling algorithm, but it has a simpler and smaller kernel than VXWORKS. It only provides the core real-time scheduling features, inter-task communication, and timing and synchronization primitives. Additional features, such as networking, file system and command console, can be added as optional components.
- FREE RTOS allows the user to assign a priority to each task, and the scheduler will always run the highest priority task that is ready. The priority of a task can be changed at run time, but it is not recommended to do so frequently, as it may affect the system performance and determinism.
- FREE RTOS does not support different scheduling policies for tasks with the same priority level, but it does provide a special idle task that will execute only when there are no other tasks able to run. The idle task can be used to perform low priority or background activities, such as power saving or garbage collection.
- FREE RTOS also provides mechanisms to deal with priority inversion, such as priority inheritance and mutexes. However, it does not support priority ceiling, which is a technique to assign the highest priority of all the tasks that may access a shared resource to the resource itself.