### Process Control Block (PCB)

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process.
- A PCB is also known as a process descriptor or a task control block (TCB) .
- A PCB is created by the operating system when a process is initialized or installed .
- A PCB gives identity to each process so that the operating system can easily distinguish between processes.
- A PCB stores the register content or the execution context of the processor when the process is blocked from running.
- A PCB enables the operating system to restore a process's execution context when the process returns to the running state.
- A PCB typically contains the following components  :
  - Process ID: A unique identifier for the process.
  - Process state: The current status of the process, such as ready, running, waiting, etc.
  - Program counter: The address of the next instruction to be executed by the process.
  - CPU registers: The values of the general-purpose registers, stack pointer, etc.
  - CPU scheduling information: The priority, burst time, queue number, etc. of the process for scheduling purposes.
  - Memory management information: The base and limit registers, page tables, segment tables, etc. of the process for memory allocation and protection.
  - Accounting information: The CPU time, system time, IO time, etc. of the process for performance monitoring and billing.
  - IO status information: The list of IO devices, files, sockets, etc. allocated to the process for input and output operations.
- A PCB is usually stored in a process table, which is an array of PCBs indexed by the process ID.
- A PCB is updated by the operating system whenever there is a change in the process state or the execution context.
- A PCB is deleted by the operating system when the process terminates or exits.