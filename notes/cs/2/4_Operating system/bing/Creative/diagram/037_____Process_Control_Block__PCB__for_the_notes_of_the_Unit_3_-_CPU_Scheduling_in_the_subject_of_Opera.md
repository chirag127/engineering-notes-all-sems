### Process Control Block (PCB)

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process .
- A PCB is also known as a process descriptor or a task control block (TCB) .
- A PCB is created by the operating system when a process is initialized or installed .
- A PCB gives identity to each process so that the operating system can easily distinguish between them.
- A PCB stores the register content or the execution context of the processor when the process is blocked from running.
- A PCB enables the operating system to restore a process's execution context when the process returns to the running state.
- A PCB typically contains the following components  :
  - Process ID: A unique identifier for the process.
  - Process state: The current status of the process, such as ready, running, waiting, etc.
  - Program counter: The address of the next instruction to be executed by the process.
  - CPU registers: The values of the general-purpose registers, stack pointer, etc.
  - CPU scheduling information: The priority, queue, burst time, etc. of the process for scheduling purposes.
  - Memory management information: The base and limit registers, page tables, segment tables, etc. of the process for memory allocation and protection.
  - Accounting information: The user ID, group ID, CPU time, system time, etc. of the process for resource usage and billing.
  - I/O status information: The list of open files, devices, pipes, sockets, etc. used by the process for input/output operations.
- A PCB is usually stored in a process table, which is an array of PCBs maintained by the operating system.
- A PCB can be accessed and modified by the operating system using pointers or indexes to the process table.
- A PCB can be deleted by the operating system when the process terminates or exits.