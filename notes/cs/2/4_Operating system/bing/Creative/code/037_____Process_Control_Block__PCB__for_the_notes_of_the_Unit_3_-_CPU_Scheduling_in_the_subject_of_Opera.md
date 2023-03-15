### Process Control Block (PCB) for the notes of the Unit 3 - CPU Scheduling in the subject of Operating System

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process.
- It is also known as a process descriptor.
- When a process is created (initialized or installed), the operating system creates a corresponding process control block.
- A process control block or simple PCB is a data structure that is used to store the information of a process that might be needed to manage the scheduling of a particular process.
- So, each process will be given a PCB which is a kind of identification card for a process.
- The OS maintains all Process Control Blocks (PCBs) in Process Scheduling Queues.
- The OS maintains a separate queue for each of the process states and PCBs of all processes in the same execution state are placed in the same queue.
- When the state of a process is changed, its PCB is unlinked from its current queue and moved to its new state queue.
- The process control block stores the register content also known as execution content of the processor when it was blocked from running.
- This execution content architecture enables the operating system to restore a process’s execution context when the process returns to the running state.
- To identify the processes, it assigns a process identification number (PID) to each process.
- As the operating system supports multi-programming, it needs to keep track of all the processes.
- For this task, the process control block (PCB) is used to track the process’s execution status.