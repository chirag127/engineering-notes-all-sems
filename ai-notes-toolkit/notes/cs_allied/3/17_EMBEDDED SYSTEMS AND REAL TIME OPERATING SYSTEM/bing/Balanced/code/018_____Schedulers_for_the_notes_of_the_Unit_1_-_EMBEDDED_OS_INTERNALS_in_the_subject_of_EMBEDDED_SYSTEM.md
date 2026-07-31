### Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is the software that determines which task should be run next by the processor in an embedded system.
- A scheduling algorithm is the logic and the mechanism that decides when the scheduler should be run and which task should be selected.
- Scheduling algorithms can be classified into two categories: preemptive and non-preemptive.
  - Preemptive scheduling allows a higher priority task to interrupt a lower priority task that is currently running and take over the processor.
  - Non-preemptive scheduling does not allow a lower priority task to be interrupted by a higher priority task once it starts running.
- Some common types of schedulers in embedded systems are:
  - Round Robin (RR) scheduler: A simple scheduler that gives each task a fixed amount of processor time in a circular order.
  - Time Slice (TS) scheduler: A scheduler that divides time into slots and assigns each task a slot based on its priority.
  - Priority scheduler: A scheduler that always selects the task with the highest priority to run next.
  - Composite scheduler: A scheduler that combines different scheduling algorithms to achieve the best performance and meet the system requirements.
- Schedulers in embedded systems must also consider the real-time constraints and deadlines of the tasks, as well as the resource utilization and power consumption of the system.
- Schedulers can be implemented using different techniques, such as function pointers, state machines, or real-time operating systems (RTOS).