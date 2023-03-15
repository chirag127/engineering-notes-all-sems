### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- **Aperiodic jobs** are tasks that do not have a regular arrival pattern and can arrive at any time.
- **Sporadic jobs** are tasks that have a minimum inter-arrival time between two consecutive jobs.
- **Priority-driven systems** assign priorities to tasks and schedule them based on their priorities.
- **Clock-driven systems** schedule tasks based on a pre-determined timetable.

#### Scheduling Aperiodic Jobs in Priority Driven Systems
- In priority-driven systems, aperiodic jobs can be scheduled using one of the following methods:
  - **Background**: Aperiodic jobs are assigned the lowest priority and are executed only when no other higher priority jobs are ready to execute.
  - **Polling Server**: A periodic task, called a polling server, is introduced with a fixed capacity. The server is used to execute aperiodic jobs whenever it has available capacity.
  - **Deferrable Server**: Similar to the polling server, but the server can defer its capacity to the next period if no aperiodic jobs are ready to execute.
  - **Sporadic Server**: Similar to the deferrable server, but the server can also reclaim unused capacity from the previous period.

#### Scheduling Sporadic Jobs in Priority Driven Systems
- In priority-driven systems, sporadic jobs can be scheduled using the sporadic server method mentioned above.

#### Scheduling Aperiodic and Sporadic Jobs in Clock Driven Systems
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using the **Time-Triggered** approach, where a fixed time slot is reserved for the execution of aperiodic and sporadic jobs.
- Another approach is the **Slack Stealing** method, where the system dynamically adjusts the schedule to accommodate aperiodic and sporadic jobs by utilizing the slack time available in the schedule.
