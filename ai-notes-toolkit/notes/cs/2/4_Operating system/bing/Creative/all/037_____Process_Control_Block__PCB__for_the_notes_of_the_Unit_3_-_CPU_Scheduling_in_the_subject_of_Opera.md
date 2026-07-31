# Process Control Block (PCB)

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process  .
- It is also known as a process descriptor.
- When a process is created (initialized or installed), the operating system creates a corresponding process control block .
- The process control block stores the register content also known as execution context of the processor when it was blocked from running.
- This execution context architecture enables the operating system to restore a process’s execution context when the process returns to the running state.
- The role of PCB is to give identity to each process so that operating system can easily distinguish between processes.
- PCBs are stored in specially reserved memory for the operating system known as kernel space.
- The information stored in a PCB may vary depending on the operating system, but some common components are  :
  - Process ID: A unique identifier for the process.
  - Process state: The current status of the process, such as ready, running, waiting, terminated, etc.
  - Program counter: The address of the next instruction to be executed by the process.
  - CPU registers: The values of the general purpose registers, stack pointer, index registers, etc. used by the process.
  - CPU scheduling information: The priority, quantum, queue pointer, etc. used by the CPU scheduler to manage the process.
  - Memory management information: The base and limit registers, page tables, segment tables, etc. used by the memory manager to allocate and deallocate memory for the process.
  - Accounting information: The CPU time, system time, IO time, etc. used by the process for performance monitoring and billing purposes.
  - IO status information: The list of open files, devices, sockets, etc. used by the process for input and output operations.