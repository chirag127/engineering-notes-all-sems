### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations.
- Online scheduling has the advantage of being flexible and adaptable, as the scheduler can handle dynamic changes in the system, such as arrival of new tasks, variations in execution times, resource failures, etc.
- Offline scheduling requires a static and deterministic system, where the tasks are periodic and have fixed parameters and no dependencies.
- Online scheduling can handle a dynamic and stochastic system, where the tasks can be aperiodic, sporadic, or have variable parameters and precedence constraints.
- Offline scheduling can be implemented by using a table-driven approach, where the scheduler simply follows a pre-defined table that contains the necessary scheduling decisions for each time instant.
- Online scheduling can be implemented by using a priority-driven approach, where the scheduler assigns a priority to each task based on some criteria and selects the highest priority task for execution at each time instant.