 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Graph Based Models

1. Rate Monotonic Analysis
- Assign priorities to tasks based on their period
- Task with shortest period gets highest priority
- Guarantees feasible schedule if tasks are independent and priority assigned using rate monotonic priority assignment
- Not optimal in terms of CPU utilization

2. Deadline Monotonic Analysis
- Assign priorities to tasks based on their deadlines
- Task with shortest deadline gets highest priority
- Guarantees feasible schedule if deadlines are constrained deadlines and priority assigned using deadline monotonic priority assignment
- Can lead to priority inversion

3. Audsley's Optimal Priority Assignment Algorithm
- Finds optimal priority assignment for a set of tasks to maximize CPU utilization
- Complex algorithm with high computational requirements
- Guarantees optimal solution if one exists

4. Earliest Deadline First (EDF) Scheduling
- Tasks are scheduled in order of shortest deadline
- Does not require fixed task priorities
- Optimal if deadlines are constrained deadlines
- Can lead to priority inversion and is not bandwidth preserving

5. Least Laxity First (LLF) Scheduling
- Tasks are scheduled based on least laxity (deadline - completion time)
- Also a dynamic priority scheduling algorithm like EDF
- Can suffer from priority inversion

The above points cover the key graph based models for real time task scheduling. The models have their own pros and cons in terms of schedulability, CPU utilization and susceptibility to priority inversion. The requirements of the application and system constraints can help choose a suitable model for scheduling real time tasks.