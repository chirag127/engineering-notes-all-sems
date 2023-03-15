### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource.
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling viewpoint.
- Both variants work by temporarily raising the priorities of tasks.
- The ceiling priority protocol Stack-Based Priority Ceiling Protocol is based on original work to allow jobs to share a run-time stack, extended to control access to other resources .
- In the statement of the rules of the stack-based, priority-ceiling protocol, we again use the term (current) ceiling ˆ f (t) of the system, which is the highest-priority ceiling of all the resources that are in use at time t Ω. is a nonexisting priority level that is lower than the lowest priority of all jobs.