### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a static schedule offline, before the system starts to execute, and follows the schedule at runtime.
- A static schedule is a sequence of scheduling decisions that specifies which job executes on which processor at any given time.
- A periodic static schedule is a cyclic schedule that repeats itself after a fixed period of time .
- This approach to scheduling hard real-time jobs is called the clock-driven or time-driven approach because each scheduling decision is made at a specific time, independent of events, such as job releases and completions, in the system.
- It is easy to see why a clock-driven system never exhibits the anomalous timing behavior of priority-driven systems.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some drawbacks, such as:
  - It may not be able to handle aperiodic or sporadic jobs well.
  - It may not be able to adapt to dynamic changes in the system, such as faults, overloads, or resource variations.
  - It may incur high overhead due to frequent context switches and clock interrupts.
  - It may waste processor time due to idle slots or fragmentation.