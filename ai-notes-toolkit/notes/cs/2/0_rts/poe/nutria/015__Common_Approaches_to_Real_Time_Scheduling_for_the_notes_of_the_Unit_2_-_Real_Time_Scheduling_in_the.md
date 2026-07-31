
### Common Approaches to Real Time Scheduling

1. Fixed Priority Preemptive Scheduling: This approach assigns a priority to each task and the tasks are executed in order of their priority. A task with higher priority is allowed to preempt a task with lower priority.

2. Rate Monotonic Scheduling: This is a static priority scheduling algorithm which assigns priorities to the tasks based on their period. Tasks with shorter period have higher priority than tasks with longer period.

3. Earliest Deadline First Scheduling: This approach assigns priority to tasks based on their deadlines. The task with the earliest deadline is given the highest priority.

4. Least Laxity First Scheduling: This approach assigns priority to tasks based on their laxity. The task with the least laxity is given the highest priority. Laxity is the difference between the task's deadline and its estimated completion time.

5. Multilevel Feedback Queue Scheduling: This approach assigns priority to tasks based on the amount of CPU time they have used. Tasks that have used more CPU time are assigned lower priority than tasks that have used less CPU time.