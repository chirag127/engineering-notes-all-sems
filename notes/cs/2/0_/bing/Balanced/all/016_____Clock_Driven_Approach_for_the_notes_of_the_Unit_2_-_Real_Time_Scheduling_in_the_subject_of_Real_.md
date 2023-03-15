# Clock Driven Approach

- Clock driven approach is a scheduling method for hard real-time systems that require predictable and deterministic behaviour.
- In clock driven approach, the system executes tasks according to a predetermined schedule, which is computed offline before the system starts  .
- The schedule is based on the known parameters of the tasks, such as their periods, deadlines, execution times, and resource requirements .
- The schedule is usually cyclic, meaning that it repeats itself after a fixed amount of time, called the cycle or frame .
- The schedule specifies at which time instants, called scheduling points, the system should switch from one task to another  .
- The scheduling points are determined by the interrupts received from a clock, hence the name clock driven.
- The advantages of clock driven approach are:
  - It guarantees that all tasks will meet their deadlines, as long as the schedule is feasible .
  - It avoids the overhead of dynamic scheduling decisions at runtime, which can be significant for hard real-time systems .
  - It simplifies the analysis and verification of the system's timing behaviour .
- The disadvantages of clock driven approach are:
  - It requires that all the task parameters are known and fixed in advance, which may not be realistic for some applications .
  - It may not be able to handle sporadic or aperiodic tasks, which have unpredictable arrival times or deadlines .
  - It may not be able to adapt to changes in the system's state or environment, such as faults, failures, or resource variations .
  - It may waste processor time and energy by executing tasks that are not necessary or urgent .