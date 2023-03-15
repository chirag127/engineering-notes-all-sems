### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal, predictable, and easy to implement, but it has the disadvantage of being inflexible, unable to handle dynamic events, and requiring a lot of offline computation.
- Online scheduling has the advantage of being flexible, adaptive, and able to handle dynamic events, but it has the disadvantage of being suboptimal, unpredictable, and complex to implement.
- Offline scheduling can be either static or dynamic, depending on whether the schedule is fixed or can be changed during the run-time.
- Online scheduling can be either static or dynamic, depending on whether the priority of the tasks is fixed or can be changed during the run-time.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.