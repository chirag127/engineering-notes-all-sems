### Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures that store information about the tasks or processes in a real time kernel or operating system.
- Control blocks are also known as process control blocks (PCBs) or task control blocks (TCBs).
- Control blocks are created by the kernel when a task or process is created, and deleted when the task or process is terminated.
- Control blocks are usually stored in a protected memory area that is inaccessible to normal user access, such as the kernel stack or a linked list.
- Control blocks contain various information about the tasks or processes, such as:
  - Task or process identifier (ID)
  - Task or process priority
  - Task or process state (idle, running, ready, blocked, terminated, etc.)
  - Task or process context (registers, program counter, stack pointer, etc.)
  - Task or process resources (memory, files, devices, etc.)
  - Task or process inter-task communication (messages, signals, semaphores, etc.)
  - Task or process timing (arrival time, execution time, deadline, etc.)
- Control blocks are used by the kernel to manage the tasks or processes, such as:
  - Scheduling: the kernel uses the priority, state, and timing information to decide which task or process to run next.
  - Switching: the kernel uses the context information to save and restore the state of the tasks or processes when switching between them.
  - Synchronization: the kernel uses the inter-task communication information to coordinate the tasks or processes that share resources or data.
  - Termination: the kernel uses the resources information to release the resources allocated to the tasks or processes when they are terminated.