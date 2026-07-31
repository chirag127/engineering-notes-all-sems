 Here is the content in markdown format without any emojis or external links and in formal tone:

### Reference Models for Real Time Systems

1. Rate Monotonic Scheduling Model:
- In this model, priorities are assigned to tasks based on their periodicity. Task with shortest period gets highest priority.
- It is optimal if deadlines are equal to periods and all tasks are periodic.
- Guarantees feasibility but may lead to poor CPU utilization.

2. Deadline Monotonic Scheduling Model:
- In this model, priorities are assigned to tasks based on their deadlines. Task with shortest deadline gets highest priority.
- It guarantees feasibility for a larger set of task parameters than RMS model but response times may increase for some tasks.

3. Earliest Deadline First Scheduling Model:
- In this model, ready task with earliest deadline is given highest priority.
- It leads to good CPU utilization but does not provide guarantees on missing deadlines.
- Scheduling is dynamic and preemptive based on changing deadlines.

4. Fixed Priority Scheduling Model:
- In this model, each task is assigned a fixed priority and ready task with highest priority is executed first.
- It is simple to implement but may lead to priority inversion problems. Deadlines may be missed for lower priority tasks.

The above reference models can be used for assigning priorities to tasks in a real time system and ensure their timely execution as per specified deadlines. An appropriate model can be chosen based on the nature of the real time tasks and desired performance goals.