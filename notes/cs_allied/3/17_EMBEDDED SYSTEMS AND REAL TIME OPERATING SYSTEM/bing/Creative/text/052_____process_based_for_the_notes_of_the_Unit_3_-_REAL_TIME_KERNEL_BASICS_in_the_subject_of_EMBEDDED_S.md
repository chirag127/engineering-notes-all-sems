### Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, especially for applications that have strict timing constraints.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel can provide features such as multitasking, inter-task communication, synchronization, memory management, and interrupt handling.
- A real-time kernel can be classified into two types: preemptive and cooperative.
  - A preemptive kernel allows a task to be interrupted by a higher priority task at any time, ensuring that the most urgent task is always executed first.
  - A cooperative kernel requires a task to voluntarily relinquish the CPU to allow other tasks to run, which simplifies the design but may cause delays or missed deadlines.
- A real-time kernel can also be distinguished by the level of determinism it provides.
  - A hard real-time kernel guarantees that a task will meet its deadline under all circumstances, even in the presence of interrupts or system faults.
  - A soft real-time kernel tries to meet the deadlines of most tasks, but may occasionally miss some due to unpredictable events or overload.
- A real-time kernel can be implemented in different ways, such as in the kernel space or in the user space.
  - A kernel space real-time kernel is integrated into the core of the operating system, and has direct access to the hardware and the system resources.
  - A user space real-time kernel is a separate module that runs on top of the operating system, and uses system calls or libraries to interact with the hardware and the system resources.
- A kernel space real-time kernel has advantages such as faster performance, lower overhead, and higher reliability, but also disadvantages such as higher complexity, lower portability, and higher risk of system crashes.
- A user space real-time kernel has advantages such as simpler design, higher portability, and lower risk of system crashes, but also disadvantages such as slower performance, higher overhead, and lower reliability.
- A user space real-time kernel can also use the real-time API and the whole Linux API, but cannot be scheduled by the real-time scheduler when using the Linux API.