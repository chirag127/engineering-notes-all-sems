# Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is the software that determines which task should be run next by the processor in an embedded system.
- A scheduling algorithm is the logic and the mechanism that decides when the scheduler should be run and how to allocate the processor time among the tasks.
- Scheduling is a crucial aspect of embedded systems, especially for real-time systems that need to meet deadlines and ensure system stability.
- There are different types of schedulers and scheduling algorithms, depending on the system requirements, the task characteristics, and the design trade-offs.
- Some of the common types of schedulers are:

  - Time Slice (TS) Scheduler: This scheduler divides the time into slots and assigns each task a slot to execute. The tasks are executed in a round-robin fashion, meaning that each task gets a turn to run for the duration of its slot. This scheduler is simple and fair, but it does not consider the priority or the deadline of the tasks.
  - Priority Scheduler: This scheduler assigns a priority level to each task and runs the task with the highest priority at any given time. The priority can be static (fixed at design time) or dynamic (changing at run time). This scheduler can improve the responsiveness and the performance of the system, but it may also cause starvation (a situation where a low-priority task never gets to run) or priority inversion (a situation where a high-priority task is blocked by a low-priority task).
  - Composite Scheduler: This scheduler combines the features of the TS and the priority schedulers. It can use a priority-based algorithm to select a group of tasks to run, and then use a TS algorithm to run the tasks within the group. This scheduler can balance the advantages and disadvantages of the TS and the priority schedulers.

- Some of the common types of scheduling algorithms are:

  - Preemptive Scheduling: This algorithm allows the scheduler to interrupt the execution of a task and switch to another task, if the new task has a higher priority or a shorter deadline. This algorithm can improve the responsiveness and the timeliness of the system, but it also increases the overhead and the complexity of the scheduler.
  - Non-Preemptive Scheduling: This algorithm does not allow the scheduler to interrupt the execution of a task, unless the task voluntarily yields the processor or completes its execution. The scheduler can only select a new task when the current task is finished or suspended. This algorithm reduces the overhead and the complexity of the scheduler, but it also reduces the responsiveness and the timeliness of the system.
  - Cooperative Scheduling: This algorithm relies on the tasks to cooperate with the scheduler and yield the processor when they are idle or waiting for an event. The scheduler can only select a new task when the current task yields the processor. This algorithm is simple and efficient, but it also requires the tasks to be well-designed and well-behaved.

- Scheduling is a trade-off between the system performance, the system complexity, and the system predictability. Different schedulers and scheduling algorithms have different strengths and weaknesses, and the choice of the best scheduler and scheduling algorithm depends on the system requirements, the task characteristics, and the design constraints.