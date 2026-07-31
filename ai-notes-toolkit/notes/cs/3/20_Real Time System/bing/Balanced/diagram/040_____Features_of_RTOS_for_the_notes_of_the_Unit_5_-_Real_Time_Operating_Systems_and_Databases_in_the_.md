### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has two key features: predictability and determinism.

Some of the features and advantages of an RTOS are  :

- It occupies very less memory and consumes fewer resources than a general-purpose operating system (GPOS).
- It is small, fast, responsive, and deterministic, meaning that it will execute tasks quickly and efficiently, responding as expected every time.
- It supports multitasking and multiprogramming, allowing multiple tasks to run concurrently and share system resources.
- It uses either co-operative scheduling or pre-emptive scheduling algorithms to manage the execution of tasks. Co-operative scheduling means that a task will run until it is completed or it voluntarily yields the CPU to another task. Pre-emptive scheduling means that a task can be interrupted by a higher-priority task at any time, and resume when the higher-priority task is finished.
- It provides mechanisms for inter-task communication and synchronization, such as message queues, semaphores, mutexes, and events.
- It offers real-time services, such as timers, clocks, interrupts, and device drivers, that can handle time-critical events and operations.
- It can handle hard real-time and soft real-time requirements. Hard real-time means that a task must meet its deadline, otherwise the system will fail. Soft real-time means that a task should meet its deadline, but occasional delays are acceptable.
- It can be customized and optimized for specific applications and hardware platforms, depending on the needs and constraints of the system.