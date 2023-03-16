### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task (commonly referred to as a process in many embedded OSs) is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A task is only part of a program, as shown in Figure 1.

![Figure 1: OS task](https://www.edn.com/wp-content/uploads/media-2013/04/040213-EDN-FIGURE-9-7.jpg)

- A task can be in one of three states: running, ready, or blocked.
- Running means that the task is currently executing on the CPU.
- Ready means that the task is ready to run but is waiting for the CPU to be available.
- Blocked means that the task is waiting for some event to occur, such as an input/output operation or a timer expiration.
- A task can change its state by performing a system call, such as a request for a resource, a signal, or a delay.
- A task scheduler is a part of the OS that decides which task to run next on the CPU.
- A task scheduler can use different algorithms to determine the priority of tasks, such as round-robin, preemptive, or cooperative.
- A round-robin scheduler gives each task a fixed amount of time to run on the CPU and then switches to the next task in a circular order.
- A preemptive scheduler allows a higher-priority task to interrupt a lower-priority task and take over the CPU.
- A cooperative scheduler requires each task to voluntarily relinquish the CPU when it is done or when it is blocked.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their deadlines, which are the maximum acceptable delays for completing a task.
- A real-time kernel can be classified as either hard or soft, depending on the consequences of missing a deadline.
- A hard real-time kernel ensures that no deadline is ever missed, even in the worst-case scenario.
- A soft real-time kernel allows some deadlines to be missed occasionally, as long as the average performance is acceptable.
- A real-time kernel typically uses a preemptive scheduler with a priority-based algorithm to ensure that the most urgent tasks are executed first.
- A real-time kernel also provides mechanisms for synchronization, communication, and resource management among tasks.