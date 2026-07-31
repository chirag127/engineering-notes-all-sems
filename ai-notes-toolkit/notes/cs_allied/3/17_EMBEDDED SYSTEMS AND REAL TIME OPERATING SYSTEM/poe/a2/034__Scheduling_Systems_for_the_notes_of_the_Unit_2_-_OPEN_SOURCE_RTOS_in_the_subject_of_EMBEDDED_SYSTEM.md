 Here is the content in markdown format without any emojis or external links:

### Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. Priority based scheduling:
- Tasks are assigned priorities.
- Higher priority task gets the CPU first.
- Starvation is possible for lower priority tasks.
- Implemented using priority queues.

2. Round Robin Scheduling:
- Each task gets the CPU for a fixed time quantum.
- After the time quantum expires, the task is preempted and added to the end of the queue.
- Ensures every task gets the CPU, but can lead to context switching overheads.
- Time quantum should be chosen carefully.

3. Earliest Deadline First Scheduling:
- Tasks are scheduled based on deadline.
- Task with earliest deadline is executed first.
- Good for real time systems with deadlines.
- Scheduling is dynamic based on deadline changes.

4. Rate Monotonic Scheduling:
- Task period is used to determine priority.
- Shorter period task gets higher priority.
- Works well for periodic real time tasks.
- Priority is static and determined a priori.

The content is written in points in a formal tone without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.