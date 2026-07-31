### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a unit of execution that is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the OS that decides which task should run at any given time based on priority, deadlines, resources, etc..
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their timing constraints, such as deadlines, response times, or execution times.
- A real-time kernel can be either preemptive or cooperative, depending on whether it allows a higher priority task to interrupt a lower priority task or not.
- A real-time kernel can also be either hard or soft, depending on whether missing a deadline is considered a critical failure or not.
- A real-time kernel provides services such as task management, synchronization, communication, memory management, interrupt handling, etc..