### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The priority-ceiling protocol works by temporarily raising the priorities of tasks that access shared resources to the priority ceiling of the resource they are accessing. This prevents lower-priority tasks from preempting higher-priority tasks that need the same resource .
- There are two variants of the priority-ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point.
- OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to run .
- The priority-ceiling protocol has several advantages over other synchronization techniques, such as:
  - It prevents deadlock by ensuring that a task can only lock a resource if its priority is higher than the priority ceiling of all the resources currently locked by other tasks .
  - It prevents unbounded priority inversion by ensuring that a task can only be blocked by tasks with higher or equal priority .
  - It allows concurrency among tasks that do not share resources or have compatible resource requirements .
  - It reduces the blocking time of tasks by allowing them to access resources in a predictable order .
  - It simplifies the analysis of the system schedulability and feasibility .