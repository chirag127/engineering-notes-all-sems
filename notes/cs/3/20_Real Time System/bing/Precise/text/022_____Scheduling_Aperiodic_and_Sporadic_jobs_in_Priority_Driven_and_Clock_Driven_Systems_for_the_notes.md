### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- **Aperiodic jobs** are tasks that do not have a regular arrival pattern and can arrive at any time.
- **Sporadic jobs** are tasks that have a minimum inter-arrival time between two consecutive jobs.
- **Priority-driven systems** assign priorities to tasks and schedule them based on their priorities.
- **Clock-driven systems** schedule tasks based on a pre-determined timetable.

#### Scheduling Aperiodic Jobs in Priority Driven Systems
- A common approach to scheduling aperiodic jobs in priority-driven systems is to use a **sporadic server**.
- A sporadic server is a high-priority task that is used to schedule aperiodic jobs.
- The sporadic server is assigned a **budget** and a **replenishment period**.
- When an aperiodic job arrives, it is executed by the sporadic server if the server has enough budget.
- The budget is replenished at the end of the replenishment period.

#### Scheduling Sporadic Jobs in Priority Driven Systems
- Sporadic jobs can be scheduled in priority-driven systems using the **Earliest Deadline First (EDF)** algorithm.
- The EDF algorithm assigns priorities to tasks based on their deadlines.
- The task with the earliest deadline is assigned the highest priority and is scheduled to execute first.

#### Scheduling Aperiodic and Sporadic Jobs in Clock Driven Systems
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using the **Time-Triggered Co-operative (TTC)** scheduling approach.
- The TTC approach schedules tasks based on a pre-determined timetable.
- Aperiodic and sporadic jobs are executed during **slack time** in the timetable.
- Slack time is the time that is not allocated to any periodic task.
