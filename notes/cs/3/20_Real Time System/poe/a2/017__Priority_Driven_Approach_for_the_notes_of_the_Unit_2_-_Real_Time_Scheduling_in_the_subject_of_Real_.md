 Here is the content in Markdown format without any emojis or external links as specified:

### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

1. Priority driven approach is a preemptive scheduling algorithm where priority is assigned to each task. Higher priority task gets precedence over lower priority task.
2. In this approach, scheduler selects the task with the highest priority from ready queue and allocates CPU to it.
3. If a new task with higher priority than running task arrives, then running task is preempted and higher priority task is executed. This is called preemptive scheduling.
4. Priority inversion problem can occur in this approach. It refers to lower priority task holding CPU and delaying execution of higher priority task. Several techniques like priority inheritance, priority ceiling are used to avoid this problem.
5. Rate monotonic scheduling is a priority assignment scheme under this approach where priorities are assigned based on task periods. Shorter period tasks get higher priorities. It works well for periodic real time tasks.
6. Deadline monotonic scheduling is another scheme where priorities are assigned based on deadlines of tasks. Task with shortest deadline gets highest priority. It can handle aperiodic real time tasks more efficiently than rate monotonic scheduling.

The above content summarizes the key points about Priority Driven approach for Real Time Scheduling. The points are written in brief in a formal tone as specified without any emotions or friendliness. The content is written in Markdown format with headings and points.