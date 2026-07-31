# Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures that store information about the processes or tasks in a real time kernel.
- A real time kernel is a software component that manages the execution of multiple tasks in a real time operating system (RTOS).
- A real time operating system is a system that can respond to events or inputs within a specified time constraint, such as in embedded systems or control systems.
- Some of the functions of a real time kernel are:
  - Task management: creating, terminating, scheduling, and prioritizing tasks.
  - Resource management: allocating and deallocating memory, I/O devices, and other resources to tasks.
  - Synchronization and communication: providing mechanisms for tasks to coordinate and exchange data, such as semaphores, message queues, and events.
  - Interrupt handling: servicing hardware or software interrupts and dispatching them to the appropriate tasks.
  - Timer management: providing services for tasks to measure time, set timeouts, and generate periodic events.

- A control block typically contains the following information about a task:
  - Task ID: a unique identifier for the task.
  - Task state: the current status of the task, such as running, ready, blocked, or terminated.
  - Task priority: the relative importance of the task, which affects its scheduling order.
  - Task context: the set of registers and memory locations that store the task's execution state, such as the program counter, the stack pointer, and the data segment.
  - Task resources: the list of resources that the task owns or requests, such as memory blocks, I/O devices, or semaphores.
  - Task attributes: the parameters that define the task's behavior, such as its deadline, period, or execution time.

- A control block is usually created by the kernel when a task is initialized, and is updated by the kernel during the task's lifetime. The control block is stored in a protected memory area that is inaccessible to the normal user. The kernel maintains a table or a list of all the control blocks in the system, and uses them to perform its functions.
- A control block is also known as a process control block (PCB) or a task control block (TCB) in some literature.