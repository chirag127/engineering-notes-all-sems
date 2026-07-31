### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. It is created by the OS to encapsulate all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc.
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the OS that decides which task should run at any given time, based on factors such as priority, deadline, resource availability, etc.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their timing constraints, such as deadlines, response times, etc.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time.
- A hard real-time kernel ensures that tasks will always meet their deadlines, even in the worst-case scenario. A missed deadline can result in a catastrophic failure of the system.
- A soft real-time kernel allows some tasks to miss their deadlines occasionally, without compromising the overall functionality of the system. A missed deadline can result in a degraded performance of the system.
- A real-time kernel can use different scheduling algorithms to manage tasks, such as rate-monotonic, earliest deadline first, round-robin, etc.
- A real-time kernel can also provide features such as inter-task communication, synchronization, memory management, interrupt handling, etc.