 Here is the content in markdown format without any emojis or external links and in formal tone:

### Reference Models for Real Time Systems

1. Rate Monotonic Analysis Model: This model is used for scheduling the tasks based on their period or frequency. The task with the shortest period gets the highest priority. This model is suitable for independent periodic tasks with fixed priority.
2. Deadline Monotonic Model: This model assigns priorities to tasks based on their deadlines. The task with the shortest relative deadline gets the highest priority. This model can be used for constrained deadlined systems to meet the deadlines.
3. Earliest Deadline First Model: In this model, the task with the earliest absolute deadline gets the highest priority at any time. The priority of a task changes dynamically based on the deadlines of other tasks. This model provides better responsiveness and can meet more deadlines but scheduling overhead is more.
4. Critical Instant Model: This model analyzes the system's behavior at critical instants which are points in time where multiple tasks request for CPU simultaneously. By showing the system is schedulable at critical instants, it can be ensured that the system is schedulable for all time. This model can be used for fixed priority as well as dynamic priority scheduling.

The above reference models can be used to analyze, evaluate and compare the performance of different real time scheduling algorithms based on parameters like CPU utilization, percentage of missed deadlines, fairness, etc. The choice of a suitable model for a real time system depends on the task characteristics and system requirements.