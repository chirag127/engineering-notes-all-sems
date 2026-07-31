### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- A dynamic priority system is a system where the priorities of the periodic tasks change with time, while the resources required by each task remain constant .
- A priority-ceiling protocol is a job task synchronization protocol that prevents deadlock and unbounded priority inversion in a real-time system .
- There are two variants of the priority-ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- Both variants work by temporarily raising the priorities of tasks that access shared resources to the highest priority of any task that may access the same resource .
- The difference between OCPP and ICPP is that OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute .
- The priority ceiling of a resource is the highest priority of any task that may access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- In a dynamic priority system, the priority ceilings of the resources may change with time, depending on the changing priorities of the tasks .
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses, provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- The priority-ceiling protocol ensures that a task will not be blocked by a lower priority task for more than one critical section, and that the blocking time is bounded by the worst-case execution time of the highest priority task that may access the same resource .
- The priority-ceiling protocol also prevents circular wait and hence deadlock, by ensuring that a task can lock a resource only if it does not violate the priority order of the resources .
- The priority-ceiling protocol improves the schedulability and predictability of real-time systems, by reducing the blocking time and the number of preemptions .