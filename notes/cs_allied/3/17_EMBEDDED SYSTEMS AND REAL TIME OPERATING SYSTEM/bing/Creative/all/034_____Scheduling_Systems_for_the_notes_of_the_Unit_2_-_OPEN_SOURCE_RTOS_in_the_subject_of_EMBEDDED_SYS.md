# Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a mechanism that determines which task or process should run on a processor at a given time, based on some criteria and constraints.
- A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint.
- An open source RTOS is a RTOS that has its source code available for anyone to inspect, modify, and enhance.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, RIOT, and NuttX.
- These RTOSes differ in their features, such as scheduling, inter-process communication, memory management, and interrupt latency.
- Some commonly used RTOS scheduling algorithms are:
  - Cooperative scheduling: tasks voluntarily yield the processor to other tasks when they are idle or waiting for an event.
  - Preemptive scheduling: tasks can be interrupted by the scheduler to run a higher priority task.
  - Rate-monotonic scheduling: tasks are assigned fixed priorities based on their periodic execution rates, with higher rates having higher priorities.
  - Round-robin scheduling: tasks with the same priority are executed in a circular order, with each task getting a fixed time slice of the processor.
  - Fixed priority pre-emptive scheduling: tasks are assigned fixed priorities and can be preempted by higher priority tasks, but not by lower priority tasks.
  - Fixed priority scheduling with deferred preemption: tasks are assigned fixed priorities and can be preempted by higher priority tasks, but only at certain preemption points within the task code.
  - Fixed priority non-preemptive scheduling: tasks are assigned fixed priorities and run to completion once they start, without being preempted by any other task.
- The choice of scheduling algorithm depends on the requirements and characteristics of the application, such as the number of tasks, the deadline constraints, the resource utilization, and the predictability of the system behavior.