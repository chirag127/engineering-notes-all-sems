### Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the OS manages and views other software in the embedded system (via processes) .
- A process is a unit of execution that consists of a program code, data, stack, and a set of registers .
- A process can be in one of the following states: ready, running, waiting, or terminated .
- A process can switch from one state to another due to events such as interrupts, system calls, or scheduler decisions .
- Process management involves the following functions :
  - Process creation: allocating memory and resources for a new process and adding it to the ready queue.
  - Process synchronization: coordinating the execution of multiple processes that share data or resources.
  - Process communication: enabling processes to exchange information or signals.
  - Process termination: releasing the memory and resources of a process and removing it from the system.
- Process management in embedded systems differs from general-purpose systems in the following aspects :
  - Embedded systems usually have limited memory and resources, so process management must be efficient and optimized.
  - Embedded systems often have strict real-time and event-driven requirements, so process management must ensure timely and predictable execution of processes.
  - Embedded systems may have different types of processors, such as microcontrollers, DSPs, or FPGAs, so process management must be adaptable and portable.
- Process management in embedded systems can be implemented using different techniques, such as :
  - Cooperative multitasking: processes voluntarily yield the CPU to other processes when they are idle or waiting.
  - Preemptive multitasking: the OS interrupts the running process and switches to another process based on a priority scheme or a timer.
  - Hybrid multitasking: a combination of cooperative and preemptive multitasking, where processes can be preempted only at certain points or by certain events.