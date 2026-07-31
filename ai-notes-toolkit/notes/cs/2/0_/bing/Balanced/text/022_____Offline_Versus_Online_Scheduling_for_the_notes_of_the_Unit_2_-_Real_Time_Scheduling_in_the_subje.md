### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations.
- Online scheduling has the advantage of being flexible and adaptive, as the scheduler can handle dynamic changes in the system such as task arrivals, task aborts, task migrations, etc.
- Offline scheduling requires a static and deterministic system, where the tasks are periodic or sporadic and their parameters are known in advance.
- Online scheduling requires a dynamic and stochastic system, where the tasks are aperiodic or irregular and their parameters are uncertain or variable.
- Offline scheduling is suitable for hard real-time systems that have strict timing constraints and high reliability requirements.
- Online scheduling is suitable for soft real-time systems that have relaxed timing constraints and low criticality levels.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.