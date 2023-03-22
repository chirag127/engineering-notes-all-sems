### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Real-time scheduling is one of the major components of real-time systems. It involves scheduling tasks in a way that meets the timing constraints of the system. Priority-driven approaches are commonly used in real-time scheduling. Here are some key points to keep in mind about the priority-driven approach:

- Priority-driven scheduling is based on assigning priorities to tasks. The higher the priority, the more important the task is considered to be.
- Tasks with higher priorities are scheduled before tasks with lower priorities.
- The priority of a task can be fixed or dynamic. In fixed priority scheduling, the priorities are assigned statically and do not change during runtime. In dynamic priority scheduling, the priorities can change during runtime based on various factors such as the task's execution history or the system load.
- Priority-driven scheduling can be preemptive or non-preemptive. In preemptive scheduling, a higher priority task can interrupt a lower priority task that is currently executing. In non-preemptive scheduling, a task continues to execute until it completes or blocks, even if a higher priority task becomes ready to execute.
- Priority inversion is a common problem in priority-driven scheduling. It occurs when a low-priority task holds a resource that a high-priority task needs, causing the high-priority task to be blocked. To avoid priority inversion, techniques such as priority inheritance or priority ceiling can be used.
- Priority-driven scheduling can be implemented using various algorithms such as Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), or Deadline Monotonic Scheduling (DMS).

Understanding the priority-driven approach is crucial for designing and analyzing real-time systems. By appropriately assigning priorities to tasks, real-time systems can meet their timing constraints and provide reliable performance.