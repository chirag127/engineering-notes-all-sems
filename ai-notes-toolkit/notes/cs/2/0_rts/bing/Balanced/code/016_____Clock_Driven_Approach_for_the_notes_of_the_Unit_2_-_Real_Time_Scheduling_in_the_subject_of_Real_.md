### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when .
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known .
- A schedule of the jobs is computed off-line and is stored for use at run-time .
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some advantages and disadvantages:

  - Advantages:
    - It is simple and easy to implement.
    - It avoids run-time overheads such as context switching and priority management.
    - It can handle periodic, aperiodic and sporadic tasks with known parameters.
    - It can guarantee the deadlines of all the tasks if the schedule is feasible.
  - Disadvantages:
    - It is inflexible and cannot handle dynamic changes in the system such as task arrivals, failures or resource availability.
    - It requires a priori knowledge of all the task parameters and system states.
    - It may waste CPU time if the schedule is not fully utilized.
    - It may not be optimal in terms of performance metrics such as response time or throughput.

- Some examples of clock-driven scheduling algorithms are:

  - Cyclic executive: A simple algorithm that divides the schedule into fixed-length cycles and assigns tasks to slots within each cycle.
  - Time-driven table-driven scheduling: An algorithm that uses a table to store the schedule of tasks for each scheduling decision time.
  - Time-driven state-machine scheduling: An algorithm that uses a state machine to represent the schedule of tasks and transitions between states based on events or conditions.

- A graphical representation of clock-driven scheduling is shown below:

```
|<----------------- Hyperperiod ----------------->|
|<-- Cycle 1 -->|<-- Cycle 2 -->|<-- Cycle 3 -->|...
| T1 | T2 | T3 | T1 | T2 | T4 | T1 | T2 | T3 |...
```

- In this example, there are four tasks: T1, T2, T3 and T4. T1 and T2 are periodic tasks with periods of 3 and 6 units, respectively. T3 and T4 are aperiodic tasks with deadlines of 9 and 12 units, respectively. The schedule is divided into cycles of length 3 units, which is the least common multiple of the periods of T1 and T2. The tasks are assigned to slots within each cycle according to their deadlines and priorities. The hyperperiod is the length of the schedule that repeats itself, which is 12 units in this case.