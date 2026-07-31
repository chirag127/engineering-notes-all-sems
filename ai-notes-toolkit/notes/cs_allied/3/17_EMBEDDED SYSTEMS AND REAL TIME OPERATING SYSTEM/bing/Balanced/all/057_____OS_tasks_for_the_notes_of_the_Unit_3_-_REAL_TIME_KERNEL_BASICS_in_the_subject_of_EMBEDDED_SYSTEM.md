# OS Tasks for the Notes of the Unit 3 - Real Time Kernel Basics in the Subject of Embedded Systems and Real Time Operating Systems

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. A task is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the embedded OS that decides which task should run at any given time. The task scheduler can use different algorithms to make this decision, such as priority-based, round-robin, or preemptive.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their deadlines, which are the time constraints imposed by the application or the environment.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time. A hard real-time kernel ensures that tasks will never miss their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel can provide various services to tasks, such as task creation, deletion, synchronization, communication, and timing.