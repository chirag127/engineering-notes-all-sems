### Process States

A process is a program in execution. It is the active state of the program when it is executing and it has its own process control block (PCB), which contains various information about the process, such as its identifier, priority, state, program counter, registers, memory allocation, etc.  

A process can be in one of the following states:

- **New**: The process is being created but not yet loaded into the main memory. It is the program which is present in secondary memory that will be picked up by the operating system to create the process. 
- **Ready**: The process is loaded into the main memory and is waiting for the CPU to be allocated. It is placed in the ready queue, which contains all the processes that are ready to run.  
- **Running**: The process is selected by the CPU scheduler and is executing on the CPU. There can be at most one running process per CPU or core. A process can run in either of the two modes, namely kernel mode or user mode. In kernel mode, the process can access the system resources and execute privileged instructions. In user mode, the process can only access its own address space and execute non-privileged instructions.  
- **Waiting**: The process is waiting for some event to occur, such as an input/output operation, a signal, a timer, etc. It is placed in the waiting queue, which contains all the processes that are blocked by some event.  
- **Terminated**: The process has completed its execution and is removed from the system. The operating system reclaims the resources allocated to the process and updates the PCB.  

The following diagram shows the possible transitions between the process states:

![Process States Diagram](https://www.guru99.com/images/1/020819_0617_ProcessMana1.png)

: https://www.guru99.com/process-management-pcb.html
: https://www.geeksforgeeks.org/states-of-a-process-in-operating-systems/
: https://www.tutorialspoint.com/what-are-the-process-states-in-windows-and-linux
: https://en.wikipedia.org/wiki/Process_state
: https://www.javatpoint.com/os-process-states