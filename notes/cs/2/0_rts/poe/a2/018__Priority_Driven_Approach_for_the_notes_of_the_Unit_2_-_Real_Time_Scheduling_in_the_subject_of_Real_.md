 Here is the content in Markdown format without any emojis or external links as per your instructions:

### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

1. In priority driven preemptive scheduling, each task is assigned a priority. Higher priority tasks are scheduled first. If a lower priority task is running and a higher priority task arrives, the lower priority running task is preempted and the higher priority task is scheduled.
2. Priority can be assigned statically or dynamically.
3. In static priority assignment, priorities are assigned to tasks based on the criticality/importance of the task and do not change with time.
4. In dynamic priority assignment, the priority of a task changes with time based on factors like deadline, latency, resource usage, etc. This is useful in overloaded systems where not all tasks can meet their deadlines. The priorities can be adjusted dynamically to increase the likelihood of more critical tasks meeting their deadlines.
5. Priority inversion: A higher priority task waits for a lower priority task to complete due to shared resources. This can be avoided using priority inheritance protocol.
6. The rate monotonic scheduling algorithm is a static priority driven preemptive scheduling algorithm where priorities are assigned based on task periods. Shorter period tasks get higher priority. This algorithm is optimal if the task set is independent and periodic.

The above content is written in a formal tone with points and without any emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the content in any way.