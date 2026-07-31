### Scheduling Aperiodic and Sporadic Jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are those that have no fixed arrival pattern and may arrive at any time. Sporadic jobs are a special case of aperiodic jobs that have a minimum inter-arrival time between successive jobs .
- Aperiodic and sporadic jobs are common in real-time systems, especially in event-driven applications that need to respond to unpredictable external stimuli .
- Scheduling aperiodic and sporadic jobs in real-time systems is challenging because they may interfere with the execution of periodic jobs that have hard deadlines and fixed arrival patterns .
- There are two main approaches to scheduling aperiodic and sporadic jobs in real-time systems: priority driven and clock driven .
- In priority driven systems, each job is assigned a priority based on some criteria, such as deadline, urgency, or importance. The scheduler always selects the highest priority job to execute at any time. Priority driven systems are flexible and adaptive, but they may suffer from priority inversion, blocking, or starvation problems .
- In clock driven systems, each job is assigned a fixed time slot in a periodic schedule that is computed offline. The scheduler follows the precomputed schedule and executes the jobs in their assigned slots. Clock driven systems are predictable and efficient, but they may waste processor time if some jobs do not arrive or finish early .
- There are several techniques to schedule aperiodic and sporadic jobs in priority driven and clock driven systems, such as:
  - Polling servers: a periodic task that polls for the arrival of aperiodic or sporadic jobs and executes them in its allocated time slot .
  - Deferrable servers: a periodic task that defers the execution of aperiodic or sporadic jobs until its allocated time slot, unless there is no other higher priority job ready to execute .
  - Sporadic servers: a periodic task that executes a sporadic job as soon as it arrives, if there is enough budget left in its allocated time slot, otherwise it defers the execution until the next slot .
  - Slack stealing: a technique that utilizes the unused processor time (slack) in the schedule to execute aperiodic or sporadic jobs, without affecting the deadlines of periodic jobs .
  - Background processing: a technique that executes aperiodic or sporadic jobs only when there is no other job ready to execute, with the lowest priority .
  - Dynamic scheduling: a technique that adjusts the priorities or time slots of jobs based on their arrival times, deadlines, or execution times, using online algorithms such as Earliest Deadline First (EDF) or Least Laxity First (LLF) .