## Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal and predictable delays .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports two types of tasks: periodic and aperiodic.
  - Periodic tasks are tasks that execute at regular intervals and have deadlines to meet.
  - Aperiodic tasks are tasks that execute in response to external events and have variable execution times.
- A real-time kernel provides mechanisms for task creation, scheduling, synchronization, communication, and termination.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time.
  - Hard real-time kernels guarantee that all tasks meet their deadlines, even in the worst-case scenario.
  - Soft real-time kernels allow some tasks to miss their deadlines occasionally, but try to minimize the number and magnitude of deadline violations.
- A real-time kernel can be implemented in different ways, such as modifying the standard kernel, adding a real-time layer to the standard kernel, or using a separate real-time kernel .
  - Modifying the standard kernel involves changing the kernel source code to reduce the latency and increase the responsiveness of the system.
  - Adding a real-time layer to the standard kernel involves inserting a module between the kernel and the hardware that intercepts and prioritizes the real-time events.
  - Using a separate real-time kernel involves running a dedicated kernel on a separate core or processor that handles the real-time tasks exclusively.