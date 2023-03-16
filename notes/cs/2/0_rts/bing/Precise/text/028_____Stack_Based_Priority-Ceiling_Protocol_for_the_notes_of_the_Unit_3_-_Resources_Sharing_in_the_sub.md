### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol is based on original work to allow jobs to share a run-time stack, extended to control access to other resources .
- In the statement of the rules of the stack-based, priority-ceiling protocol, we again use the term (current) ceiling ˆ f (t) of the system, which is the highest-priority ceiling of all the resources that are in use at time t Ω. is a nonexisting priority level that is lower than the lowest priority of all jobs.
- Stack Based Priority-ceiling Protocol has two rules:
  1. Scheduling Rule: After a job is released, it is blocked from starting execution until its assigned priority is higher.
  2. Allocation Rule: Whenever a job requests a resource, it is allocated the resource.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point. Both variants work by temporarily raising the priorities of tasks.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways. Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.