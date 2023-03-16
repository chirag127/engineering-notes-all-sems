# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

## Introduction
- Aperiodic and sporadic jobs are types of tasks that do not have a fixed period or inter-arrival time.
- Aperiodic jobs have a soft deadline, while sporadic jobs have a hard deadline.
- Scheduling these types of jobs in real-time systems can be challenging, as their arrival times are unpredictable.

## Priority Driven Systems
- In priority-driven systems, tasks are assigned priorities based on their importance or urgency.
- Aperiodic and sporadic jobs can be scheduled using various techniques, such as the Slack Stealing algorithm, the Total Bandwidth Server algorithm, or the Deferrable Server algorithm.
- These algorithms aim to schedule aperiodic and sporadic jobs without affecting the schedulability of periodic tasks.

## Clock Driven Systems
- In clock-driven systems, tasks are scheduled based on a pre-determined schedule, which is calculated offline.
- Aperiodic and sporadic jobs can be scheduled using the Time-Triggered Co-Scheduling algorithm or the Cyclic Executive algorithm.
- These algorithms aim to schedule aperiodic and sporadic jobs within the available slack time in the pre-determined schedule.

## Conclusion
- Scheduling aperiodic and sporadic jobs in real-time systems can be challenging, but various techniques and algorithms have been developed to address this issue.
- The choice of algorithm depends on the type of system (priority-driven or clock-driven) and the specific requirements of the system.