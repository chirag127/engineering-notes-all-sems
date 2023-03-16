### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when .
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known .
- A schedule of the jobs is computed off-line and is stored for use at run-time .
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can handle periodic tasks and aperiodic tasks with known arrival times.
- Clock-driven scheduling can also handle sporadic tasks with known minimum inter-arrival times and deadlines.
- Clock-driven scheduling can be implemented using cyclic executives or table-driven schedulers.
- Clock-driven scheduling has some drawbacks, such as:
  - It may not be able to handle dynamic changes in the system or the environment.
  - It may not be able to handle tasks with unknown or variable execution times.
  - It may not be able to handle tasks with unknown or variable arrival times.
  - It may not be able to handle tasks with soft or imprecise deadlines.
  - It may not be able to utilize the processor efficiently.
  - It may require a lot of memory to store the schedule.
  - It may require a lot of computation time to generate the schedule.