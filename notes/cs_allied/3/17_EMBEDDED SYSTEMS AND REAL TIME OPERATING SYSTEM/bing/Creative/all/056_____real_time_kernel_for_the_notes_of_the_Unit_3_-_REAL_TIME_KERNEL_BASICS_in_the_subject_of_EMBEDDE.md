# Real Time Kernel

A real time kernel is a software component that manages the time and resources of a CPU or MPU in a way that guarantees predictable and deterministic behavior. A real time kernel is also known as a real time operating system (RTOS) or a real time executive.

## Features of a Real Time Kernel

Some of the features of a real time kernel are:

- **Preemptive multitasking**: A real time kernel can switch between multiple tasks based on their priority and deadlines, and can interrupt a lower priority task to execute a higher priority task at any time.
- **Synchronization and communication**: A real time kernel provides mechanisms for tasks to synchronize and communicate with each other, such as semaphores, mutexes, message queues, event flags, etc.
- **Memory management**: A real time kernel can allocate and deallocate memory for tasks and data structures, and can prevent memory fragmentation and leaks.
- **Interrupt handling**: A real time kernel can handle hardware and software interrupts, and can assign priorities and handlers to them.
- **Timing services**: A real time kernel can provide accurate and reliable timing services, such as timers, delays, timeouts, etc.

## Types of Real Time Kernels

There are two main types of real time kernels:

- **Hard real time kernel**: A hard real time kernel guarantees that all tasks and interrupts will meet their deadlines, regardless of the system load and complexity. A hard real time kernel is suitable for applications that require strict timing constraints and high reliability, such as avionics, medical devices, robotics, etc.
- **Soft real time kernel**: A soft real time kernel tries to meet the deadlines of tasks and interrupts, but does not guarantee it. A soft real time kernel is suitable for applications that can tolerate some degree of latency and jitter, such as multimedia, gaming, networking, etc.

## Examples of Real Time Kernels

Some of the examples of real time kernels are:

- **FreeRTOS**: A free and open source real time kernel that supports various architectures and platforms, and provides a rich set of features and APIs.
- **Linux-rt**: A patch set that modifies the standard Linux kernel to make it more suitable for real time applications, by reducing the latency and improving the responsiveness of the kernel.
- **VxWorks**: A commercial real time kernel that is widely used in embedded and industrial systems, and offers high performance, scalability, and security.