### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have the prior information related to the tasks and the parameters of each task are known to the scheduler only after the release of the task. Online scheduling can be either static or dynamic.
- The advantages of offline scheduling are:
  - It can guarantee the schedulability of all hard real-time tasks, as the schedule is computed in advance and verified before execution.
  - It can optimize the system performance, as the scheduler can choose the best order and allocation of tasks based on the global information.
  - It can reduce the run-time overhead, as the scheduler only needs to follow the pre-computed schedule and does not need to perform complex computations or comparisons at run-time.
- The disadvantages of offline scheduling are:
  - It requires the system to be predictable and deterministic, i.e., the tasks must have fixed and known parameters and the system must not have any uncertainties or disturbances.
  - It cannot handle dynamic changes or events, such as task arrivals, failures, or variations, as the schedule is fixed and cannot be modified at run-time.
  - It may not be feasible or practical, as the offline computation of the schedule may be too complex or time-consuming, especially for large-scale or heterogeneous systems.
- The advantages of online scheduling are:
  - It can handle dynamic changes or events, such as task arrivals, failures, or variations, as the scheduler can adapt the schedule according to the current system state and the available information.
  - It does not require the system to be predictable and deterministic, i.e., the tasks can have variable or unknown parameters and the system can have uncertainties or disturbances.
  - It can be feasible and practical, as the online computation of the schedule can be simpler or faster, especially for small-scale or homogeneous systems.
- The disadvantages of online scheduling are:
  - It may not guarantee the schedulability of all hard real-time tasks, as the scheduler may not have enough information or time to make the optimal scheduling decisions.
  - It may not optimize the system performance, as the scheduler may only choose the local optimal or suboptimal order and allocation of tasks based on the partial information.
  - It may increase the run-time overhead, as the scheduler may need to perform complex computations or comparisons at run-time.