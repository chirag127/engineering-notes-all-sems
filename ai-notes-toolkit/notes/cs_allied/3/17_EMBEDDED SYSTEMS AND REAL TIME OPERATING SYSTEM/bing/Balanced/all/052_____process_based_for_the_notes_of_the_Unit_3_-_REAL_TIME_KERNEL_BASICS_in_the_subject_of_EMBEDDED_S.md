# Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, especially for applications that have strict timing constraints.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel can provide features such as multitasking, inter-task communication, synchronization, memory management, and interrupt handling.
- A real-time kernel can be classified into two types: preemptive and cooperative.
  - A preemptive kernel allows a task to be interrupted by a higher priority task at any time, thus ensuring that the highest priority task is always running.
  - A cooperative kernel requires a task to voluntarily relinquish the CPU to allow other tasks to run, thus avoiding the overhead of context switching.
- A real-time kernel can also be distinguished by the level of determinism it provides.
  - A hard real-time kernel guarantees that a task will meet its deadline, regardless of the system load or the occurrence of interrupts.
  - A soft real-time kernel tries to meet the deadlines of tasks, but does not guarantee it, and may tolerate some degree of latency or jitter.
- A real-time kernel can be implemented in different ways, such as in kernel space or in user space.
  - A kernel space real-time kernel runs as part of the operating system, and has direct access to the hardware and the system resources.
  - A user space real-time kernel runs as a separate process, and relies on the operating system to provide access to the hardware and the system resources.
- A real-time kernel can be used for various applications, such as industrial control, robotics, multimedia, gaming, and embedded systems  .