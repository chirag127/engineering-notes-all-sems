### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-Ceiling Protocol (PCP) is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks that access shared resources and blocking tasks that have lower priorities than the ceiling of the system.
- The ceiling of the system is the highest priority among all the resources currently locked by any task.
- The ceiling of a resource is the highest priority among all the tasks that may request that resource.
- In a dynamic priority system, the priorities of the tasks change with time, but the resources required by each task remain constant.
- Hence, the ceilings of the resources and the system may change with time as well.
- For dynamic systems, PCP can be used to control resource accesses provided that the ceilings of each resource and the system are updated each time the task priorities change.
- PCP can be implemented in two variants: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP raises the priority of a task to the ceiling of the requested resource only when the task locks the resource.
- ICPP raises the priority of a task to the ceiling of the requested resource as soon as the task is ready to run.
- The worst-case behavior of the two variants is identical from a scheduling viewpoint.
- PCP has some advantages over other synchronization protocols, such as Priority Inheritance Protocol (PIP), such as:
  - PCP avoids chained blocking, which occurs when a low-priority task blocks a higher-priority task that in turn blocks another higher-priority task.
  - PCP bounds the blocking time of any task by the maximum execution time of a critical section of any lower-priority task.
  - PCP allows the schedulability analysis of the system to be performed without knowing the exact order of resource requests.
  - PCP can be combined with other techniques, such as slack stealing, to improve the system utilization.