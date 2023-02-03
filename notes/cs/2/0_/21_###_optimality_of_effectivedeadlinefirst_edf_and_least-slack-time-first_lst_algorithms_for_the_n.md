### Optimality of EffectiveDeadlineFirst (EDF) and Least-Slack-Time-First (LST) Algorithms for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

EffectiveDeadlineFirst (EDF) and Least-Slack-Time-First (LST) are two popular algorithms used in real-time scheduling.

EDF:
- assigns tasks to the processor based on the task with the earliest deadline.
- If two tasks have the same deadline, the task with the highest priority is assigned first.
- EDF is optimal for tasks with non-preemptive deadlines, meaning that once a task starts, it cannot be interrupted until it finishes.
- EDF ensures that all tasks are completed before their deadlines and minimizes the number of missed deadlines.

LST:
- assigns tasks to the processor based on the task with the least amount of time remaining until its deadline.
- If two tasks have the same amount of time remaining, the task with the highest priority is assigned first.
- LST is optimal for tasks with preemptive deadlines, meaning that a task can be interrupted and resumed later if a higher priority task becomes available.
- LST ensures that the processor is never idle and minimizes the total amount of time it takes to complete all tasks.

Both algorithms have their advantages and disadvantages and the choice of which one to use depends on the specific requirements of the real-time system.
