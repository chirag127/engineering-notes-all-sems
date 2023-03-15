# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler makes each scheduling decision without knowledge about the tasks that will be released in future and parameter of each task known to scheduler only after release of task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations or resource conflicts.
- Online scheduling has the advantage of being flexible and adaptive, as the scheduler can handle dynamic changes in the system such as arrival of new tasks, variations in execution time, or failures of resources.
- Offline scheduling has the disadvantage of being rigid and static, as the scheduler cannot cope with any uncertainty or unpredictability in the system such as changes in task parameters, workload, or environment.
- Online scheduling has the disadvantage of being complex and heuristic, as the scheduler has to make quick and efficient decisions based on limited and incomplete information and trade-off between different objectives and constraints.
- Offline scheduling is suitable for systems that have fixed and known set of tasks, deterministic and constant execution time, and no external disturbances or interferences.
- Online scheduling is suitable for systems that have variable and unknown set of tasks, stochastic and varying execution time, and external disturbances or interferences.
- Examples of offline scheduling are table-driven scheduling, cyclic scheduling, and time-triggered scheduling.
- Examples of online scheduling are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.