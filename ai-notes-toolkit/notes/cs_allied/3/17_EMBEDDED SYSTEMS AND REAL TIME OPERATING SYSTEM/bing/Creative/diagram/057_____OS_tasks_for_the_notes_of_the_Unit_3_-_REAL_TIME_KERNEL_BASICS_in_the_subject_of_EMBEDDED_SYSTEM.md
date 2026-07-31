### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. It is created by the OS to encapsulate all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc.
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the OS that decides which task should run at any given time, based on factors such as priority, deadline, resource availability, etc.
- A task scheduler can be either preemptive or cooperative. A preemptive scheduler can interrupt a running task and switch to another task, while a cooperative scheduler requires the running task to voluntarily yield the CPU to another task.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their timing constraints, such as deadlines, response times, etc.
- A real-time kernel can be either hard or soft. A hard real-time kernel ensures that tasks will always meet their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel typically provides features such as task management, inter-task communication, synchronization, memory management, interrupt handling, etc.