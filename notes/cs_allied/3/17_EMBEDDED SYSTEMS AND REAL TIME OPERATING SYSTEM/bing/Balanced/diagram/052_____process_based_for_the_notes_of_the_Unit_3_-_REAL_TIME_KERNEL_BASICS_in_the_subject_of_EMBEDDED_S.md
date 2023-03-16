### Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel can run on different CPU architectures and even on low-end 8 or 16-bit CPUs or DSP chips.
- A real-time kernel can provide deterministic and predictable behavior for time-critical applications.
- A real-time kernel can be classified into two types: hard real-time and soft real-time.
  - Hard real-time kernels guarantee that tasks will meet their deadlines, even in the worst-case scenario.
  - Soft real-time kernels try to meet the deadlines of tasks, but do not guarantee it. They can tolerate some degree of latency or jitter.
- A real-time kernel can be implemented in two ways: as a kernel model or as a user space model.
  - In a kernel model, the real-time kernel is integrated into the Linux kernel and replaces the standard scheduler.
  - In a user space model, the real-time kernel runs as a user space program and communicates with the Linux kernel through a device driver.
- A real-time kernel can provide various services and features, such as :
  - Task management: creating, deleting, suspending, resuming, and prioritizing tasks.
  - Time management: measuring, delaying, and triggering tasks based on time.
  - Resource management: allocating, freeing, and sharing resources among tasks, such as memory, semaphores, mutexes, message queues, etc.
  - Interrupt management: handling, masking, and unmasking interrupts from hardware devices.
  - Debugging and profiling: monitoring, tracing, and analyzing the performance and behavior of tasks and the kernel.