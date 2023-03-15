### Process States

A process is a program in execution that requires various resources such as CPU, memory, disk, and I/O devices. A process is represented by a process control block (PCB) in the operating system, which contains various information about the process such as its identifier, priority, state, registers, memory allocation, etc. 

A process can be in one of the following states during its lifetime:

- **New**: The process is being created but not yet loaded into the main memory. It is the program that is present in the secondary memory that will be picked up by the OS to create the process. 
- **Ready**: The process is loaded into the main memory and is waiting for the CPU to be allocated. The process is placed in the ready queue, which is a data structure that holds all the ready processes. The ready queue is managed by a scheduling algorithm that decides which process to run next.  
- **Running**: The process is selected by the scheduler and is executing on the CPU. The process can run in either user mode or kernel mode, depending on the type of instructions it is executing. User mode is the normal mode of execution, where the process can access only its own memory space and has limited privileges. Kernel mode is the privileged mode of execution, where the process can access the entire memory space and has full control over the hardware. The process switches from user mode to kernel mode when it requests a system service or encounters an interrupt or an exception.  
- **Blocked**: The process is waiting for an event to occur, such as an I/O operation to complete, a signal to arrive, a resource to be available, etc. The process cannot run until the event occurs, so it is moved from the CPU to the blocked queue, which is a data structure that holds all the blocked processes. The process remains in the blocked state until the event occurs, and then it is moved to the ready state.  
- **Terminated**: The process has completed its execution and is no longer needed. The process releases all the resources it has acquired and exits the system. The OS removes the process from the PCB and frees up the memory space occupied by the process.  

The following diagram shows the possible transitions between the process states:

![Process State Diagram](https://www.guru99.com/images/1/020221_0619_ProcessMana1.png)

: https://www.guru99.com/process-management-pcb.html
: https://www.geeksforgeeks.org/states-of-a-process-in-operating-systems/
: https://www.tutorialspoint.com/what-are-the-process-states-in-windows-and-linux
: https://en.wikipedia.org/wiki/Process_state
: https://www.javatpoint.com/os-process-states