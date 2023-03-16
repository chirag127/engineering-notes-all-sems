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
    - It avoids run-time overheads such as context switching, priority inversion, and synchronization.
    - It can handle periodic, aperiodic, and sporadic tasks with known parameters.
    - It can guarantee the deadlines of all tasks if the schedule is feasible.
  - Disadvantages:
    - It is not flexible and adaptive to dynamic changes in the system.
    - It may waste processor resources if the schedule is not optimal or the system is underloaded.
    - It may not handle tasks with unknown or variable parameters, such as arrival times, execution times, or deadlines.
    - It may not handle tasks with precedence or resource constraints.