### Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures used by the real time kernel to store and manage information about the tasks and resources in the system  .
- Control blocks are usually kept in a protected memory area that is inaccessible to the normal user tasks.
- Control blocks can be classified into two types: task control blocks (TCB) and resource control blocks (RCB).
- Task control blocks are used to store information about each task in the system, such as task id, priority, state, stack pointer, program counter, registers, etc  .
- Resource control blocks are used to store information about each resource in the system, such as resource id, type, owner, waiting list, etc.
- The real time kernel uses control blocks to perform various operations, such as task creation, termination, scheduling, synchronization, communication, etc .
- The real time kernel also uses control blocks to handle interrupts, timers, network messages, etc .
- Control blocks are essential for the real time kernel to achieve concurrency, responsiveness, and predictability in the system .