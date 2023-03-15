# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

In real-time systems, there are three types of tasks: periodic, aperiodic, and sporadic. Periodic tasks have a fixed period and deadline, while aperiodic and sporadic tasks have variable arrival times and deadlines. Scheduling aperiodic and sporadic jobs in priority-driven and clock-driven systems is an important aspect of real-time scheduling.

## Priority Driven Systems

In priority-driven systems, tasks are assigned priorities based on their importance, and the scheduler selects the highest priority task to execute. Aperiodic and sporadic jobs can be scheduled using several techniques in priority-driven systems:

1. **Background Scheduling**: Aperiodic and sporadic jobs are assigned the lowest priority and are executed only when no other higher priority tasks are ready to execute. This approach ensures that periodic tasks are not affected by the execution of aperiodic and sporadic jobs, but it may result in long response times for aperiodic and sporadic jobs.

2. **Polling Servers**: A polling server is a periodic task with a fixed period and a fixed execution time. At each period, the server checks if there are any aperiodic or sporadic jobs ready to execute. If there are, the server executes one of the jobs for its fixed execution time. This approach can reduce the response time of aperiodic and sporadic jobs, but it may affect the schedulability of periodic tasks.

3. **Deferrable Servers**: A deferrable server is similar to a polling server, but it can defer its execution if there are no aperiodic or sporadic jobs ready to execute. This approach can improve the schedulability of periodic tasks, but it may result in longer response times for aperiodic and sporadic jobs.

4. **Sporadic Servers**: A sporadic server is a task with a minimum inter-arrival time and a fixed execution time. When an aperiodic or sporadic job arrives, the server is activated and executes the job for its fixed execution time. This approach can provide good response times for aperiodic and sporadic jobs, but it may affect the schedulability of periodic tasks.

## Clock Driven Systems

In clock-driven systems, tasks are scheduled based on a pre-computed schedule. Aperiodic and sporadic jobs can be scheduled using several techniques in clock-driven systems:

1. **Time-Triggered Scheduling**: In time-triggered scheduling, aperiodic and sporadic jobs are assigned specific time slots in the schedule. When a job arrives, it is executed in its assigned time slot. This approach ensures that periodic tasks are not affected by the execution of aperiodic and sporadic jobs, but it may result in long response times for aperiodic and sporadic jobs.

2. **Slack Stealing**: In slack stealing, the scheduler computes the slack time, which is the amount of time that can be used to execute aperiodic and sporadic jobs without affecting the schedulability of periodic tasks. When an aperiodic or sporadic job arrives, the scheduler checks if there is enough slack time to execute the job. If there is, the job is executed, and the slack time is updated. This approach can provide good response times for aperiodic and sporadic jobs, but it requires the scheduler to compute the slack time at runtime.

In conclusion, scheduling aperiodic and sporadic jobs in priority-driven and clock-driven systems is a complex task that requires careful consideration of the trade-offs between the response time of aperiodic and sporadic jobs and the schedulability of periodic tasks. Several techniques can be used to schedule aperiodic and sporadic jobs in both priority-driven and clock-driven systems, and the choice of technique depends on the specific requirements of the system.