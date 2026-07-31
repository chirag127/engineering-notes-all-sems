### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They may have soft or hard deadlines, or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They usually have hard deadlines. Examples are interrupts, sensor readings, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a pre-defined schedule that is determined offline. The scheduler follows the schedule and switches jobs at fixed time instants. Examples are cyclic executive, time triggered architecture, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in real-time systems is to balance the responsiveness of these jobs with the schedulability of the periodic jobs, which are usually more critical and have hard deadlines.
- There are different approaches to schedule aperiodic and sporadic jobs in priority driven and clock driven systems, such as:

  - Polling servers: A periodic task with a fixed priority and budget is used to serve the aperiodic and sporadic jobs in a FIFO order. The server replenishes its budget at the beginning of each period. Examples are periodic, deferrable, and sporadic servers.
  - Slack stealing: The scheduler uses the available slack times of periodic and sporadic jobs to complete aperiodic jobs early. The slack time of a job is the difference between its latest start time and its current time. Examples are background, total bandwidth, and dynamic slack stealing algorithms.
  - Reservation based: The scheduler reserves a portion of the processor bandwidth for the aperiodic and sporadic jobs, and allocates the remaining bandwidth for the periodic jobs. The reservation can be fixed or variable, depending on the system requirements. Examples are constant, variable, and harmonic utilization servers.
  - Hybrid: The scheduler combines two or more of the above approaches to achieve better performance and flexibility. Examples are priority exchange, priority exchange with slack stealing, etc.

- In clock driven systems, the scheduling of aperiodic and sporadic jobs is more difficult, because the schedule is fixed and predetermined, and the system has less flexibility to accommodate dynamic events. Some possible solutions are:

  - Insert idle slots in the schedule to handle aperiodic and sporadic jobs. The scheduler can use a priority queue or a FIFO queue to select the next job to execute in the idle slot. The drawback is that the system utilization is reduced and the response time of the jobs may be long.
  - Overload the schedule to handle aperiodic and sporadic jobs. The scheduler can use a priority queue or a FIFO queue to select the next job to execute, and preempt the current job if it has a lower priority. The drawback is that the system may become unstable and the periodic jobs may miss their deadlines.
  - Use a separate processor or a co-processor to handle aperiodic and sporadic jobs. The scheduler can use a priority queue or a FIFO queue to select the next job to execute on the dedicated processor. The drawback is that the system cost and complexity are increased and the communication overhead may be high.