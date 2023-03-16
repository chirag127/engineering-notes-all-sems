# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a priority queue or a sorted list to store the tasks and their priorities, and by using a table or a map to store the resources and their priority ceilings .
- Whenever a task requests a resource, we check if its priority is higher than the system ceiling, and if so, we grant the resource and update the system ceiling .
- Whenever a task releases a resource, we update the priority ceiling of the resource and the system ceiling .
- The priority ceiling protocol can prevent deadlock and unbounded priority inversion in dynamic priority systems, but it may introduce some overhead in updating the priority ceilings and the system ceiling .
- The priority ceiling protocol can also be applied to static priority systems, where the priority ceilings and the system ceiling do not change over time .
- There are two variants of the priority ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- The difference between them is that in OCPP, a task inherits the priority ceiling of the resource only when it is blocked by a lower priority task that holds the resource, while in ICPP, a task inherits the priority ceiling of the resource as soon as it locks the resource.
- The worst-case behaviour of the two variants is identical from a scheduling viewpoint, but ICPP may reduce the number of context switches and the blocking time of tasks.