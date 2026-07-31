# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler makes each scheduling decision without knowledge about the tasks that will be released in future and parameter of each task known to scheduler only after release of task.
- Offline scheduling can be either static or dynamic, depending on whether the schedule is fixed or can be modified during the run-time.
- Online scheduling can be either static or dynamic, depending on whether the priority of the tasks is fixed or can be changed during the run-time.
- Offline scheduling has the advantage of being optimal, since it can exploit the complete information about the tasks and their requirements.
- Online scheduling has the advantage of being flexible, since it can adapt to the unpredictable changes in the system state and workload.
- Offline scheduling has the disadvantage of being inflexible, since it cannot handle the uncertainties and variations in the system behavior and environment.
- Online scheduling has the disadvantage of being suboptimal, since it has to make decisions based on limited and incomplete information about the tasks and their requirements.
- Offline scheduling is suitable for systems that have predictable and deterministic task sets, such as embedded systems and control systems.
- Online scheduling is suitable for systems that have unpredictable and dynamic task sets, such as interactive systems and multimedia systems.
- An example of offline scheduling is table-driven scheduling, where a table is generated that contains the necessary scheduling decisions for use during the run-time.
- An example of online scheduling is priority-driven scheduling, where the scheduler assigns a priority to each task and selects the highest priority task for execution at each scheduling point.