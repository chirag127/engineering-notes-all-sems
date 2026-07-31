### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal delay and predictable response times .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A task is a piece of code that performs a specific function or service in the system.
- A task can have different states, such as ready, running, waiting, suspended, or terminated.
- A task can have different priorities, which determine the order of execution among the ready tasks.
- A real-time kernel provides services for creating, deleting, suspending, resuming, and communicating between tasks.
- A real-time kernel also provides services for managing system resources, such as memory, timers, interrupts, semaphores, queues, and events.
- A real-time kernel can be classified into two types: preemptive and cooperative.
- A preemptive kernel allows a higher priority task to interrupt a lower priority task and take over the CPU.
- A cooperative kernel requires a lower priority task to voluntarily relinquish the CPU to a higher priority task.
- A preemptive kernel is more suitable for real-time systems, as it provides better responsiveness and determinism.
- A real-time kernel can be further classified into two types: hard and soft.
- A hard real-time kernel guarantees that all tasks will meet their deadlines, regardless of the system load.
- A soft real-time kernel tries to meet the deadlines of most tasks, but may occasionally miss some deadlines due to high system load.
- A hard real-time kernel is more suitable for critical applications, such as aerospace, medical, or military systems.
- A soft real-time kernel is more suitable for non-critical applications, such as multimedia, gaming, or networking systems.