### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-Ceiling Protocol (PCP) is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks that access shared resources and blocking tasks that have lower priorities than the ceiling of the system.
- PCP can be applied to dynamic priority systems, where the priorities of the periodic tasks change with time, but the resources required by each task remain constant.
- To use PCP in dynamic priority systems, the following steps are needed:
  - Assign a priority ceiling to each resource, which is the highest priority of any task that may access it.
  - Update the priority ceiling of each resource and the ceiling of the system each time task priorities change.
  - When a task requests a resource, check if its priority is higher than the ceiling of the system. If yes, grant the resource and raise the task's priority to the ceiling of the resource. If no, block the task and put it in a waiting queue.
  - When a task releases a resource, restore its original priority and check the waiting queue for the highest priority task that can be granted the resource.
- PCP ensures that at any time, at most one resource is accessed by more than one task, and the tasks that access the same resource are executed in the order of their original priorities.
- PCP also ensures that a task can be blocked by at most one lower priority task, and the blocking time is bounded by the worst-case execution time of the lower priority task.