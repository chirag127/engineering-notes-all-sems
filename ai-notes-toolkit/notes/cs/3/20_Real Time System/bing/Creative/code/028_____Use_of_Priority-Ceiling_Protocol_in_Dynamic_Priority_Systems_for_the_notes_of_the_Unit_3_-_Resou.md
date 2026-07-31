### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The priority ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections .
- The protocol works by temporarily raising the priorities of tasks that access shared resources to the priority ceiling of the resource, and blocking any lower priority tasks from preempting them .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point .
- The difference between OCPP and ICPP is that in OCPP, the priority of a task is raised to the priority ceiling of the resource only when it accesses the resource, while in ICPP, the priority of a task is raised to the priority ceiling of the resource as soon as it is ready to execute .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The ceiling of the system is the highest priority ceiling of all the resources currently accessed by any task .
- The priority ceiling protocol ensures that a task can access a resource only if its current priority is higher than the ceiling of the system, and that no task can be blocked for more than one critical section .
- The priority ceiling protocol also prevents deadlocks due to circular waiting for resources, as a task can only access a resource if it has a higher priority than any other task that may need the same resource .
- The priority ceiling protocol can be implemented using semaphores, mutexes, or monitors, depending on the programming language and the operating system.