### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has two key features: predictability and determinism.

Some of the features of an RTOS are:

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources than a general-purpose operating system. This makes it suitable for embedded systems and devices with limited resources.
- **Fast response**: An RTOS is able to respond quickly and efficiently to events and interrupts, without significant delays or overheads. This is important for applications that require real-time feedback and control.
- **Deterministic behavior**: An RTOS ensures that tasks are executed as expected every time, without any variations or uncertainties. This is achieved by using strict scheduling algorithms, data buffers, or fixed task prioritization.
- **Co-operative or pre-emptive scheduling**: An RTOS can use either co-operative or pre-emptive scheduling to manage the execution of tasks. In co-operative scheduling, a task runs until it is completed or it voluntarily yields the processor to another task. In pre-emptive scheduling, a task can be interrupted by a higher-priority task at any time, and resumed later when the processor is available.
- **Main and background loops**: An RTOS can use a main and background loop structure to handle tasks. The main loop is responsible for executing the most critical and time-sensitive tasks, while the background loop handles the less urgent and non-real-time tasks. The main loop has higher priority than the background loop, and can pre-empt it if necessary.