### Process Control Block (PCB) for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process  .
- A PCB is also known as a process descriptor or a task control block  .
- A PCB is created by the operating system when a process is initialized or installed .
- A PCB gives identity to each process so that the operating system can easily distinguish between processes.
- A PCB stores the register content or the execution context of the processor when the process is blocked from running.
- The execution context enables the operating system to restore the process's state when the process returns to the running state.
- A PCB typically contains the following information about a process  :
  - Process ID: a unique identifier for the process
  - Process state: the current status of the process, such as ready, running, waiting, etc.
  - Program counter: the address of the next instruction to be executed by the process
  - CPU registers: the values of the general-purpose registers, stack pointer, etc.
  - CPU scheduling information: the priority, quantum, queue pointer, etc. of the process
  - Memory management information: the base and limit registers, page tables, segment tables, etc. of the process
  - Accounting information: the CPU time, system time, waiting time, etc. of the process
  - I/O status information: the list of I/O devices allocated to the process, open files, etc. of the process
- A PCB is usually stored in a process table, which is an array of PCBs indexed by the process ID.
- A PCB is updated by the operating system whenever the process changes its state or performs any operation.
- A PCB is deleted by the operating system when the process terminates or is killed.