# Clock Driven Approach

- Clock driven approach is also known as time driven approach or cyclic scheduling .
- In this approach, the system executes tasks according to a predetermined schedule .
- The schedule is computed offline before the system starts running  .
- The schedule is based on the known parameters of the tasks, such as period, deadline, execution time, and precedence constraints .
- The schedule is usually periodic and cyclic, meaning that it repeats itself after a fixed interval of time  .
- The schedule specifies the exact time instants when each task should start and finish execution .
- The scheduling decisions are made at specific time points, independent of events, such as job releases and completions, in the system  .
- The advantages of clock driven approach are:
  - It guarantees the feasibility and timeliness of hard real-time tasks .
  - It avoids the overhead of dynamic scheduling, such as priority assignment, context switching, and preemption .
  - It simplifies the analysis and verification of the system .
  - It eliminates the possibility of anomalous timing behavior, such as priority inversion and deadline misses, that may occur in priority driven systems  .
- The disadvantages of clock driven approach are:
  - It requires the complete knowledge of the task parameters and system configuration .
  - It cannot handle unpredictable or aperiodic tasks, such as interrupts, faults, or user inputs .
  - It may waste CPU resources if the tasks are not fully utilized or if the schedule is not optimal .
  - It may be difficult to update or modify the schedule if the task parameters or system configuration change .