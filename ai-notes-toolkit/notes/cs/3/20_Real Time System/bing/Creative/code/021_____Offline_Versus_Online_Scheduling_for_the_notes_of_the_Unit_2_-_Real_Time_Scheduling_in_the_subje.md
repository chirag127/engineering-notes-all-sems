### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal, predictable, and easy to implement, but it has the disadvantage of being inflexible, unable to handle dynamic events, and requiring a lot of offline computation.
- Online scheduling has the advantage of being flexible, adaptive, and able to handle dynamic events, but it has the disadvantage of being suboptimal, unpredictable, and complex to implement.
- Offline scheduling can be either table-driven or program-driven, i.e., the schedule can be stored as a table or as a program that generates the schedule on demand.
- Online scheduling can be either static or dynamic, i.e., the scheduling decisions can be based on fixed priorities or on changing priorities.
- Examples of offline scheduling algorithms are cyclic executive, time-triggered, and rate-monotonic scheduling.
- Examples of online scheduling algorithms are earliest deadline first, least laxity first, and priority-driven scheduling.