### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Scheduling Aperiodic and Sporadic Jobs in Priority Driven Systems:
1. Aperiodic jobs: These are jobs that arrive at random times and have no set arrival rate. They are usually assigned lower priority than periodic tasks to ensure their execution does not interfere with critical tasks.
2. Sporadic jobs: These are jobs with infrequent and unpredictable arrival times that require immediate processing. They are usually assigned the highest priority to ensure their processing is not delayed.
3. Priority Driven Systems: In these systems, tasks are assigned priorities based on their criticality and urgency. Tasks with higher priority are executed first and those with lower priority are executed later. 

Scheduling Aperiodic and Sporadic Jobs in Clock Driven Systems:
1. Aperiodic jobs: These jobs are executed in a time-sharing mode with periodic tasks. They are executed only when no periodic task is executing.
2. Sporadic jobs: These jobs are executed immediately, even if a periodic task is executing. They have higher priority than periodic tasks and are executed first.
3. Clock Driven Systems: In these systems, tasks are executed in a cyclic fashion based on a pre-defined schedule. Tasks are executed in a time-sharing mode, with the length of each task’s execution time determined by its priority.
