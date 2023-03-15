# Process States

A process is a program in execution that requires various resources such as CPU, memory, disk, and I/O devices. A process is represented by a process control block (PCB) in the operating system, which contains various information about the process such as its identifier, priority, state, registers, memory allocation, etc. 

A process can be in one of the following states during its lifetime:

- **New**: The process is being created but not yet ready to run. It is the program that is present in the secondary memory that will be loaded into the main memory by the operating system. 
- **Ready**: The process is loaded into the main memory and is waiting for the CPU to be allocated. The process is placed in the ready queue, which is a data structure that holds all the ready processes. 
- **Running**: The process is selected by the CPU scheduler and is executing on the CPU. There can be at most one running process per CPU or core. A process can run in either user mode or kernel mode, depending on the type of instructions it is executing.  
- **Waiting**: The process is blocked and cannot run until some event occurs, such as an I/O completion, a signal, a timer expiration, etc. The process is placed in the waiting queue, which is a data structure that holds all the blocked processes. 
- **Terminated**: The process has completed its execution and is removed from the system. The operating system reclaims the resources allocated to the process and updates the PCB. 

The following diagram shows the possible transitions between the process states:

![Process State Diagram](https://www.guru99.com/images/1/020221_0615_ProcessMana1.png)

: https://www.guru99.com/process-management-pcb.html
: https://www.geeksforgeeks.org/states-of-a-process-in-operating-systems/
: https://en.wikipedia.org/wiki/Process_state