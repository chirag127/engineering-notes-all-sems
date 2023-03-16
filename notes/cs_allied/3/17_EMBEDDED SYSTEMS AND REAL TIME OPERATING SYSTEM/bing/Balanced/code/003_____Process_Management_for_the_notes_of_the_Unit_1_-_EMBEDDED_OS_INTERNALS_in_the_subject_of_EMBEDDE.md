### Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the OS manages and views other software in the embedded system (via processes)  .
- A process is a program in execution, which has a unique process identifier, a set of registers, a stack, a program counter, and a memory space .
- A process can be in one of the following states: ready, running, waiting, or terminated .
- Process management involves the following functions :
  - Process creation: allocating memory and resources for a new process, initializing its attributes, and adding it to the ready queue.
  - Process scheduling: selecting the next process to run based on a scheduling algorithm, such as round-robin, priority, or shortest job first.
  - Process switching: saving the context of the current process and restoring the context of the next process, which involves changing the program counter, the stack pointer, and the registers.
  - Process synchronization: coordinating the execution of multiple processes that share data or resources, using mechanisms such as semaphores, mutexes, or message queues.
  - Process communication: enabling the exchange of data or signals between processes, using mechanisms such as pipes, sockets, or shared memory.
  - Process termination: releasing the memory and resources of a process, removing it from the ready queue, and notifying its parent or other processes.
- Process management in embedded systems differs from general-purpose systems in the following aspects :
  - Embedded systems usually have limited memory and resources, which require efficient and optimized process management techniques.
  - Embedded systems often have strict real-time and event-driven requirements, which require predictable and deterministic process scheduling and switching.
  - Embedded systems may have different types of processors, such as microcontrollers, digital signal processors, or application-specific integrated circuits, which require different process management strategies and architectures.
  - Embedded systems may have different types of operating systems, such as bare-metal, monolithic, microkernel, or hybrid, which provide different levels of process management functionality and abstraction.