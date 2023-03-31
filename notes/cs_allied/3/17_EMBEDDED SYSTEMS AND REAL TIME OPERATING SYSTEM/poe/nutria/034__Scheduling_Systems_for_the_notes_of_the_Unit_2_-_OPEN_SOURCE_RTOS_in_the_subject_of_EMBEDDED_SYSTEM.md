
### Scheduling Systems for Unit 2 - OPEN SOURCE RTOS

* Preemptive Scheduling: In preemptive scheduling, a task can be interrupted at any point in time by a higher priority task. This type of scheduling is used in real-time systems where response time is critical.
* Round-Robin Scheduling: Round-robin scheduling is a scheduling algorithm in which each task is assigned a fixed time slot in a cyclic way. It is simple, easy to implement, and starvation-free.
* Priority Scheduling: In priority scheduling, tasks are assigned priority numbers. The task with the highest priority is executed first. If two tasks have the same priority, then they are executed in a round-robin fashion.
* Rate Monotonic Scheduling: Rate monotonic scheduling is a priority-based scheduling algorithm. It assigns priority to each task based on its rate of execution. Tasks with higher rates get higher priority.
* Deadline Scheduling: Deadline scheduling is a scheduling algorithm in which each task is assigned a deadline. Tasks with shorter deadlines are executed first. This type of scheduling is used in real-time systems.