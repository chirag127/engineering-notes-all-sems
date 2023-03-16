### Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the OS manages and views other software in the embedded system (via processes).
- A process is a unit of execution that has its own state, memory, and resources.
- A subfunction typically found within process management is interrupt and error detection management.
- Interrupts are signals that notify the OS of an event that requires immediate attention, such as a timer expiration, a keyboard input, or a sensor reading.
- Error detection is the process of identifying and handling errors that occur during the execution of a process, such as memory faults, division by zero, or illegal instructions.
- Process management involves the following tasks:
  - Process creation: the OS allocates memory and resources for a new process and assigns it a unique identifier.
  - Process scheduling: the OS decides which process to run next based on criteria such as priority, deadline, or fairness.
  - Process synchronization: the OS coordinates the access of shared resources among multiple processes to avoid conflicts and ensure consistency.
  - Process communication: the OS enables the exchange of data and messages among processes using mechanisms such as pipes, sockets, or message queues.
  - Process termination: the OS frees the memory and resources of a process that has completed its execution or has been aborted.
- Process management in embedded systems differs from general-purpose systems in the following aspects :
  - Embedded systems usually have limited memory and resources, which require efficient and optimized process management algorithms and data structures.
  - Embedded systems often have strict real-time and event-driven requirements, which demand fast and predictable process scheduling and interrupt handling.
  - Embedded systems may have safety-critical or mission-critical functions, which necessitate robust and reliable error detection and recovery mechanisms.
  - Embedded systems may have long life cycles, which imply stable and adaptable process management solutions that can cope with changing requirements and environments.