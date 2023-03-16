### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are tasks that do not have a regular arrival time and can arrive at any time.
- Sporadic jobs are tasks that have a minimum inter-arrival time between two consecutive jobs.
- In priority-driven systems, tasks are assigned priorities and the scheduler selects the highest priority task for execution.
- In clock-driven systems, the scheduler uses a pre-computed schedule to determine which task to execute at a given time.
- A common approach to scheduling aperiodic jobs in priority-driven systems is to use a server, such as a sporadic server or a deferrable server, to handle the execution of aperiodic jobs.
- A sporadic server assigns a priority to aperiodic jobs based on their arrival time and the minimum inter-arrival time of sporadic jobs.
- A deferrable server assigns a priority to aperiodic jobs based on their deadline and defers the execution of aperiodic jobs if higher priority periodic jobs are ready to execute.
- In clock-driven systems, aperiodic jobs can be scheduled using slack stealing, where the scheduler steals time from lower priority tasks to execute aperiodic jobs.
- Another approach to scheduling aperiodic jobs in clock-driven systems is to use a fixed pre-emptive schedule, where the scheduler pre-assigns time slots for the execution of aperiodic jobs.