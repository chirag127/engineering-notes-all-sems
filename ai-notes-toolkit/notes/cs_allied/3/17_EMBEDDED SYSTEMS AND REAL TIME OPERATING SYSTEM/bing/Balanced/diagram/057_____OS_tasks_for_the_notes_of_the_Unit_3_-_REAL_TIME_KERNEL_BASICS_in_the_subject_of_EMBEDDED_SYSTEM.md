### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An OS task (also called a process or a thread) is a unit of execution that encapsulates all the information that is involved in the running of a program (stack, program counter, source code, data, etc.).
- An OS task can be in one of the following states: ready, running, blocked, or terminated.
- A task scheduler is a component of the OS that decides which task to run next based on some criteria, such as priority, deadline, or round-robin.
- A real-time operating system (RTOS) is an embedded operating system that guarantees a certain level of performance and responsiveness for time-critical applications.
- A real-time kernel is the core component of an RTOS that provides the basic services for task management, synchronization, communication, and interrupt handling.
- A real-time kernel can be classified into two types: preemptive and cooperative.
- A preemptive kernel allows a higher priority task to interrupt a lower priority task at any time, ensuring that the most urgent task is always executed.
- A cooperative kernel requires a task to voluntarily relinquish the CPU to another task, ensuring that no task can monopolize the CPU.
- A real-time kernel can also support different scheduling algorithms, such as rate-monotonic, earliest deadline first, or least laxity first.
- A real-time kernel can provide various features, such as task creation and deletion, task suspension and resumption, task priority management, task synchronization, task communication, task timers, interrupt handling, and memory management.