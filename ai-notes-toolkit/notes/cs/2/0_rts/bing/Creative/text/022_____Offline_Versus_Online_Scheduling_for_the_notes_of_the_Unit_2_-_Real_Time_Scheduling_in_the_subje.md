### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have the prior information related to the task parameters and has to make decisions based on the current state of the system.
- Offline scheduling has the advantage of being optimal, predictable, and easy to implement, but it has the disadvantage of being inflexible, unable to handle dynamic events, and requiring a lot of offline computation.
- Online scheduling has the advantage of being adaptable, responsive, and able to handle uncertainties, but it has the disadvantage of being suboptimal, complex, and requiring a lot of run-time overhead.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.