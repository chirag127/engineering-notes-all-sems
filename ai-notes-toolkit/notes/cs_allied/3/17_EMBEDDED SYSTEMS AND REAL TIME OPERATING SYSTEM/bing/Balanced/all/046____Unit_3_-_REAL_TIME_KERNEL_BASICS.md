# Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal latency and jitter .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks.
- A real-time kernel supports different scheduling algorithms, such as priority-based, round-robin, or deadline-based, to assign CPU time to tasks.
- A real-time kernel provides mechanisms for inter-task communication and synchronization, such as semaphores, message queues, mutexes, and event flags.
- A real-time kernel can be classified into two types: hard real-time and soft real-time.
  - A hard real-time kernel guarantees that all tasks will meet their deadlines, regardless of the system load.
  - A soft real-time kernel tries to meet the deadlines of most tasks, but may occasionally miss some deadlines due to high system load or unpredictable events.
- A real-time kernel can be identified by the rt keyword in the kernel version, such as kernel-rt or preempt-rt.
- A real-time kernel is suitable for applications that require deterministic response times, such as telco, industrial automation, robotics, and gaming.