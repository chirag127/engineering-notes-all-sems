### Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, especially for applications that have strict timing constraints or deadlines.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel provides a set of services or APIs (Application Programming Interfaces) that allow the application to create, manage, and synchronize tasks, which are the basic units of execution in a real-time system.
- A real-time kernel can be classified into two types: preemptive and cooperative.
  - A preemptive kernel allows a task to be interrupted by a higher priority task at any time, thus ensuring that the most urgent task always gets the CPU.
  - A cooperative kernel requires a task to voluntarily relinquish the CPU to another task, thus avoiding the overhead of context switching but risking missing deadlines if a task does not cooperate.
- A real-time kernel can also be distinguished by the number of priority levels it supports for the tasks.
  - A fixed-priority kernel assigns a unique priority level to each task, and always schedules the highest priority ready task.
  - A dynamic-priority kernel can change the priority level of a task based on some criteria, such as the deadline or the execution time.
- A real-time kernel can be implemented in different ways, such as in the kernel space or in the user space of the operating system.
  - A kernel space implementation modifies the original kernel to support real-time features, such as reducing the latency or adding the real-time scheduler.
  - A user space implementation runs the real-time kernel as a separate process that communicates with the original kernel through a device driver or a shared memory.
- A real-time kernel can be identified by the rt keyword in the kernel version, which can be obtained by executing the uname -r command on the terminal.
- A real-time kernel can be used for various applications that require high performance, reliability, and predictability, such as industrial control, robotics, multimedia, gaming, and scientific computing .