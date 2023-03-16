### Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a mechanism that determines which task or process should run on a processor at a given time.
- A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint.
- An open source RTOS is a RTOS that is freely available and can be modified and distributed by anyone.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, NuttX, and RIOT.
- These RTOSes differ in their features, such as scheduling, inter-process communication, memory management, and interrupt latency.
- Scheduling is the process of assigning priorities and time slots to tasks or processes that need to run on a processor.
- Scheduling can be cooperative or preemptive.
- Cooperative scheduling means that a task or process voluntarily gives up the processor when it is done or when it needs to wait for an event.
- Preemptive scheduling means that a task or process can be interrupted by the scheduler and replaced by another task or process with a higher priority.
- Some commonly used preemptive scheduling algorithms for RTOSes are rate-monotonic scheduling, round-robin scheduling, and fixed priority scheduling.
- Rate-monotonic scheduling assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- Round-robin scheduling assigns equal priorities to tasks and allocates them equal time slices in a circular order.
- Fixed priority scheduling assigns fixed priorities to tasks and runs the highest priority task that is ready.
- Fixed priority scheduling can be implemented with or without deferred preemption or non-preemption.
- Deferred preemption means that a task can only be preempted at certain points, such as when it calls a system service or when it blocks on a resource.
- Non-preemption means that a task cannot be preempted once it starts running until it finishes or blocks.
- The choice of scheduling algorithm depends on the requirements and characteristics of the application, such as the number of tasks, the deadlines, the criticality, the variability, and the synchronization.
- The scheduling algorithm affects the performance, predictability, and responsiveness of the RTOS and the application.