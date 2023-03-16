### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The priority-ceiling protocol works by temporarily raising the priorities of tasks that access shared resources to the priority ceiling of the resource they are accessing. This prevents lower-priority tasks from preempting higher-priority tasks that need the same resource .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point.
- OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute and has a resource request pending .
- The priority-ceiling protocol has several advantages over other synchronization techniques, such as priority inheritance protocol, such as:
  - It avoids deadlock by preventing circular waiting among tasks that need multiple resources .
  - It bounds the blocking time of any task by at most one critical section of a lower-priority task .
  - It reduces the number of context switches and the overhead of priority management .
  - It allows for simple and efficient implementation in both static and dynamic priority systems .
- The priority-ceiling protocol also has some limitations, such as:
  - It requires a priori knowledge of the resource requirements of each task and the priority ceiling of each resource .
  - It may cause unnecessary blocking of lower-priority tasks that do not contend for the same resources as higher-priority tasks .
  - It may not be optimal for some task sets and resource allocation policies .