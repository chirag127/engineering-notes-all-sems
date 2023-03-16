# Control Blocks for the Notes of the Unit 3 - Real Time Kernel Basics

- A control block is a data structure that contains information about a system entity, such as a process, a task, a file, a device, etc.
- A control block is used by the operating system or the kernel to manage and control the entity, such as creating, terminating, scheduling, communicating, etc.
- A control block typically has a unique identifier, a state, a priority, and other attributes that are relevant to the entity.
- In a real time kernel, a control block is often used to represent a real time task, which is a unit of execution that performs a specific function in a real time system.
- A real time task control block (TCB) has information about the task id, the task state, the task priority, the task deadline, the task stack, the task context, the task resources, the task events, the task timers, etc.
- A real time task control block is created by the kernel when a task is created, and is deleted by the kernel when a task is terminated.
- A real time task control block is updated by the kernel when a task changes its state, priority, deadline, resources, events, timers, etc.
- A real time task control block is used by the kernel to select the next task to run, to switch the context between tasks, to handle the interrupts and exceptions, to synchronize and communicate between tasks, to monitor and enforce the timing constraints, etc.
- A real time task control block is usually stored in a protected memory area that is inaccessible by the normal user tasks, to prevent unauthorized or accidental modification or corruption of the task information.
- A real time task control block is usually located at the beginning of the kernel stack for the task, as it is a safe and convenient location for the kernel to access and manipulate the task information.