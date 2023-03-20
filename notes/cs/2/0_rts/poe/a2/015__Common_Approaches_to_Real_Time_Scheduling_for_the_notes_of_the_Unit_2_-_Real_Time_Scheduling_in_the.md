 Here is the content in markdown format without any emojis or external links as per your instructions:

### Common Approaches to Real Time Scheduling

1. Rate Monotonic Scheduling (RMS):
- Assign priorities to tasks based on their period (task with shortest period gets highest priority)
- Guarantees scheduling of tasks if:
-- All tasks have deadline equal to their period
-- Tasks are independent
- Utilization bound = n(2^1/n - 1), where n is number of tasks

2. Deadline Monotonic Scheduling (DMS):
- Assign priorities to tasks based on their deadlines (task with shortest deadline gets highest priority)
- Guarantees scheduling of tasks if:
-- All tasks have deadlines less than or equal to their periods
-- Tasks are independent
- Generally has higher utilization than RMS for same task set

3. Earliest Deadline First (EDF):
- Assign priority to tasks based on closest deadline (task with nearest deadline gets highest priority)
- Optimal if preemptive scheduling is used (can schedule any set of independent tasks as long as utilization bound is not exceeded)
- However, non-preemptive EDF can lead to deadline misses even if utilization bound is not exceeded

4. Least Laxity First:
- Assign priority to tasks based on laxity (amount of time task can wait before deadline miss occurs)
- Effective for scheduling sporadic tasks (tasks with variable inter-arrival times)
- Preemptive version can schedule any set of independent sporadic tasks

The content is written in a formal tone with points in a list format as instructed. Let me know if you would like me to modify or expand the content in any way.