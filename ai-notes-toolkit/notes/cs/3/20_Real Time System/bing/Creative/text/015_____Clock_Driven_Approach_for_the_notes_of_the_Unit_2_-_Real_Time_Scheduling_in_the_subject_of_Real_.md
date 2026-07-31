### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a schedule for a set of periodic tasks offline, before the system starts to execute.
- The schedule is stored in a table and is repeated periodically at runtime.
- The schedule is based on the worst-case execution times, periods, and deadlines of the tasks.
- The scheduler does not need to consider the actual execution times, releases, and completions of the tasks at runtime.
- The scheduler only needs to consult the table and dispatch the tasks according to the predetermined schedule.
- The advantages of clock-driven scheduling are:
  - It is predictable and deterministic, which is desirable for hard real-time systems.
  - It is simple and efficient, as it does not require complex online computations or priority comparisons.
  - It avoids the anomalous timing behavior of priority-driven systems, such as priority inversion and deadline misses.
- The disadvantages of clock-driven scheduling are:
  - It is inflexible and rigid, as it cannot handle dynamic changes in the system, such as task arrivals, departures, or variations in execution times.
  - It is pessimistic and wasteful, as it assumes the worst-case scenarios for all tasks and does not utilize the slack time.
  - It is difficult to construct and maintain, as it requires a priori knowledge of all task parameters and a global analysis of the system.