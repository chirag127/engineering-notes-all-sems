### Control Blocks

Control blocks are data structures used by the kernel of a real-time operating system (RTOS) to manage and control the execution of tasks. They are an essential component of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

Some key points to note about control blocks are:

1. Control blocks contain information about the state of a task, such as its priority, current execution status, and any resources it may be using or waiting for.
2. The kernel uses control blocks to determine which task should be executed next, based on factors such as task priority and scheduling algorithms.
3. Control blocks are typically created and initialized when a task is created, and are updated by the kernel as the task executes and changes state.
4. The number and size of control blocks in an RTOS is typically fixed at compile-time, and is determined by the maximum number of tasks that the system can support.
5. Control blocks are typically stored in a fixed location in memory, and are accessed by the kernel using pointers or indices.

In summary, control blocks are an essential component of a real-time operating system, and are used by the kernel to manage and control the execution of tasks. They contain important information about the state of tasks, and are used by the kernel to make scheduling decisions. Understanding the role and function of control blocks is important for anyone studying the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.