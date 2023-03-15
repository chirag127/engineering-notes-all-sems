### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are tasks that do not have a regular arrival time and can arrive at any time.
- Sporadic jobs are tasks that have a minimum inter-arrival time between two consecutive jobs.
- Priority-driven systems assign priorities to jobs and schedule them based on their priorities.
- Clock-driven systems schedule jobs based on a pre-determined time table.
- In priority-driven systems, aperiodic and sporadic jobs can be scheduled using the slack stealing technique, where the scheduler steals the slack time from periodic tasks and assigns it to aperiodic and sporadic tasks.
- In clock-driven systems, aperiodic and sporadic jobs can be scheduled using the sporadic server technique, where a server task is created to handle the execution of aperiodic and sporadic tasks.
- The sporadic server has a pre-determined capacity and replenishment period, and can only execute aperiodic and sporadic tasks if it has enough capacity.
- The choice of scheduling technique for aperiodic and sporadic jobs depends on the specific requirements of the real-time system.
