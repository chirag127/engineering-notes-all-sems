# Features of RTOS

A real-time operating system (RTOS) is an operating system with two key features: **predictability** and **determinism**. This means that it will execute tasks quickly and efficiently, responding as expected every time within a tight time boundary. An RTOS is different from a general-purpose operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment. In an RTOS, processing time requirements need to be fully understood and bound rather than just kept as a minimum.

Some of the features of an RTOS are  :

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources, as it often runs on embedded systems with limited hardware capabilities.
- **Fast response**: An RTOS is able to handle interrupts and events with minimal latency and overhead, as it prioritizes the tasks that need to be executed in real time.
- **Preemptive scheduling**: An RTOS uses a preemptive scheduling algorithm, which means that each task has a unique priority value and the higher priority task can interrupt the lower priority task at any time. This ensures that the most urgent tasks are always executed first.
- **Cooperative scheduling**: An RTOS can also use a cooperative scheduling algorithm, which means that the task will run until the execution is completed or it voluntarily yields the control to another task. This reduces the context switching overhead and allows the tasks to cooperate with each other.
- **Main loop**: An RTOS can also use a main loop algorithm, which means that the tasks are executed in a sequential order in a loop, without any interruption or preemption. This is suitable for simple and periodic tasks that do not have strict timing constraints.
- **Inter-task communication**: An RTOS provides mechanisms for inter-task communication, such as message queues, semaphores, mutexes, events, signals, etc. These allow the tasks to exchange data, synchronize, and coordinate with each other.
- **Resource management**: An RTOS manages the allocation and deallocation of system resources, such as memory, CPU, I/O, etc. It ensures that the tasks have access to the resources they need and that the resources are not wasted or corrupted.
- **Error handling**: An RTOS handles the errors and exceptions that may occur during the execution of the tasks, such as memory faults, divide by zero, illegal instructions, etc. It provides mechanisms for error detection, recovery, and reporting.