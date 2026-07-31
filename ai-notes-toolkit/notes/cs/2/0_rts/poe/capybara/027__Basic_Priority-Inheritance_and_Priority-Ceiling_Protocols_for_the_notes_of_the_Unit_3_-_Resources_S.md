### Basic Priority-Inheritance and Priority-Ceiling Protocols

In real-time systems, it is essential to ensure that resources are properly shared among concurrent tasks without any interference. Two protocols that are commonly used for resource sharing are the Basic Priority-Inheritance Protocol (PIP) and the Priority-Ceiling Protocol (PCP).

#### Basic Priority-Inheritance Protocol (PIP):

1. In this protocol, a task that requires a resource is given the highest priority until it completes its execution. 
2. If another task with a higher priority requests the same resource, the lower priority task is preempted, and the priority of the requesting task is temporarily increased to that of the preempted task.
3. This temporary priority increase is known as priority inheritance. 
4. When the task holding the resource releases it, the priority of the requesting task is reduced to its original priority.

#### Priority-Ceiling Protocol (PCP):

1. In this protocol, each resource is assigned a priority ceiling, which is the highest priority of any task that can potentially block the resource.
2. If a task requests a resource, its priority is raised to the priority ceiling of the resource it wants to access.
3. If the requesting task already has a higher priority than the ceiling priority of the requested resource, then no priority change occurs.
4. This protocol ensures that no task can be preempted by a lower priority task while holding a resource.
5. If a task with a higher priority than the ceiling priority of the resource tries to access it, a priority inversion occurs, which can be resolved using the PIP.

In conclusion, the Basic Priority-Inheritance Protocol and Priority-Ceiling Protocol are two important techniques for resource sharing in real-time systems. These protocols help in avoiding priority inversion and ensure that the resources are shared efficiently among the concurrent tasks.