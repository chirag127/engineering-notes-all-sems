### Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures that store information about various components of a real time kernel, such as tasks, timers, messages, interrupts, etc.
- Control blocks are usually created and managed by the kernel, and are protected from normal user access.
- Control blocks enable the kernel to perform various functions, such as task management, scheduling, synchronization, communication, etc.
- Some of the common types of control blocks are:

  - **Task Control Block (TCB)**: It contains information about a task, such as its id, priority, state, stack pointer, context, etc. The kernel uses the TCB to create, terminate, suspend, resume, and change the priority of tasks. The kernel also uses the TCB to perform context switching between tasks.   
  - **Timer Control Block (TCB)**: It contains information about a timer, such as its id, expiration time, callback function, etc. The kernel uses the TCB to create, delete, start, stop, and reset timers. The kernel also uses the TCB to invoke the callback function when the timer expires. 
  - **Message Control Block (MCB)**: It contains information about a message, such as its id, source, destination, size, content, etc. The kernel uses the MCB to create, delete, send, and receive messages. The kernel also uses the MCB to perform synchronization and communication between tasks. 
  - **Interrupt Control Block (ICB)**: It contains information about an interrupt, such as its id, source, priority, handler, etc. The kernel uses the ICB to register, deregister, enable, and disable interrupts. The kernel also uses the ICB to invoke the handler when the interrupt occurs.