Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Embedded Systems and Real Time Operating Systems. Here are some notes on the topic of Scheduling Systems for the notes of the Unit 2 - Open Source RTOS.

### Scheduling Systems for the notes of the Unit 2 - Open Source RTOS

- A scheduling system is a mechanism that determines which task or process should run on a processor at any given time, based on some criteria and policies.
- A real-time operating system (RTOS) is an operating system that guarantees a certain level of performance and responsiveness for time-critical applications.
- An open source RTOS is a RTOS that is freely available and can be modified and distributed by anyone, subject to the terms of the license.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, RIOT, and NuttX.
- These RTOSes differ in their features, such as scheduling, inter-process communication, memory management, and interrupt latency.
- Some commonly used RTOS scheduling algorithms are:
  - Cooperative scheduling: A task voluntarily yields the processor to another task when it is done or blocked. This is simple and predictable, but not suitable for high-priority tasks that need quick response.
  - Preemptive scheduling: A task can be interrupted by another task with higher priority at any time. This is more responsive and fair, but introduces overhead and complexity.
  - Rate-monotonic scheduling: A task is assigned a priority based on its period, the shorter the period, the higher the priority. This is optimal for periodic tasks with fixed deadlines, but not for aperiodic or dynamic tasks.
  - Round-robin scheduling: A task is given a fixed time slice to run, and then the processor is switched to the next task in a circular order. This is simple and fair, but not suitable for tasks with different priorities or deadlines.
  - Fixed priority pre-emptive scheduling: A task is assigned a fixed priority, and the processor is always given to the highest priority task that is ready to run. This is flexible and widely used, but may suffer from priority inversion or starvation.
  - Fixed priority scheduling with deferred preemption: A task is assigned a fixed priority, and the processor is given to the highest priority task that is ready to run, but a lower priority task can continue to run until it reaches a preemption point. This reduces the number of context switches and improves the performance, but may increase the response time of higher priority tasks.
  - Fixed priority non-preemptive scheduling: A task is assigned a fixed priority, and the processor is given to the highest priority task that is ready to run, but a lower priority task can continue to run until it finishes or blocks. This eliminates the overhead of context switches and interrupts, but may cause long delays for higher priority tasks.