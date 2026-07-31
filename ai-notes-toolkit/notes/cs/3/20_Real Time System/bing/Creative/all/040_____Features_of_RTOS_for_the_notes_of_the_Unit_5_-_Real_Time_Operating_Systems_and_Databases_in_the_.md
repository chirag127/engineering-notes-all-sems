# Features of RTOS

A real-time operating system (RTOS) is an operating system with two key features: predictability and determinism. This means that it can guarantee that a certain task will be completed within a specified time limit, regardless of the system load or other factors. Some of the features and advantages of an RTOS are:

- **Small and fast**: An RTOS is designed to occupy very less memory and consume fewer resources, making it suitable for embedded systems and devices with limited hardware capabilities.
- **Responsive**: An RTOS can respond quickly to external events and interrupts, without significant delays or overheads.
- **Deterministic**: An RTOS can ensure that the same task will always take the same amount of time to execute, regardless of the system state or other tasks.
- **Scalable**: An RTOS can support the addition of new features and capabilities to products as market needs evolve, while leveraging the existing code base and hardware platform.
- **Reliable**: An RTOS can provide fault tolerance and error handling mechanisms to ensure the system's functionality and safety in case of failures or malfunctions.

Some of the common types of RTOS are:

- **Co-operative scheduling**: In this type of RTOS, the tasks run until they are completed or they voluntarily yield the CPU to another task. The kernel can only be set up in one way, and the tasks have equal priority.
- **Pre-emptive scheduling**: In this type of RTOS, each task has a unique priority value, and the scheduler always runs the highest priority task that is ready. The tasks can be pre-empted by higher priority tasks or interrupts at any time.
- **Time-slicing**: In this type of RTOS, the tasks have equal priority, but the scheduler assigns a fixed time slice to each task. The tasks are executed in a round-robin fashion, and the scheduler switches to the next task when the time slice expires or the current task yields the CPU.

Some of the examples of RTOS are:

- **Wind River VxWorks**: This is a commercial RTOS that supports a wide range of architectures and platforms, and provides features such as security, networking, graphics, and IoT connectivity.
- **FreeRTOS**: This is an open source RTOS that is designed for microcontrollers and small embedded systems, and provides features such as task management, timers, queues, and semaphores.
- **Linux**: This is a general-purpose operating system that can be configured to run in real-time mode, by using patches such as PREEMPT_RT or Xenomai, or by using a co-kernel such as RTAI or RTLinux.