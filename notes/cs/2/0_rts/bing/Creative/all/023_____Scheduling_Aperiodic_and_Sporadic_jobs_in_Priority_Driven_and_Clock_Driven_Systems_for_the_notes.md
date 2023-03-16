# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job to execute at any time. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign fixed time slots to jobs based on their arrival patterns and execution times. The scheduler follows a pre-computed schedule that is determined offline. Examples are cyclic executive, time triggered, etc.

## Scheduling Aperiodic and Sporadic jobs in Priority Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in priority driven systems: background scheduling and slack stealing.

### Background Scheduling

- Background scheduling is a simple and intuitive approach that assigns the lowest priority to aperiodic jobs and executes them only when there are no periodic or sporadic jobs ready to run. This ensures that aperiodic jobs do not interfere with the schedulability of periodic and sporadic jobs, but it also results in poor responsiveness of aperiodic jobs, especially when the system is heavily loaded with periodic and sporadic jobs.
- Background scheduling can be improved by using a server task, which is a periodic task that reserves a portion of the processor time for aperiodic jobs. The server task has a fixed priority and a fixed budget, and it replenishes its budget periodically. When the server task is ready to run, it executes the aperiodic jobs in a first-come first-served order until its budget is exhausted or there are no more aperiodic jobs. This way, the server task can provide a guaranteed service level to aperiodic jobs, while still respecting the priorities of periodic and sporadic jobs. There are different types of server tasks, such as polling server, deferrable server, sporadic server, etc., that differ in how they replenish their budgets and handle sporadic jobs.

### Slack Stealing

- Slack stealing is a more sophisticated approach that exploits the available slack times of periodic and sporadic jobs to complete aperiodic jobs early. Slack time is the amount of time that a job can be delayed without missing its deadline. Slack stealing algorithms monitor the slack times of periodic and sporadic jobs and dynamically adjust the priorities of aperiodic jobs to execute them when there is enough slack time. This way, slack stealing algorithms can improve the responsiveness of aperiodic jobs, while still ensuring the schedulability of periodic and sporadic jobs.
- Slack stealing algorithms require online computation of slack times, which can be costly and complex. There are different types of slack stealing algorithms, such as total slack stealing, dynamic slack stealing, hybrid slack stealing, etc., that differ in how they compute and distribute slack times and handle sporadic jobs.

## Scheduling Aperiodic and Sporadic jobs in Clock Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to handle the unpredictability of their arrival times and execution times. Since the schedule is pre-computed offline, it cannot accommodate the dynamic behavior of aperiodic and sporadic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in clock driven systems: overloading and sporadic servers.

### Overloading

- Overloading is a simple and intuitive approach that assigns a fixed time slot to aperiodic jobs and executes them in a first-come first-served order. If an aperiodic job arrives when the time slot is occupied by another aperiodic job, it is queued until the next time slot. This ensures that aperiodic jobs do not interfere with the schedule of periodic jobs, but it also results in poor responsiveness of aperiodic jobs, especially when the time slot is too small or too infrequent.
- Overloading can be improved by using a priority queue, which assigns priorities to aperiodic jobs based on some criteria, such as deadline