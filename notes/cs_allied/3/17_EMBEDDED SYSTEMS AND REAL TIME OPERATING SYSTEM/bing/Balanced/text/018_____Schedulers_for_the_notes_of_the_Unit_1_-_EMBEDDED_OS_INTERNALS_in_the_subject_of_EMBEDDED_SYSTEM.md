### Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is the software that determines which task should be run next by the processor in an embedded system.
- A scheduling algorithm is the logic and the mechanism that decides when the scheduler should be run and how to allocate the processor time among the tasks.
- Scheduling is a crucial aspect of embedded systems, especially for real-time systems that need to meet deadlines and ensure system stability.
- There are different types of schedulers and scheduling algorithms, depending on the system requirements, the task characteristics, and the design choices.
- Some of the common types of schedulers are:

  - Time Slice (TS) Scheduler: This scheduler divides the time into slots and assigns each task a slot to execute. The tasks are executed in a round-robin fashion, meaning that each task gets a turn to run for the duration of its slot. This scheduler is simple and fair, but it does not consider the priority or the deadline of the tasks.
  - Priority Scheduler: This scheduler assigns a priority level to each task and runs the task with the highest priority at any given time. The priority can be static (fixed at design time) or dynamic (changing at run time). This scheduler can improve the responsiveness and the performance of the system, but it may also cause starvation (a situation where a low-priority task never gets to run) or deadlock (a situation where two or more tasks are waiting for each other to finish).
  - Composite Scheduler: This scheduler combines the features of the TS and the priority schedulers. It uses a priority queue to store the ready tasks and assigns them time slots based on their priority. The tasks with the same priority are executed in a round-robin fashion. This scheduler can balance the trade-offs between fairness and efficiency, but it may also increase the complexity and the overhead of the system.

- Some of the common types of scheduling algorithms are:

  - Preemptive Scheduling: This algorithm allows the scheduler to interrupt the running task and switch to a higher-priority task when it becomes ready. This algorithm can improve the responsiveness and the predictability of the system, but it may also increase the context switching cost and the synchronization challenges.
  - Non-Preemptive Scheduling: This algorithm does not allow the scheduler to interrupt the running task until it finishes or blocks. This algorithm can reduce the context switching cost and the synchronization challenges, but it may also degrade the responsiveness and the predictability of the system.
  - Cooperative Scheduling: This algorithm relies on the tasks to voluntarily yield the processor to the scheduler when they are done or waiting for an event. This algorithm can simplify the design and the implementation of the system, but it may also require the tasks to be well-behaved and cooperative.