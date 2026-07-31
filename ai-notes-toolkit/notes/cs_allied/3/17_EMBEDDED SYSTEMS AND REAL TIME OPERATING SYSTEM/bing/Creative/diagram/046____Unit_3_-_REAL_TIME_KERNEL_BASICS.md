## Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal and predictable delays .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports two types of tasks: periodic and aperiodic.
  - Periodic tasks are tasks that execute at regular intervals and have deadlines to meet.
  - Aperiodic tasks are tasks that execute in response to external events and have variable execution times.
- A real-time kernel provides mechanisms for task creation, deletion, synchronization, communication, scheduling, and resource management.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time.
  - Hard real-time kernels guarantee that all tasks meet their deadlines, even in the worst-case scenario.
  - Soft real-time kernels allow some tasks to miss their deadlines occasionally, but try to minimize the number and magnitude of deadline violations.
- A real-time kernel can be implemented in different ways, such as:
  - Modifying the standard kernel to reduce the latency and increase the responsiveness .
  - Developing a separate kernel that runs alongside the standard kernel and handles the real-time tasks .
  - Developing a microkernel that provides the minimal functionality and allows the user to customize the rest.
- A real-time kernel can be identified by executing the `uname -r` command on the terminal and looking for the `rt` keyword in the kernel version.