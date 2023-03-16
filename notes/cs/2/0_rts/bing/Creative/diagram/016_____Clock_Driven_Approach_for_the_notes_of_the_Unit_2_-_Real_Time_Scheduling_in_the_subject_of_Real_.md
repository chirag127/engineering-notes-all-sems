### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a schedule offline, before the system starts to execute, and stores it in a table.
- The scheduler consults the table at each scheduling point and dispatches the jobs accordingly.
- The scheduling points are determined by the release times and deadlines of the jobs.
- A clock-driven scheduler can handle periodic, sporadic, and aperiodic jobs, as long as their parameters are known in advance.
- A clock-driven scheduler can also handle precedence constraints among jobs, as long as they are specified in advance.
- A clock-driven scheduler can guarantee that all the jobs will meet their deadlines, if the system is schedulable.
- A clock-driven scheduler does not depend on the actual execution times of the jobs, as long as they do not exceed their worst-case execution times.
- A clock-driven scheduler does not need to handle interrupts or context switches, which can reduce the overhead and latency.
- A clock-driven scheduler can also exploit the slack time of the jobs to perform energy management or fault tolerance techniques.

Some advantages of clock-driven scheduling are:

- Predictable and deterministic behaviour.
- No anomalous timing behaviour.
- No need for runtime priority assignment or queue management.
- Easy to verify and validate.

Some disadvantages of clock-driven scheduling are:

- Lack of flexibility and adaptability to dynamic changes.
- High memory requirement for storing the schedule table.
- Difficulty in handling jobs with variable execution times or arrival rates.
- Difficulty in handling jobs with soft or imprecise deadlines.
- Difficulty in handling jobs with complex dependencies or synchronization.
- Difficulty in handling jobs with different criticality levels.