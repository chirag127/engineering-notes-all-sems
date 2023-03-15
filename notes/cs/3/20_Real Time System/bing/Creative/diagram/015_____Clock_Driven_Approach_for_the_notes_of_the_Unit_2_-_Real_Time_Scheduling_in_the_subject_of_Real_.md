### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a static schedule for the jobs before the system starts to execute.
- The scheduler uses a table or a program to determine which job to execute at each scheduling point.
- The scheduling points are determined by the interrupts received from a clock.
- This approach to scheduling hard real-time jobs is called the clock-driven or time-driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system.
- It is easy to see why a clock-driven system never exhibits the anomalous timing behavior of priority-driven systems.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some advantages and disadvantages:

  - Advantages:
    - It is simple and easy to implement.
    - It avoids runtime overheads such as context switching and priority computation.
    - It can handle periodic, aperiodic and sporadic jobs with known parameters.
    - It can guarantee the deadlines of all feasible jobs.
  - Disadvantages:
    - It is inflexible and cannot handle dynamic changes in the system.
    - It requires a priori knowledge of all the job parameters and system states.
    - It may waste processor time if the jobs are not evenly distributed.
    - It may not be optimal in terms of resource utilization or response time.