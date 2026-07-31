### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameter of each task is known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations.
- Online scheduling has the advantage of being flexible and adaptive, as the scheduler can handle dynamic changes in the system such as task arrivals, task terminations, task suspensions, resource failures, etc.
- Offline scheduling has the disadvantage of being rigid and impractical, as the scheduler requires complete and accurate knowledge of the system parameters and behavior, which is often unrealistic or unavailable in real-time systems.
- Online scheduling has the disadvantage of being suboptimal and uncertain, as the scheduler may not be able to guarantee the deadlines of all the tasks due to the lack of information and the unpredictability of the system.
- Offline scheduling is suitable for static and deterministic systems, where the tasks have fixed and known characteristics and the system does not change during the execution.
- Online scheduling is suitable for dynamic and stochastic systems, where the tasks have variable and unknown characteristics and the system may change during the execution.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, etc.
- Examples of online scheduling algorithms are priority-driven scheduling, earliest deadline first scheduling, rate monotonic scheduling, etc.