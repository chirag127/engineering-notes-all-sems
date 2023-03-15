### Clock Driven Approach

- Clock driven scheduling is also called as time-driven scheduling.
- When scheduling is clock driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock driven scheduler computes a static schedule for the jobs before the system starts to execute.
- The static schedule is periodic and cyclic, meaning that it repeats itself after a fixed amount of time .
- The scheduler uses a clock to trigger the execution of the jobs according to the static schedule.
- The clock driven approach is suitable for real-time systems that require predictable and deterministic behaviour.
- The advantages of clock driven scheduling are :
  - It is easy to verify the schedulability of the system and guarantee the deadlines of the jobs.
  - It avoids the overhead of dynamic scheduling decisions and context switches.
  - It eliminates the possibility of priority inversion and timing anomalies.
- The disadvantages of clock driven scheduling are :
  - It is inflexible and cannot handle aperiodic or sporadic jobs easily.
  - It is inefficient and may waste processor time if the jobs are not evenly distributed.
  - It is sensitive to changes in the system parameters and may require recomputation of the schedule.