### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a schedule offline, before the system starts to execute, and stores it in a table.
- The schedule is repeated periodically, and each period is called a major cycle.
- The major cycle is the least common multiple of the periods of all the tasks.
- The scheduler uses a clock to determine when to switch tasks according to the schedule table.
- The clock-driven approach is suitable for real-time systems that require predictable and deterministic behaviour.
- The advantages of clock-driven scheduling are :
  - It is easy to verify the schedulability of the system.
  - It avoids the overhead of dynamic scheduling decisions and priority inversion.
  - It can handle aperiodic and sporadic tasks by reserving slots for them in the schedule table.
  - It can exploit the slack time of the tasks to reduce the power consumption of the system.
- The disadvantages of clock-driven scheduling are :
  - It is not flexible to handle dynamic changes in the system, such as task arrivals, deadlines, or resource availability.
  - It may waste processor time if some tasks do not execute or finish early.
  - It requires accurate knowledge of the task parameters and the clock frequency.
  - It may not be scalable for large and complex systems with many tasks and resources.