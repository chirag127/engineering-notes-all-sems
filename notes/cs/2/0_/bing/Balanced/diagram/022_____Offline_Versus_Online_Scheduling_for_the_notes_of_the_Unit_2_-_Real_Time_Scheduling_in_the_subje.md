### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal and predictable, but it requires a static and deterministic system, where all the task parameters and events are known in advance and do not change during the execution.
- Online scheduling has the advantage of being flexible and adaptable, but it requires a dynamic and probabilistic system, where the task parameters and events are unknown or uncertain and may change during the execution.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.