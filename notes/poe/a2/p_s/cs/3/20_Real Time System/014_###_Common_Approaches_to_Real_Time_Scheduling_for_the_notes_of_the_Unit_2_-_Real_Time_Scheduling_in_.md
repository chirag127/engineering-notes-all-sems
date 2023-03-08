 Here is the content in markdown format for the topic ### Common Approaches to Real Time Scheduling for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System:

### Fixed Priority Scheduling
- In fixed priority scheduling, each task is assigned a fixed priority.
- The scheduler chooses the task with the highest priority from the ready queue and allocates the CPU to it.
- If two tasks have the same priority, Round-Robin scheme is used.
- The priority can be assigned based on factors like criticality of the task.
- Advantage: simple to implement.
- Disadvantage: priority inversion problem can occur.

### Earliest Deadline First (EDF)
- In EDF, the task with the earliest deadline is given the highest priority.
- The scheduler picks the task with the earliest deadline from the ready queue and allocates the CPU to it.
- If multiple tasks have the same deadline, Round-Robin scheme can be used.
- Superior as it can theoretically achieve 100% CPU utilization.
- Difficult to implement as deadlines must be constantly re-calculated and sorted.

### Rate Monotonic Scheduling (RMS)
- In RMS, priorities are assigned based on task periodicity.
- Task with smallest period gets the highest priority.
- It is optimal if all tasks have CPU utilization below a certain threshold.
- Easy to implement as task set is static and priorities are pre-assigned.
- Suffers from priority inversion.

[Additional details, diagrams, examples, applications, advantages, disadvantages, etc can be added here for the given points to make the content more explanatory and helpful for learning and exams.]